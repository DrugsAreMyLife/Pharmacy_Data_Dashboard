# Patient Match

This section covers the functionality for finding matching patient records in the DRX API.

## Find a Match

Search for matching patient records based on prescription and patient information.

### Endpoint

`POST /api/v2/patient-match`

### Important Requirements

- Rx number, first name, and last name fields must be populated to produce a match
- If there is not exactly one match, no patient data will be displayed
- Date of birth must be an ISO 8601 formatted string

### Request Body

| Field | Type | Description |
|-------|------|-------------|
| rx_number | string | Prescription number |
| first_name | string | Patient's first name |
| last_name | string | Patient's last name |
| date_of_birth | string | Patient's birth date (ISO 8601) |

### Example Request

```json
{
  "rx_number": "123456",
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1980-01-15"
}
```

### Response

#### Success Response (200 OK) - Exact Match Found

```json
{
  "match_found": true,
  "patient": {
    "id": "pat_12345",
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1980-01-15",
    "gender": "M",
    "status": "active",
    "address": {
      "street": "123 Main St",
      "city": "Austin",
      "state": "TX",
      "zip": "78701"
    },
    "phone_numbers": [
      {
        "type": "cell",
        "number": "5551234567"
      }
    ]
  },
  "prescription": {
    "rx_number": "123456",
    "status": "active",
    "last_fill_date": "2025-02-01"
  }
}
```

#### No Match Response (200 OK)

```json
{
  "match_found": false,
  "message": "No exact match found"
}
```

#### Multiple Matches Response (200 OK)

```json
{
  "match_found": false,
  "message": "Multiple potential matches found"
}
```

#### Error Responses

- 400 Bad Request: Missing required fields
- 401 Unauthorized: Invalid or missing API key
- 422 Unprocessable Entity: Invalid data format

### Matching Algorithm

The matching process follows these steps:

1. Required Field Validation
   - Checks for presence of all required fields
   - Validates data formats
   - Confirms prescription exists

2. Name Matching
   - Exact match on last name
   - Exact match on first name
   - Case-insensitive comparison
   - No partial matches allowed

3. Date of Birth Verification
   - Exact match required
   - Validates format
   - Checks reasonable date range

4. Prescription Verification
   - Confirms Rx belongs to matched patient
   - Verifies Rx status
   - Checks fill history

### Best Practices

1. Data Preparation
   - Normalize name formats
   - Validate date formats
   - Clean input data
   - Remove extra whitespace

2. Error Handling
   - Handle all response types
   - Provide clear user feedback
   - Log failed matches
   - Monitor match rates

3. Security Considerations
   - Validate input data
   - Rate limit requests
   - Log access attempts
   - Protect sensitive data

4. Performance Optimization
   - Cache common searches
   - Index key fields
   - Monitor response times
   - Optimize query patterns

### Additional Information

- URL requests expire after 30 days
- All match attempts are logged
- Audit trail maintained
- Match criteria cannot be modified
- No fuzzy matching supported