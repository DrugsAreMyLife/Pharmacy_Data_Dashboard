# DRX API Tester

## Overview
Tool for testing DRX API endpoints and verifying functionality across API versions (V1 and V2).

## Test Results (2025-02-19)

### Summary
- Total Endpoints Tested: 200
- Successful: 127 (63.5%)
- Failed: 73 (36.5%)

### Working Endpoints
Successfully tested endpoints with 200 status code:
- Get All Inventory
- Get Store Settings
- List Addresses (with various filters)
- List Allergies (with various filters)
- List Claims
- List Deliveries
- List Delivery Routes
- List Doctors (with search functionality)
- List Items
- List Patients (with various filters)
- List Phone Numbers
- List Prescriptions (except "Rejected" status)
- List Tasks
- List Webhooks
- Search Provider Catalog

### Failed Endpoints

#### 404 Not Found
These endpoints may have been moved or renamed in V2:
- Get Item Inventory History
- List Past Shipments
- List Sale Events
- List SureScripts
- List Competing Pharmacies
- List Fill Tags
- List Packing Lists
- List Prescription Fills

#### 401 Unauthorized
These endpoints may require additional permissions:
- Charge Account endpoints
- List Charge Accounts

#### 500 Internal Server Error
These endpoints need backend investigation:
- Inventory History endpoint
- List Prescriptions with "Rejected" status

## API Version Differences

### V1 API
- Base URL: https://[store-slug].drxapp.com/external_api/v1/
- Authentication: X-DRX-Key header
- Status: Currently in use

### V2 API
- Base URL: https://api.drx.com/v2/ (Production)
- Sandbox URL: https://sandbox-api.drx.com/v2/ (Testing)
- Authentication: Bearer token
- Status: Testing blocked (requires developer account)

## Next Steps

### 1. Developer Account Setup
- Register for DRX developer account
- Generate V2 API credentials
- Configure sandbox environment access
- Document credential management process

### 2. V2 API Testing
- Update test scripts for V2 authentication
- Verify endpoint mappings between versions
- Document breaking changes
- Create compatibility test suite

### 3. Permission Verification
- Audit current API key permissions
- Document required permissions per endpoint
- Request permission updates if needed
- Implement permission testing

### 4. Error Investigation
- Debug 500 errors on Inventory History
- Verify correct paths for 404 endpoints
- Document deprecated endpoints
- Create error handling test cases

## Usage

### Running Tests
```bash
python Broken_API_Endpoint_Tests_to_Live_CCP_PMS.py
```

### Test Output
Results are saved to JSON files with timestamp:
```
broken_endpoints_test_results_[TIMESTAMP].json
```

### Configuration
Update API keys and base URLs in the script:
```python
PRODUCTION_API_KEY = "your-api-key"
PRODUCTION_BASE_URL_V1 = "https://[store-slug].drxapp.com/external_api/v1"
PRODUCTION_BASE_URL_V2 = "https://sandbox-api.drx.com/v2"
```

## Contributing
1. Document any new endpoint tests
2. Add error handling test cases
3. Update version compatibility tests
4. Maintain test result documentation

## Notes
- URL requests expire after 30 days
- Rate limiting applies to API requests
- Some endpoints require specific permissions
- V2 API testing requires developer account