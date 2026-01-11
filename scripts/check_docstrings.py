#!/usr/bin/env python
"""
Docstring Coverage Checker for richardutils

This script analyzes Python source files to check docstring coverage
and validate docstring format.
"""

import ast
import sys
import os
from pathlib import Path
from typing import List, Dict, Tuple, Set
import re


class DocstringChecker:
    """Check docstring coverage and format in Python files."""
    
    def __init__(self, source_dir: str):
        """
        Initialize the docstring checker.
        
        Args:
            source_dir: Path to the source directory to check.
        """
        self.source_dir = Path(source_dir)
        self.stats = {
            'total_functions': 0,
            'documented_functions': 0,
            'total_classes': 0,
            'documented_classes': 0,
            'total_modules': 0,
            'documented_modules': 0,
        }
        self.issues: List[Dict] = []
        
    def check_file(self, filepath: Path) -> None:
        """
        Check a single Python file for docstring coverage.
        
        Args:
            filepath: Path to the Python file to check.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                source = f.read()
            
            tree = ast.parse(source, filename=str(filepath))
            self._check_node(tree, filepath)
            
        except SyntaxError as e:
            self.issues.append({
                'file': str(filepath),
                'line': e.lineno or 0,
                'type': 'syntax_error',
                'message': f'Syntax error: {e.msg}'
            })
        except Exception as e:
            self.issues.append({
                'file': str(filepath),
                'line': 0,
                'type': 'error',
                'message': f'Error processing file: {str(e)}'
            })
    
    def _check_node(self, node: ast.AST, filepath: Path, parent_name: str = '') -> None:
        """
        Recursively check AST nodes for docstrings.
        
        Args:
            node: AST node to check.
            filepath: Path to the file being checked.
            parent_name: Name of parent class/function (for nested items).
        """
        if isinstance(node, ast.Module):
            self.stats['total_modules'] += 1
            docstring = ast.get_docstring(node)
            if docstring:
                self.stats['documented_modules'] += 1
            else:
                self.issues.append({
                    'file': str(filepath),
                    'line': 1,
                    'type': 'missing_docstring',
                    'message': 'Module missing docstring'
                })
        
        elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
            # Skip private functions (those starting with _)
            if not node.name.startswith('_'):
                full_name = f"{parent_name}.{node.name}" if parent_name else node.name
                self.stats['total_functions'] += 1
                
                docstring = ast.get_docstring(node)
                if docstring:
                    self.stats['documented_functions'] += 1
                    self._check_docstring_format(docstring, full_name, node.lineno, filepath)
                else:
                    self.issues.append({
                        'file': str(filepath),
                        'line': node.lineno,
                        'type': 'missing_docstring',
                        'message': f'Function "{full_name}" missing docstring'
                    })
        
        elif isinstance(node, ast.ClassDef):
            # Skip private classes
            if not node.name.startswith('_'):
                full_name = f"{parent_name}.{node.name}" if parent_name else node.name
                self.stats['total_classes'] += 1
                
                docstring = ast.get_docstring(node)
                if docstring:
                    self.stats['documented_classes'] += 1
                else:
                    self.issues.append({
                        'file': str(filepath),
                        'line': node.lineno,
                        'type': 'missing_docstring',
                        'message': f'Class "{full_name}" missing docstring'
                    })
                
                # Check class methods
                for child in node.body:
                    self._check_node(child, filepath, full_name)
                return  # Don't continue with generic iteration
        
        # Recursively check child nodes
        for child in ast.iter_child_nodes(node):
            self._check_node(child, filepath, parent_name)
    
    def _check_docstring_format(self, docstring: str, name: str, line: int, filepath: Path) -> None:
        """
        Check docstring format for common issues.
        
        Args:
            docstring: The docstring text to check.
            name: Name of the function/class/module.
            line: Line number where the item is defined.
            filepath: Path to the file being checked.
        """
        # Check for common docstring format issues
        
        # Check for Args section if there are arguments expected
        if 'Args:' not in docstring and 'Arguments:' not in docstring:
            # This is just informational, not always required
            pass
        
        # Check for Returns section for functions that might return values
        # (heuristic: not checking thoroughly)
        
        # Check for Examples section (recommended but not required)
        if '>>>' in docstring:
            # Has examples, check they follow doctest format
            if 'Examples:' not in docstring and 'Example:' not in docstring:
                self.issues.append({
                    'file': str(filepath),
                    'line': line,
                    'type': 'docstring_format',
                    'message': f'"{name}" has doctest examples without "Examples:" header'
                })
    
    def check_all(self) -> None:
        """Check all Python files in the source directory."""
        python_files = list(self.source_dir.rglob('*.py'))
        
        for filepath in python_files:
            # Skip version files and __pycache__
            if '_version.py' in str(filepath) or '__pycache__' in str(filepath):
                continue
            self.check_file(filepath)
    
    def print_report(self) -> int:
        """
        Print the docstring coverage report.
        
        Returns:
            Exit code (0 if no issues, 1 otherwise).
        """
        print("=" * 70)
        print("Docstring Coverage Report")
        print("=" * 70)
        print()
        
        # Calculate percentages
        func_coverage = (
            (self.stats['documented_functions'] / self.stats['total_functions'] * 100)
            if self.stats['total_functions'] > 0 else 100
        )
        class_coverage = (
            (self.stats['documented_classes'] / self.stats['total_classes'] * 100)
            if self.stats['total_classes'] > 0 else 100
        )
        module_coverage = (
            (self.stats['documented_modules'] / self.stats['total_modules'] * 100)
            if self.stats['total_modules'] > 0 else 100
        )
        
        print(f"Module Coverage:   {self.stats['documented_modules']}/{self.stats['total_modules']} ({module_coverage:.1f}%)")
        print(f"Class Coverage:    {self.stats['documented_classes']}/{self.stats['total_classes']} ({class_coverage:.1f}%)")
        print(f"Function Coverage: {self.stats['documented_functions']}/{self.stats['total_functions']} ({func_coverage:.1f}%)")
        print()
        
        # Overall coverage
        total_items = (
            self.stats['total_modules'] + 
            self.stats['total_classes'] + 
            self.stats['total_functions']
        )
        documented_items = (
            self.stats['documented_modules'] + 
            self.stats['documented_classes'] + 
            self.stats['documented_functions']
        )
        overall_coverage = (documented_items / total_items * 100) if total_items > 0 else 100
        
        print(f"Overall Coverage:  {documented_items}/{total_items} ({overall_coverage:.1f}%)")
        print()
        
        # Print issues grouped by file
        if self.issues:
            print("=" * 70)
            print("Issues Found")
            print("=" * 70)
            print()
            
            # Group issues by file
            issues_by_file = {}
            for issue in self.issues:
                filepath = issue['file']
                if filepath not in issues_by_file:
                    issues_by_file[filepath] = []
                issues_by_file[filepath].append(issue)
            
            # Sort by file and line number
            for filepath in sorted(issues_by_file.keys()):
                print(f"\n{filepath}:")
                for issue in sorted(issues_by_file[filepath], key=lambda x: x['line']):
                    print(f"  Line {issue['line']}: [{issue['type']}] {issue['message']}")
            
            print()
            print(f"Total Issues: {len(self.issues)}")
            return 1
        else:
            print("✓ No issues found!")
            return 0


def main():
    """Main entry point for the script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Check docstring coverage in Python source files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s src/richardutils          # Check all files in directory
  %(prog)s src/richardutils --quiet  # Show only summary
        """
    )
    parser.add_argument(
        'source_dir',
        nargs='?',
        default='src/richardutils',
        help='Source directory to check (default: src/richardutils)'
    )
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Only show summary, not individual issues'
    )
    parser.add_argument(
        '--min-coverage',
        type=float,
        default=0,
        help='Minimum required coverage percentage (0-100)'
    )
    
    args = parser.parse_args()
    
    # Check if source directory exists
    if not os.path.exists(args.source_dir):
        print(f"Error: Source directory '{args.source_dir}' not found", file=sys.stderr)
        return 1
    
    # Run checker
    checker = DocstringChecker(args.source_dir)
    checker.check_all()
    
    # Print report
    if args.quiet and not checker.issues:
        total_items = (
            checker.stats['total_modules'] + 
            checker.stats['total_classes'] + 
            checker.stats['total_functions']
        )
        documented_items = (
            checker.stats['documented_modules'] + 
            checker.stats['documented_classes'] + 
            checker.stats['documented_functions']
        )
        overall_coverage = (documented_items / total_items * 100) if total_items > 0 else 100
        print(f"Overall docstring coverage: {overall_coverage:.1f}%")
        
        if overall_coverage < args.min_coverage:
            print(f"Error: Coverage {overall_coverage:.1f}% is below minimum {args.min_coverage}%")
            return 1
        return 0
    
    exit_code = checker.print_report()
    
    # Check minimum coverage
    if args.min_coverage > 0:
        total_items = (
            checker.stats['total_modules'] + 
            checker.stats['total_classes'] + 
            checker.stats['total_functions']
        )
        documented_items = (
            checker.stats['documented_modules'] + 
            checker.stats['documented_classes'] + 
            checker.stats['documented_functions']
        )
        overall_coverage = (documented_items / total_items * 100) if total_items > 0 else 100
        
        if overall_coverage < args.min_coverage:
            print(f"\nError: Coverage {overall_coverage:.1f}% is below minimum {args.min_coverage}%")
            return 1
    
    return exit_code


if __name__ == '__main__':
    sys.exit(main())
