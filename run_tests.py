"""
Test runner script for Jenkins
"""
import pytest
import sys
import os


def main():
    """Run tests with pytest"""
    # Add current directory to Python path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    # Run tests
    result = pytest.main([
        "tests/",
        "-v",
        "--html=test-report.html",
        "--self-contained-html",
        "--junit-xml=test-results.xml"
    ])

    # Exit with proper code
    sys.exit(result)


if __name__ == "__main__":
    main()
