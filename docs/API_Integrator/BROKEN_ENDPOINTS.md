# Broken API Endpoints Analysis

## Authentication Issues (401)
These endpoints require proper authentication but are returning 401 errors:

1. **Charge Account Endpoints**
   - `/charge-account/{charge_account_id}`
   - `/charge-accounts`
   - Possible Solutions:
     * Verify API key permissions include charge account access
     * Check if additional headers are required
     * Confirm if these endpoints require special authorization

## Not Found Errors (404)
These endpoints appear to have been moved or renamed:

1. **Past Shipments**
   - Current Path: `/shipments`
   - Status: 404
   - Possible Solutions:
     * Check if moved to `/shipping/shipments`
     * Verify if consolidated under deliveries endpoint
     * Confirm if feature has been deprecated

2. **Sale Events**
   - Current Path: `/pos/events`
   - Status: 404
   - Possible Solutions:
     * Check if moved to `/sales/events`
     * Verify if renamed to `/transactions`
     * Confirm current POS integration endpoints

3. **SureScripts**
   - Current Path: `/surescripts`
   - Status: 404
   - Possible Solutions:
     * Check if moved to `/e-prescriptions`
     * Verify if consolidated under prescriptions endpoint
     * Confirm current e-prescription integration paths

## Internal Server Error (500)
These endpoints are experiencing server-side issues:

1. **Inventory History**
   - Path: `/inventory/history/{item_id}`
   - Status: 500
   - Possible Solutions:
     * Check if item_id format is correct
     * Verify date range parameters
     * Review server logs for specific error
     * Test with different item IDs

## Next Steps

1. **Authentication Issues**
   - Request updated API key with correct permissions
   - Review authentication documentation
   - Test with different authentication methods

2. **404 Endpoints**
   - Request updated API documentation
   - Check for endpoint migration notices
   - Test alternative endpoint paths

3. **500 Error**
   - Request server logs for error details
   - Test with different parameter combinations
   - Check for any rate limiting issues

## Testing Notes
- All tests performed against demo environment
- Using API key: DRX22770ca6e378423fa85c62f8675c5bd7
- Tests run on: 2025-02-19
- Full test results saved in JSON format with timestamp

## Related Documentation
- [DRX_API_ENDPOINTS.md](./DRX_API_ENDPOINTS.md) - Working endpoints reference
- [api_test_results.md](./api_test_results.md) - Full test results