# Deliveries

This section covers the endpoints related to managing deliveries and delivery routes in the DRX API.

## Get a List of Deliveries

Retrieve a list of deliveries with optional filtering and sorting.

### Endpoint

`GET /api/v2/deliveries`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| route | string | Filter deliveries by specific route |
| per_page | integer | Number of records per page (default: 20, max: 100) |
| page | integer | Page number for pagination |
| date | string | Filter deliveries due on specific date (ISO 8601) |
| external_id | string | Find deliveries with specific external_id |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "del_12345",
      "route": "NORTH_AUSTIN",
      "route_order": 5,
      "status": "pending",
      "delivery_on": "2025-02-19",
      "name": "John Doe",
      "address": "123 Main St",
      "city": "Austin",
      "state": "TX",
      "zip_code": "78701",
      "special_instructions": "Leave at front door",
      "recipient_phone": "5551234567",
      "external_id": "EXT123",
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

### Notes

- Default order is by route and then by route_order
- Route order represents most efficient round trip starting and ending at pharmacy
- Route order may be null for unassigned deliveries

## Get a List of Delivery Routes

Retrieve all available delivery routes.

### Endpoint

`GET /api/v2/delivery-routes`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Number of records to return |
| page | integer | Page number for pagination |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "rte_12345",
      "name": "NORTH_AUSTIN",
      "description": "North Austin delivery route",
      "active": true,
      "created_at": "2025-01-01T00:00:00Z",
      "updated_at": "2025-02-19T08:50:00Z"
    }
  ],
  "pagination": {
    "total_items": 10,
    "total_pages": 1,
    "current_page": 1,
    "per_page": 20,
    "next_page": null,
    "prev_page": null
  }
}
```

### Notes

- Routes are always sorted alphabetically in ascending order
- Inactive routes are included in results

## Look Up a Delivery

Retrieve details for a specific delivery.

### Endpoint

`GET /api/v2/deliveries/{delivery_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| delivery_id | string | Unique identifier of the delivery |

### Response

#### Success Response (200 OK)

```json
{
  "id": "del_12345",
  "route": "NORTH_AUSTIN",
  "route_order": 5,
  "status": "pending",
  "delivery_on": "2025-02-19",
  "name": "John Doe",
  "address": "123 Main St",
  "city": "Austin",
  "state": "TX",
  "zip_code": "78701",
  "special_instructions": "Leave at front door",
  "recipient_phone": "5551234567",
  "external_id": "EXT123",
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

## Edit a Delivery

Update an existing delivery's information.

### Endpoint

`PATCH /api/v2/deliveries/{delivery_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| delivery_id | string | Unique identifier of the delivery |

### Request Body

| Field | Definition |
|---|---|
| delivery_on | Date in ISO format |
| name | Delivery recipient name |
| address | Street address |
| city | City |
| state | State |
| zip_code | ZIP code |
| refused_at | Date/time of refusal (ISO format) |
| refused_by | Name of person who refused delivery |
| completed_at | Date/time of completion (ISO format) |
| special_instructions | Delivery instructions |
| recipient_phone | 10-digit phone number |
| external_id | External identifier |
| label_url | URL for delivery label |

### Example Request

```json
{
  "special_instructions": "Call upon arrival",
  "recipient_phone": "5551234567",
  "external_id": "EXT123"
}
```

### Response

#### Success Response (200 OK)

```json
{
  "id": "del_12345",
  "route": "NORTH_AUSTIN",
  "route_order": 5,
  "status": "pending",
  "delivery_on": "2025-02-19",
  "name": "John Doe",
  "address": "123 Main St",
  "city": "Austin",
  "state": "TX",
  "zip_code": "78701",
  "special_instructions": "Call upon arrival",
  "recipient_phone": "5551234567",
  "external_id": "EXT123",
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T09:00:00Z"
}
```

### Notes

- Phone numbers must be 10 digits without formatting
- Refused deliveries show red 'Refused' highlight in UI
- Completed deliveries show green 'Delivered' highlight
- External IDs can be used for third-party system integration
- Label URLs are displayed in the Delivery Queue

## Best Practices

1. Always validate addresses before creating deliveries
2. Use external_id for tracking in external systems
3. Keep special instructions clear and concise
4. Update delivery status promptly
5. Monitor refused deliveries for patterns
6. Maintain accurate recipient contact information

## Additional Information

- URL requests expire after 30 days
- All delivery updates are logged for audit purposes
- Route optimization is handled automatically
- Delivery history is preserved indefinitely