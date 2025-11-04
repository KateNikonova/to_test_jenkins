#!/usr/bin/env python3
import pytest
import sys
import os

if __name__ == "__main__":
    # Добавляем текущую директорию в Python path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    # Запускаем тесты
    result_code = pytest.main([
        "tests/",
        "-v",
        "--html=test-report.html",
        "--self-contained-html",
        "--junit-xml=test-results.xml"
    ])
    
    sys.exit(result_code)
