# Claims

This section covers the endpoints related to prescription claims in the DRX API.

## Look Up a Claim

Retrieve detailed information about a specific claim using its unique identifier.

### Endpoint

`GET /api/v2/claims/{claim_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | string | Primary key of the claim |

### Response

#### Success Response (200 OK)

```json
{
  "id": "clm_12345",
  "prescription_id": "rx_67890",
  "patient_id": "pat_11111",
  "status": "paid",
  "claim_date": "2025-02-19T08:50:00Z",
  "submitted_amount": 150.00,
  "approved_amount": 125.00,
  "copay": 25.00,
  "insurance_paid": 100.00,
  "rejection_codes": [],
  "third_party": {
    "id": "ins_22222",
    "name": "Example Insurance",
    "bin": "123456",
    "pcn": "ABCD",
    "group": "GROUP123"
  },
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

#### Error Responses

- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Claim not found

### Notes

- All monetary values are in USD
- Timestamps are in ISO 8601 format
- URL requests expire after 30 days
- Claim status can be: "pending", "paid", "rejected", "reversed"

## Get a List of Claims

Retrieve a list of claims with optional filtering and pagination.

### Endpoint

`GET /api/v2/claims`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| patient_id | string | Filter claims by patient ID |
| prescription_id | string | Filter claims by prescription ID |
| status | string | Filter by claim status |
| before_date | string | Find claims before this date time (ISO 8601) |
| after_date | string | Find claims after this date time (ISO 8601) |
| limit | integer | Number of records to return (default: 20, max: 100) |
| offset | integer | Number of records to skip for pagination |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "clm_12345",
      "prescription_id": "rx_67890",
      "patient_id": "pat_11111",
      "status": "paid",
      "claim_date": "2025-02-19T08:50:00Z",
      "submitted_amount": 150.00,
      "approved_amount": 125.00,
      "copay": 25.00,
      "insurance_paid": 100.00,
      "rejection_codes": [],
      "third_party": {
        "id": "ins_22222",
        "name": "Example Insurance",
        "bin": "123456",
        "pcn": "ABCD",
        "group": "GROUP123"
      },
      "created_at": "2025-02-19T08:50:00Z",
      "updated_at": "2025-02-19T08:50:00Z"
    }
  ],
  "pagination": {
    "total_items": 45,
    "total_pages": 3,
    "current_page": 1,
    "per_page": 20,
    "next_page": 2,
    "prev_page": null
  }
}
```

#### Error Responses

- 401 Unauthorized: Invalid or missing API key
- 400 Bad Request: Invalid query parameters

### Notes

- Results are sorted by claim date in descending order
- Empty or invalid filters are ignored
- All claim details are included in each response item
- Pagination metadata is always included
- Maximum of 100 claims can be retrieved per request
- Use pagination for large datasets
- URL requests expire after 30 days

## Common Rejection Codes

| Code | Description |
|------|-------------|
| 70   | Product/Service Not Covered |
| 75   | Prior Authorization Required |
| 79   | Refill Too Soon |
| 80   | Drug-Drug Interaction |
| 88   | DUR Reject Error |

## Best Practices

1. Always check claim status before processing
2. Store rejection codes for troubleshooting
3. Implement proper error handling
4. Use date filters for targeted searches
5. Monitor claim reversals and resubmissions
6. Keep track of URL expiration dates

## Additional Information

- Claims cannot be modified once submitted
- Rejected claims may be resubmitted with corrections
- Paid claims may be reversed if necessary
- Historical claim data is preserved indefinitely
- All claim actions are logged for audit purposes