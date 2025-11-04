# API Tests for Jenkins Demo

This project contains Python API tests for the X-CLIENTS API.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and configure your API settings
3. Run tests: `python run_tests.py`

## Jenkins Pipeline
The project includes a Jenkinsfile for CI/CD pipeline automation.

## Test Structure
- `tests/test_company_api.py` - API tests for company endpoints
- `utils/api_client.py` - API client class
- `run_tests.py` - Test runner with HTML reports