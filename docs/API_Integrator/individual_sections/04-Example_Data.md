# Example Data

## Overview

This section provides example data structures and responses that you'll encounter when using the DRX API. These examples help illustrate the expected format and content of various API objects.

## Address Object

```json
{
  "id": "addr_12345",
  "street_1": "123 Main St",
  "street_2": "Suite 100",
  "city": "Austin",
  "state": "TX",
  "postal_code": "78701",
  "country": "US",
  "type": "billing",
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

## User Object

```json
{
  "id": "usr_67890",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "phone": "+1-555-123-4567",
  "status": "active",
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

## Order Object

```json
{
  "id": "ord_24680",
  "customer_id": "usr_67890",
  "status": "processing",
  "items": [
    {
      "id": "item_111",
      "product_id": "prod_555",
      "quantity": 2,
      "price": 29.99
    }
  ],
  "shipping_address": {
    "id": "addr_12345",
    "street_1": "123 Main St",
    "street_2": "Suite 100",
    "city": "Austin",
    "state": "TX",
    "postal_code": "78701",
    "country": "US"
  },
  "total": 59.98,
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

## Error Response

```json
{
  "error": {
    "code": "validation_error",
    "message": "Invalid request parameters",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

## Pagination Response

```json
{
  "data": [...],
  "pagination": {
    "total_items": 100,
    "total_pages": 5,
    "current_page": 1,
    "per_page": 20,
    "next_page": 2,
    "prev_page": null
  }
}
```

## Common Fields

Most objects in the API include these standard fields:

- id: Unique identifier with appropriate prefix
- created_at: UTC timestamp of creation
- updated_at: UTC timestamp of last update
- status: Current state of the object (when applicable)

## Data Types

| Type | Format | Example |
|------|---------|---------|
| ID | string with prefix | "usr_12345" |
| DateTime | ISO 8601 UTC | "2025-02-19T08:50:00Z" |
| Currency | decimal | 29.99 |
| Phone | E.164 format | "+1-555-123-4567" |
| Country | ISO 3166-1 alpha-2 | "US" |
| State | Standard code | "TX" |

## Best Practices

1. Always validate data against these example structures
2. Handle optional fields appropriately
3. Use proper data types for each field
4. Follow the format conventions for IDs and timestamps
5. Implement proper error handling based on error response format
6. Use pagination parameters when available