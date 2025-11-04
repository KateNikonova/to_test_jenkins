import pytest
import time
import allure


@allure.epic("Company API")
@allure.feature("Company Management")
@allure.story("Get Company List")
@allure.title("Test getting list of companies")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_company_list(api_client):
    """Test getting list of companies"""
    response = api_client.get_company_list()
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    if data:
        company = data[0]
        assert 'name' in company
        assert 'description' in company
        assert 'is_active' in company


@allure.epic("Company API")
@allure.feature("Company Management")
@allure.story("Get Company List")
@allure.title("Test response structure for company list")
@allure.severity(allure.severity_level.NORMAL)
def test_get_company_list_structure(api_client):
    """Test response structure for company list"""
    response = api_client.get_company_list()
    assert response.status_code == 200

    companies = response.json()
    for company in companies:
        assert isinstance(company.get('name'), str)
        assert len(company['name']) > 0
        assert isinstance(company.get('is_active'), bool)


@allure.epic("Company API")
@allure.feature("API Connectivity")
@allure.story("Connectivity")
@allure.title("Test basic API connectivity")
@allure.severity(allure.severity_level.BLOCKER)
def test_api_connectivity(api_client):
    """Test basic API connectivity"""
    response = api_client.get_company_list()
    assert response.status_code in [200, 401, 403]


@allure.epic("Company API")
@allure.feature("Performance")
@allure.story("Response Time")
@allure.title("Test API response time")
@allure.severity(allure.severity_level.MINOR)
def test_response_time(api_client):
    """Test API response time"""
    start_time = time.time()
    response = api_client.get_company_list()
    end_time = time.time()

    response_time = end_time - start_time
    assert response_time < 5
    assert response.status_code in [200, 401, 403]
