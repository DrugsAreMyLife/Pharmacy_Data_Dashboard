# Shipping

This section covers the endpoints related to managing shipping operations in the DRX API.

## Get a List of Past Shipments

Retrieve a list of past shipments, sorted by creation date in descending order.

### Endpoint

`GET /api/v2/shipments`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| patient_id | string | Filter shipments by patient |
| limit | integer | Records to return |
| offset | integer | Offset for pagination |
| status | string | Filter by status |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "shp_12345",
      "tracking_number": "1Z999999999999999",
      "carrier": "ups",
      "service": "ground",
      "status": "delivered",
      "created_at": "2025-02-19T08:50:00Z",
      "shipped_at": "2025-02-19T10:30:00Z",
      "delivered_at": "2025-02-21T14:20:00Z",
      "recipient": {
        "name": "John Doe",
        "address": {
          "street": "123 Main St",
          "city": "Austin",
          "state": "TX",
          "zip": "78701"
        }
      },
      "package": {
        "weight_pounds": 2.5,
        "dimensions": {
          "length": 12,
          "width": 8,
          "height": 6
        },
        "signature_required": true
      },
      "cost": {
        "shipping": 12.50,
        "insurance": 1.50,
        "total": 14.00
      }
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

## Get Shipping Rates

Get available shipping rates for a package.

### Endpoint

`POST /api/v2/shipping/rates`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| patient_id | string | Optional patient ID |
| address_id | string | Optional address ID (must be associated with patient) |

### Request Body

1. If address_id not provided:
   ```json
   {
     "address": {
       "street": "123 Main St",
       "line_two": "Apt 4B",
       "city": "Austin",
       "state": "TX",
       "zip_code": "78701"
     },
     "name": "John Doe",
     "package_weight_pounds": 2.5,
     "signature_required": true,
     "carrier": "ups"
   }
   ```

2. Package Information:
   - At least one required:
     * package_weight_pounds
     * package_weight_ounces
   - Optional:
     * signature_required (boolean)
     * carrier (fedex, ups, usps)

### Response

#### Success Response (200 OK)

```json
{
  "rates": [
    {
      "carrier": "ups",
      "service": "ground",
      "rate_id": "rate_12345",
      "delivery_date": "2025-02-21",
      "guaranteed": true,
      "price": 12.50,
      "tracking_available": true
    },
    {
      "carrier": "ups",
      "service": "2day",
      "rate_id": "rate_12346",
      "delivery_date": "2025-02-20",
      "guaranteed": true,
      "price": 25.00,
      "tracking_available": true
    }
  ]
}
```

## Generate Label

Generate a shipping label using a selected shipping rate.

### Endpoint

`POST /api/v2/shipping/labels`

### Required Fields

| Field | Definition |
|-------|------------|
| rate_id | Rate ID from Get Shipping Rates response |

### Optional Fields

| Field | Definition |
|-------|------------|
| signature_required | Require signature on delivery |
| pos_event_id | Link to Point of Sale event |
| packing_list_id | Link to packing list |
| patient_id | Link shipment with patient |

### Response

#### Success Response (200 OK)

```json
{
  "label": {
    "id": "lbl_12345",
    "tracking_number": "1Z999999999999999",
    "carrier": "ups",
    "service": "ground",
    "url": "https://example.com/labels/lbl_12345.pdf",
    "expires_at": "2025-02-20T08:50:00Z"
  },
  "tracking": {
    "url": "https://example.com/track/1Z999999999999999",
    "updates_available": true
  }
}
```

## Best Practices

1. Rate Management
   - Compare carrier rates
   - Check delivery times
   - Verify service availability
   - Monitor price changes

2. Label Generation
   - Validate addresses
   - Check package details
   - Monitor label expiration
   - Handle printing errors

3. Shipment Tracking
   - Monitor shipment status
   - Handle delivery issues
   - Track signature capture
   - Process returns

4. System Integration
   - Connect to carriers
   - Update order status
   - Sync tracking data
   - Handle notifications

### Additional Information

- URL requests expire after 30 days
- All shipments logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported
- Integration with:
  * Carrier APIs
  * Order system
  * Patient portal
  * Notification system