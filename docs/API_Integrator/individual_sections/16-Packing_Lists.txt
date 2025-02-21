# Packing Lists

This section covers the endpoints related to managing packing lists in the DRX API.

## Get a List of Packing Lists

Retrieve a list of packing lists with pagination support.

### Endpoint

`GET /api/v2/packing-lists`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Maximum number of records to return (max: 100) |
| offset | integer | Number of records to skip for pagination |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "pkl_12345",
      "status": "active",
      "created_by": "john.doe",
      "created_at": "2025-02-19T08:50:00Z",
      "completed_at": null,
      "fill_count": 25,
      "total_items": 150,
      "delivery_route": "NORTH_AUSTIN",
      "delivery_date": "2025-02-20",
      "notes": "Priority deliveries",
      "metadata": {
        "total_value": 1250.00,
        "total_weight": 2.5
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

### Notes

- Results are sorted by creation date in descending order
- All monetary values are in store's local currency
- Weight is in kilograms

## Get All Prescription Fills on Packing List

Retrieve all prescription fills associated with a specific packing list.

### Endpoint

`GET /api/v2/packing-lists/{packing_list_id}/fills`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| packing_list_id | string | Primary key of the packing list |

### Response

#### Success Response (200 OK)

```json
{
  "packing_list": {
    "id": "pkl_12345",
    "status": "active",
    "created_at": "2025-02-19T08:50:00Z"
  },
  "fills": [
    {
      "id": "fill_67890",
      "prescription_id": "rx_11111",
      "patient": {
        "id": "pat_22222",
        "name": "John Doe",
        "address": "123 Main St, Austin, TX 78701"
      },
      "medication": {
        "name": "Example Medication 10mg Tablet",
        "quantity": 30,
        "days_supply": 30
      },
      "status": "ready",
      "bin_location": "A-15",
      "packed": false,
      "verified": false,
      "notes": "Refrigerate upon delivery"
    }
  ],
  "metadata": {
    "total_fills": 25,
    "completed_fills": 15,
    "verified_fills": 20
  }
}
```

### Notes

- Fills are sorted by bin location
- Status updates are real-time
- Verification status is tracked
- Special handling notes included

## Best Practices

1. Packing List Management
   - Create lists by delivery route
   - Maintain reasonable list sizes
   - Monitor completion status
   - Track verification progress

2. Fill Organization
   - Group by delivery area
   - Sort by bin location
   - Note special handling
   - Verify counts regularly

3. Quality Control
   - Double-check medications
   - Verify patient information
   - Check special instructions
   - Document all verifications

4. Delivery Planning
   - Group by geographic area
   - Consider delivery timing
   - Note access restrictions
   - Plan efficient routes

### Additional Information

- URL requests expire after 30 days
- All updates are logged
- Audit trail maintained
- Real-time status updates
- Integration with delivery system