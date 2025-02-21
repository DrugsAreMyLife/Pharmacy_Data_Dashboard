# API Issue Resolution Plan

## Issue
Receiving a 401 Unauthorized error when making a GET request to the DRX API endpoint `https://demo.drxapp.com/external_api/v1/queue`.

## Authentication Requirements
1. **API Key Requirement**: Obtain an API key from the store and include it in the request header.
   - Format for `X-DRX-Key`:
     ```
     X-DRX-Key: your-api-key-here
     ```
   - Format for Authorization header:
     ```
     Authorization: Bearer your-api-key-here
     ```

2. **General Request Guidelines**:
   - Use SSL connection for all requests.
   - Responses are in JSON format.
   - Unauthorized requests will return a 401 error code.

## Plan to Fix the Issue
1. **Verify API Key**: Ensure the API key is correct and has not been revoked or expired.
2. **Check Authorization Header**: Confirm the Authorization header is formatted correctly.
3. **Test with a Known Good Key**: If possible, test with a different API key that is known to work.
4. **Review API Documentation**: Ensure the endpoint is correctly defined and accessible.
5. **Implement Error Handling**: Add error handling for 401 errors in the code.
6. **Testing**: Retest the API request after making changes.

## Next Steps
- Follow the plan outlined above to resolve the issue.