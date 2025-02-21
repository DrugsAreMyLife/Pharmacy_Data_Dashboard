# Charge Accounts

This section covers the endpoints related to charge accounts in the DRX API.

## Look Up a Charge Account

Retrieve details for a specific charge account using its unique identifier.

### Endpoint

`GET /api/v2/charge-accounts/{account_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| account_id | string | Primary key of the charge account |

### Response

#### Success Response (200 OK)

```json
{
  "id": "chg_12345",
  "patient_id": "pat_67890",
  "account_number": "ACC123456",
  "status": "active",
  "balance": 150.00,
  "credit_limit": 500.00,
  "payment_terms": "NET30",
  "last_payment_date": "2025-01-15",
  "last_payment_amount": 75.00,
  "created_at": "2024-12-01T00:00:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

#### Error Responses

- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Charge account not found

### Notes

- All monetary values are in USD
- Timestamps are in ISO 8601 format
- Account status can be: "active", "suspended", "closed"
- URL requests expire after 30 days

## Get a List of Charge Accounts

Retrieve a list of charge accounts with optional filtering and pagination.

### Endpoint

`GET /api/v2/charge-accounts`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| patient_id | string | Filter accounts by patient ID |
| status | string | Filter by account status |
| limit | integer | Number of records to return (default: 20, max: 100) |
| offset | integer | Number of records to skip for pagination |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "chg_12345",
      "patient_id": "pat_67890",
      "account_number": "ACC123456",
      "status": "active",
      "balance": 150.00,
      "credit_limit": 500.00,
      "payment_terms": "NET30",
      "last_payment_date": "2025-01-15",
      "last_payment_amount": 75.00,
      "created_at": "2024-12-01T00:00:00Z",
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

- Results are sorted by account number in ascending order
- Empty or invalid filters are ignored
- All account details are included in each response item
- Pagination metadata is always included
- Maximum of 100 accounts can be retrieved per request
- Use pagination for large datasets
- URL requests expire after 30 days

## History and Audit Trail

- All changes to charge accounts are logged
- Historical data is preserved for audit purposes
- Account status changes are tracked with timestamps
- Payment history is maintained indefinitely

## Best Practices

1. Always verify account status before processing charges
2. Check credit limits before adding new charges
3. Monitor payment terms for overdue accounts
4. Use pagination when retrieving large lists
5. Implement proper error handling for all responses
6. Keep track of URL expiration dates