# Addresses

This section covers all address-related endpoints in the DRX API, including looking up, listing, editing, and adding addresses.

## Look Up an Address

Retrieve details for a specific address using its unique identifier.

### Endpoint

`GET /api/v2/addresses/{address_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| address_id | string | Unique identifier of the address to retrieve |

### Response

#### Success Response (200 OK)

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

#### Error Responses

- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Address ID does not exist

### Notes

- All address fields are included in the response
- Historical address data is preserved and accessible
- Use this endpoint when you need complete details for a specific address
- The address ID must be a valid identifier previously returned by the API
- Response includes both the created_at and updated_at timestamps
- Deleted addresses will return a 404 Not Found response

## Get a List of Addresses

Retrieve a list of all addresses in the system. This endpoint supports pagination and filtering to manage large sets of address records.

### Endpoint

`GET /api/v2/addresses`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| page | integer | Page number for pagination (default: 1) |
| per_page | integer | Number of items per page (default: 20, max: 100) |
| type | string | Filter by address type (e.g., "billing", "shipping") |
| city | string | Filter by city name |
| state | string | Filter by state/province code |
| country | string | Filter by country code |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
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
  ],
  "pagination": {
    "total_items": 50,
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

- Results are sorted by creation date in descending order
- Empty or invalid filters are ignored
- All address fields are included in the response
- Pagination metadata is always included
- Maximum of 100 addresses can be retrieved per request
- Use pagination for large datasets

## Edit an Address

Update an existing address in the system.

### Endpoint

`PATCH /api/v2/addresses/{address_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| address_id | string | Unique identifier of the address to update |

### Request Body

| Field | Type | Description |
|-------|------|-------------|
| street_1 | string | Primary street address |
| street_2 | string | Secondary address info (optional) |
| city | string | City name |
| state | string | State/province code |
| postal_code | string | ZIP/Postal code |
| country | string | Country code (ISO 3166-1 alpha-2) |
| type | string | Address type (e.g., "billing", "shipping") |

### Example Request

```json
{
  "street_1": "456 Oak Ave",
  "street_2": "Unit 200",
  "city": "Austin",
  "state": "TX",
  "postal_code": "78702",
  "country": "US",
  "type": "shipping"
}
```

### Response

#### Success Response (200 OK)

```json
{
  "id": "addr_12345",
  "street_1": "456 Oak Ave",
  "street_2": "Unit 200",
  "city": "Austin",
  "state": "TX",
  "postal_code": "78702",
  "country": "US",
  "type": "shipping",
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:54:00Z"
}
```

#### Error Responses

- 400 Bad Request: Invalid address data
- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Address ID does not exist
- 422 Unprocessable Entity: Missing required fields

### Notes

- All fields except street_2 are required
- Country codes must be valid ISO 3166-1 alpha-2 codes
- State codes must be valid for the specified country
- Postal code format is validated based on country
- Address type must be one of the predefined values
- The created_at timestamp remains unchanged
- The updated_at timestamp is automatically updated
- Historical address data is preserved for audit purposes

## Add an Address

Add a new address to the system.

### Endpoint

`POST /api/v2/addresses`

### Request Body

| Field | Type | Description |
|-------|------|-------------|
| street_1 | string | Primary street address |
| street_2 | string | Secondary address info (optional) |
| city | string | City name |
| state | string | State/province code |
| postal_code | string | ZIP/Postal code |
| country | string | Country code (ISO 3166-1 alpha-2) |
| type | string | Address type (e.g., "billing", "shipping") |

### Example Request

```json
{
  "street_1": "123 Main St",
  "street_2": "Suite 100",
  "city": "Austin",
  "state": "TX",
  "postal_code": "78701",
  "country": "US",
  "type": "billing"
}
```

### Response

#### Success Response (201 Created)

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

#### Error Responses

- 400 Bad Request: Invalid address data
- 401 Unauthorized: Invalid or missing API key
- 422 Unprocessable Entity: Missing required fields

### Notes

- All fields except street_2 are required
- Country codes must be valid ISO 3166-1 alpha-2 codes
- State codes must be valid for the specified country
- Postal code format is validated based on country
- Address type must be one of the predefined values