#!/bin/bash
# Documentation build helper script for richardutils
# This script provides convenient options for building and serving documentation

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Script directory and project root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DOCS_DIR="$PROJECT_ROOT/docs"
BUILD_DIR="$DOCS_DIR/_build/html"

# Function to print colored messages
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if dependencies are installed
check_dependencies() {
    print_info "Checking dependencies..."
    
    if ! command -v python &> /dev/null; then
        print_error "Python is not installed or not in PATH"
        exit 1
    fi
    
    # Check if sphinx is installed
    if ! python -c "import sphinx" 2>/dev/null; then
        print_error "Sphinx is not installed. Run: pip install -e .[dev]"
        exit 1
    fi
    
    print_info "Dependencies OK"
}

# Function to clean build directory
clean_build() {
    print_info "Cleaning build directory..."
    if [ -d "$BUILD_DIR" ]; then
        rm -rf "$BUILD_DIR"
        print_info "Build directory cleaned"
    else
        print_info "Build directory does not exist, nothing to clean"
    fi
}

# Function to build documentation
build_docs() {
    local clean_first=$1
    
    if [ "$clean_first" = "true" ]; then
        clean_build
    fi
    
    print_info "Building documentation..."
    cd "$DOCS_DIR"
    
    if make html 2>&1 | tee /tmp/sphinx-build.log; then
        print_info "Documentation built successfully!"
        print_info "Output: $BUILD_DIR/index.html"
        return 0
    else
        print_error "Documentation build failed. Check output above."
        return 1
    fi
}

# Function to serve documentation
serve_docs() {
    local port=$1
    
    if [ ! -d "$BUILD_DIR" ]; then
        print_error "Build directory not found. Build the docs first."
        exit 1
    fi
    
    print_info "Starting documentation server on http://localhost:$port"
    print_info "Press Ctrl+C to stop the server"
    cd "$BUILD_DIR"
    python -m http.server "$port"
}

# Function to open documentation in browser
open_docs() {
    if [ ! -f "$BUILD_DIR/index.html" ]; then
        print_error "Documentation not found. Build it first."
        exit 1
    fi
    
    print_info "Opening documentation in browser..."
    
    # Try different commands based on OS
    if command -v xdg-open &> /dev/null; then
        xdg-open "$BUILD_DIR/index.html"
    elif command -v open &> /dev/null; then
        open "$BUILD_DIR/index.html"
    elif command -v start &> /dev/null; then
        start "$BUILD_DIR/index.html"
    else
        print_warning "Could not open browser automatically."
        print_info "Open this file manually: $BUILD_DIR/index.html"
    fi
}

# Function to check for warnings
check_warnings() {
    print_info "Checking for build warnings..."
    
    if [ ! -f /tmp/sphinx-build.log ]; then
        print_warning "No build log found. Run a build first."
        return 1
    fi
    
    local warning_count=$(grep -c "WARNING:" /tmp/sphinx-build.log || true)
    local error_count=$(grep -c "ERROR:" /tmp/sphinx-build.log || true)
    
    echo ""
    print_info "Build Summary:"
    echo "  Warnings: $warning_count"
    echo "  Errors: $error_count"
    echo ""
    
    if [ $error_count -gt 0 ]; then
        print_error "Errors found in build:"
        grep "ERROR:" /tmp/sphinx-build.log || true
    fi
    
    if [ $warning_count -gt 0 ]; then
        print_warning "Warnings found in build:"
        grep "WARNING:" /tmp/sphinx-build.log | head -20 || true
        if [ $warning_count -gt 20 ]; then
            echo "  ... and $(($warning_count - 20)) more warnings"
        fi
    fi
    
    if [ $warning_count -eq 0 ] && [ $error_count -eq 0 ]; then
        print_info "No warnings or errors! ✓"
    fi
}

# Function to show help
show_help() {
    cat << EOF
Documentation Build Helper for richardutils

Usage: $0 [COMMAND] [OPTIONS]

Commands:
    build           Build the documentation (default)
    clean           Clean the build directory
    rebuild         Clean and rebuild documentation
    serve [PORT]    Serve documentation on localhost (default port: 8000)
    open            Open documentation in default browser
    check           Build and check for warnings/errors
    help            Show this help message

Examples:
    $0 build              # Build documentation
    $0 rebuild            # Clean build from scratch
    $0 serve              # Serve on http://localhost:8000
    $0 serve 8080         # Serve on http://localhost:8080
    $0 check              # Build and check for issues
    $0 open               # Open docs in browser

Options:
    -h, --help      Show this help message

Environment Variables:
    DOCS_PORT       Default port for serving (default: 8000)

EOF
}

# Main script logic
main() {
    local command="${1:-build}"
    
    case "$command" in
        build)
            check_dependencies
            build_docs false
            ;;
        clean)
            clean_build
            ;;
        rebuild)
            check_dependencies
            build_docs true
            ;;
        serve)
            local port="${2:-${DOCS_PORT:-8000}}"
            serve_docs "$port"
            ;;
        open)
            open_docs
            ;;
        check)
            check_dependencies
            build_docs true
            check_warnings
            ;;
        help|-h|--help)
            show_help
            ;;
        *)
            print_error "Unknown command: $command"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

# Run main function
main "$@"
