import pytest
import sys
import os
import shutil

if __name__ == "__main__":
    # Добавляем текущую директорию в Python path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    # Очищаем предыдущие результаты Allure
    allure_results_dir = "allure-results"
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)

    # Запускаем тесты с Allure
    result_code = pytest.main([
        "tests/",
        "-v",
        "--alluredir=allure-results",
        "--html=test-report.html",
        "--self-contained-html",
        "--junit-xml=test-results.xml"
    ])

    sys.exit(result_code)
