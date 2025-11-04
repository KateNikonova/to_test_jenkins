import requests
import os
from dotenv import load_dotenv

load_dotenv()


class CompanyAPIClient:
    def __init__(self):
        self.base_url = os.getenv('API_BASE_URL', 'http://5.101.50.27:8000')
        self.token = os.getenv('API_TOKEN', '')
        self.headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {self.token}' if self.token else ''
        }

    def get_company_list(self):
        """Get list of all companies"""
        response = requests.get(f'{self.base_url}/company/list', headers=self.headers)
        return response

    def get_company_by_id(self, company_id):
        """Get company by ID"""
        response = requests.get(f'{self.base_url}/company/{company_id}', headers=self.headers)
        return response

    def create_company(self, name, description=""):
        """Create new company"""
        data = {
            "name": name,
            "description": description
        }
        response = requests.post(
            f'{self.base_url}/company/create',
            json=data,
            headers=self.headers
        )
        return response