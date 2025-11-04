import pytest
import time


class TestCompanyAPI:

    def test_get_company_list(self, api_client):
        """Test getting list of companies"""
        response = api_client.get_company_list()

        assert response.status_code == 200
        data = response.json()

        # Basic structure validation
        assert isinstance(data, list)
        if data:  # If there are companies
            company = data[0]
            assert 'name' in company
            assert 'description' in company
            assert 'is_active' in company

    def test_get_company_list_structure(self, api_client):
        """Test response structure for company list"""
        response = api_client.get_company_list()

        assert response.status_code == 200
        companies = response.json()

        for company in companies:
            # Required fields
            assert isinstance(company.get('name'), str)
            assert len(company['name']) > 0
            assert isinstance(company.get('is_active'), bool)

            # Optional fields validation
            description = company.get('description')
            if description is not None:
                assert isinstance(description, str)

    def test_api_connectivity(self, api_client):
        """Test basic API connectivity"""
        response = api_client.get_company_list()

        # Should get either 200 (success) or 401/403 (auth required)
        assert response.status_code in [200, 401, 403]

        if response.status_code == 200:
            # If we get data, validate structure
            companies = response.json()
            assert isinstance(companies, list)

    def test_response_time(self, api_client):
        """Test API response time"""
        start_time = time.time()
        response = api_client.get_company_list()
        end_time = time.time()

        response_time = end_time - start_time
        assert response_time < 5  # Should respond within 5 seconds
        assert response.status_code in [200, 401, 403]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
