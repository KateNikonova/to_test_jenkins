import pytest
from utils.api_client import CompanyAPIClient

@pytest.fixture
def api_client():
    return CompanyAPIClient()

@pytest.fixture
def sample_company_data():
    return {
        "name": "Test Company Python",
        "description": "Test company created by Python tests"
    }
