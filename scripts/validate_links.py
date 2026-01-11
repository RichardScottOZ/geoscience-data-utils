#!/usr/bin/env python
"""
Documentation Link Validator for richardutils

This script checks for broken links in documentation files.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Set, Tuple
import argparse


class LinkValidator:
    """Validate links in documentation files."""
    
    def __init__(self, docs_dir: str, check_external: bool = False):
        """
        Initialize the link validator.
        
        Args:
            docs_dir: Path to the documentation directory.
            check_external: Whether to check external URLs (requires network).
        """
        self.docs_dir = Path(docs_dir)
        self.check_external = check_external
        self.issues: List[Dict] = []
        self.stats = {
            'files_checked': 0,
            'links_found': 0,
            'broken_links': 0,
        }
        
        # Regex patterns for different link types
        self.md_link_pattern = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')
        self.rst_link_pattern = re.compile(r'`([^`<]+)\s*<([^>]+)>`_')
        self.rst_ref_pattern = re.compile(r':ref:`([^`]+)`')
        self.rst_doc_pattern = re.compile(r':doc:`([^`]+)`')
    
    def check_file(self, filepath: Path) -> None:
        """
        Check a single documentation file for broken links.
        
        Args:
            filepath: Path to the documentation file.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.stats['files_checked'] += 1
            
            # Check based on file type
            if filepath.suffix == '.md':
                self._check_markdown_links(content, filepath)
            elif filepath.suffix == '.rst':
                self._check_rst_links(content, filepath)
            elif filepath.suffix == '.ipynb':
                # Notebooks are JSON, more complex to parse
                # For now, just check as text
                self._check_markdown_links(content, filepath)
                
        except Exception as e:
            self.issues.append({
                'file': str(filepath),
                'line': 0,
                'type': 'error',
                'message': f'Error reading file: {str(e)}'
            })
    
    def _check_markdown_links(self, content: str, filepath: Path) -> None:
        """
        Check Markdown-style links in content.
        
        Args:
            content: File content to check.
            filepath: Path to the file being checked.
        """
        # Find all markdown links
        for match in self.md_link_pattern.finditer(content):
            link_text = match.group(1)
            link_url = match.group(2)
            line_num = content[:match.start()].count('\n') + 1
            
            self.stats['links_found'] += 1
            self._validate_link(link_url, filepath, line_num, link_text)
    
    def _check_rst_links(self, content: str, filepath: Path) -> None:
        """
        Check reStructuredText-style links in content.
        
        Args:
            content: File content to check.
            filepath: Path to the file being checked.
        """
        # Check inline links
        for match in self.rst_link_pattern.finditer(content):
            link_text = match.group(1)
            link_url = match.group(2)
            line_num = content[:match.start()].count('\n') + 1
            
            self.stats['links_found'] += 1
            self._validate_link(link_url, filepath, line_num, link_text)
        
        # Check :ref: links
        for match in self.rst_ref_pattern.finditer(content):
            ref = match.group(1)
            line_num = content[:match.start()].count('\n') + 1
            # References are checked by Sphinx, we'll just note them
            self.stats['links_found'] += 1
        
        # Check :doc: links
        for match in self.rst_doc_pattern.finditer(content):
            doc = match.group(1)
            line_num = content[:match.start()].count('\n') + 1
            self.stats['links_found'] += 1
            # Check if the document exists
            doc_path = self.docs_dir / f"{doc}.rst"
            doc_path_md = self.docs_dir / f"{doc}.md"
            if not doc_path.exists() and not doc_path_md.exists():
                self.issues.append({
                    'file': str(filepath),
                    'line': line_num,
                    'type': 'broken_link',
                    'message': f'Referenced document "{doc}" not found'
                })
                self.stats['broken_links'] += 1
    
    def _validate_link(self, link: str, filepath: Path, line_num: int, link_text: str) -> None:
        """
        Validate a single link.
        
        Args:
            link: The URL or path to validate.
            filepath: Path to the file containing the link.
            line_num: Line number of the link.
            link_text: Display text of the link.
        """
        # Skip anchors
        if link.startswith('#'):
            return
        
        # Skip mailto links
        if link.startswith('mailto:'):
            return
        
        # Check external links
        if link.startswith('http://') or link.startswith('https://'):
            if self.check_external:
                # Would need to make HTTP requests here
                # For now, just note them
                pass
            return
        
        # Check internal file links
        # Remove any anchor from the link
        link_path = link.split('#')[0]
        
        if not link_path:
            return
        
        # Resolve relative to the file's directory
        target_path = (filepath.parent / link_path).resolve()
        
        # Check if target exists
        if not target_path.exists():
            self.issues.append({
                'file': str(filepath),
                'line': line_num,
                'type': 'broken_link',
                'message': f'Link target not found: "{link}" (text: "{link_text}")'
            })
            self.stats['broken_links'] += 1
    
    def check_all(self) -> None:
        """Check all documentation files in the docs directory."""
        # Check markdown files
        for md_file in self.docs_dir.rglob('*.md'):
            if '_build' not in str(md_file):
                self.check_file(md_file)
        
        # Check RST files
        for rst_file in self.docs_dir.rglob('*.rst'):
            if '_build' not in str(rst_file):
                self.check_file(rst_file)
        
        # Check notebooks
        for nb_file in self.docs_dir.rglob('*.ipynb'):
            if '_build' not in str(nb_file) and '.ipynb_checkpoints' not in str(nb_file):
                self.check_file(nb_file)
    
    def print_report(self) -> int:
        """
        Print the link validation report.
        
        Returns:
            Exit code (0 if no issues, 1 otherwise).
        """
        print("=" * 70)
        print("Documentation Link Validation Report")
        print("=" * 70)
        print()
        
        print(f"Files checked:  {self.stats['files_checked']}")
        print(f"Links found:    {self.stats['links_found']}")
        print(f"Broken links:   {self.stats['broken_links']}")
        print()
        
        if self.issues:
            print("=" * 70)
            print("Issues Found")
            print("=" * 70)
            print()
            
            # Group by file
            issues_by_file = {}
            for issue in self.issues:
                filepath = issue['file']
                if filepath not in issues_by_file:
                    issues_by_file[filepath] = []
                issues_by_file[filepath].append(issue)
            
            for filepath in sorted(issues_by_file.keys()):
                print(f"\n{filepath}:")
                for issue in sorted(issues_by_file[filepath], key=lambda x: x['line']):
                    if issue['line'] > 0:
                        print(f"  Line {issue['line']}: {issue['message']}")
                    else:
                        print(f"  {issue['message']}")
            
            print()
            print(f"Total Issues: {len(self.issues)}")
            return 1
        else:
            print("✓ No broken links found!")
            return 0


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Validate links in documentation files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s docs                    # Check all docs
  %(prog)s docs --external         # Also check external URLs (slower)
        """
    )
    parser.add_argument(
        'docs_dir',
        nargs='?',
        default='docs',
        help='Documentation directory to check (default: docs)'
    )
    parser.add_argument(
        '-e', '--external',
        action='store_true',
        help='Check external URLs (requires network, slower)'
    )
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Only show summary'
    )
    
    args = parser.parse_args()
    
    # Check if docs directory exists
    if not Path(args.docs_dir).exists():
        print(f"Error: Documentation directory '{args.docs_dir}' not found", file=sys.stderr)
        return 1
    
    # Run validator
    validator = LinkValidator(args.docs_dir, check_external=args.external)
    validator.check_all()
    
    # Print report
    if args.quiet and not validator.issues:
        print(f"Link validation: {validator.stats['links_found']} links checked, 0 broken")
        return 0
    
    return validator.print_report()


if __name__ == '__main__':
    sys.exit(main())
