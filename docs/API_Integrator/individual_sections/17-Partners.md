# Partners

This section covers the endpoints related to partner integrations and data exports in the DRX API.

## Commands

The partners API generates specific responses tailored to particular vendors. While accessible to anyone with an appropriate API key, this endpoint was designed for specific integrations with frozen output formats.

### Endpoint

`GET /api/v2/partners/{partner_name}`

Note: The partner_name in the path can be any name used to help identify the source of the request.

### Available Commands

| Command | Description |
|---------|-------------|
| startFeed | Start the daily Datarithm export. **IMPORTANT**: Takes effect after next server restart (weekly or sooner) |
| endFeed | End the daily Datarithm export. **IMPORTANT**: Takes effect after next server restart |
| checkTaskStatus | Check progress of a recently started export task. Requires taskId parameter |
| export | Start new data export (default: last two days). Optional startDate parameter |
| dataDump | Generate signed download link for database dump tables (conversion data) |

### Example Requests

#### Check Task Status
```bash
curl --request GET \
     --url 'https://slug.drxapp.com/external_api/v1/partners/infowerks?command=checkTaskStatus&taskId=82919a9b-825e-46c1-938a-a5a4e69f1675' \
     --header 'X-DRX-Key: DRX75e1XXXXXXXXXXXXXXXXXXXXXXXXXXXX' \
     --header 'accept: application/json'
```

#### Response
```json
{
    "success": true,
    "response": {
        "state": "PENDING"
    }
}
```

## Data Dump Process

### Step 1: Contact DRX Support
- Email support@drxpharmacytech.com
- Request data export form
- Form must be completed and filed for customer

### Step 2: Email Setup
- Provide email address for export link
- DRX support will activate email
- Validate data export form

### Step 3: API Request

```bash
curl --request GET \
     --url 'https://slug.drxapp.com/external_api/v1/partners/infowerks?command=dataDump' \
     --header 'X-DRX-Key: DRX7XXXXXXXXXXXXXXXXXXXXXX' \
     --header 'accept: application/json'
```

#### Response
```json
{
    "success": true,
    "message": "Data export started, this can take up to 1 hour to complete.",
    "task_id": "82919a9b-825e-46c1-938a-a5a4e69f1675"
}
```

### Important Notes

1. Resource Management
   - Use your own API key
   - Ensure slug matches target store
   - Export can take up to one hour
   - Do not start multiple pulls simultaneously
   - API keys may be suspended for overuse

2. Best Practices
   - Perform dumps during off-hours
   - Monitor task status
   - Handle large datasets appropriately
   - Implement error handling
   - Log all operations

3. Data Security
   - Secure download links
   - Protect exported data
   - Monitor access patterns
   - Delete exports after use
   - Follow data retention policies

4. Performance Considerations
   - Rate limit requests
   - Handle timeouts gracefully
   - Process data in chunks
   - Monitor system resources
   - Schedule during off-peak hours

### Export File Format

The data dump includes the following information:

1. Patient Data
   - Demographics
   - Contact information
   - Insurance details
   - Medical history

2. Prescription Data
   - Active prescriptions
   - Fill history
   - Provider information
   - Insurance claims

3. Inventory Data
   - Item details
   - Stock levels
   - Pricing information
   - Supplier data

4. Transaction History
   - Sales records
   - Payment information
   - Adjustments
   - Returns

### Additional Information

- Files are compressed
- Data is encrypted
- 30-day link expiration
- Audit logs maintained
- Support for incremental exports