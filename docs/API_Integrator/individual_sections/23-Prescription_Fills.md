# Prescription Fills

This section covers the endpoints related to managing prescription fills in the DRX API.

## Get a List of Prescription Fills

Retrieve a list of prescription fills with optional filtering.

### Endpoint

`GET /api/v2/prescription-fills`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| before_date | string | Get fills sold before date (exclusive) |
| after_date | string | Get fills sold after date (exclusive) |
| fills_in_progress | boolean | Limit to fills in active workflow |
| status | string | Filter by specific fill status |
| patient_id | string | Filter by patient |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "fill_12345",
      "prescription_id": "rx_67890",
      "status": "ready",
      "fill_date": "2025-02-19",
      "quantity": 30,
      "days_supply": 30,
      "fill_number": 1,
      "refills_remaining": 2,
      "patient": {
        "id": "pat_11111",
        "name": "John Doe"
      },
      "medication": {
        "id": "med_22222",
        "name": "Example Medication 10mg Tablet",
        "ndc": "12345-6789-10"
      },
      "bin_location": "A-15",
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

## Look Up a Prescription Fill

Retrieve details for a specific prescription fill.

### Endpoint

`GET /api/v2/prescription-fills/{fill_id}`

### Response

Returns detailed fill object including:
- Basic fill information
- Patient details
- Medication information
- Insurance claims
- Fill status history
- Special handling notes

## Send Fill to Vial Dispensing Robot

Send a prescription fill to an available vial dispensing robot.

### Endpoint

`POST /api/v2/prescription-fills/{fill_id}/robot`

### Notes

- Fill sent to any available robot
- Most pharmacies have single robot
- Status updates received asynchronously
- Error handling automated

## Reverse Paid Claims

Attempt to reverse any paid insurance claims on a fill.

### Endpoint

`POST /api/v2/prescription-fills/{fill_id}/reverse-claims`

### Process

1. Attempts to reverse all paid claims
2. If successful:
   - Claims reversed
   - Fill status set to Hold
3. If errors occur:
   - List of errors returned
   - Partial reversals possible

### Response

#### Success Response (200 OK)

```json
{
  "success": true,
  "message": "All claims reversed successfully",
  "fill_status": "hold",
  "reversed_claims": [
    {
      "claim_id": "clm_12345",
      "reversal_date": "2025-02-19T08:50:00Z",
      "amount": 125.00
    }
  ]
}
```

#### Error Response (200 OK with Errors)

```json
{
  "success": false,
  "errors": [
    {
      "claim_id": "clm_12345",
      "message": "Claim outside reversal window"
    }
  ]
}
```

## Add Bin Location

Assign a bin location to a prescription fill.

### Endpoint

`POST /api/v2/prescription-fills/{fill_id}/bin-location`

### Request Body

```json
{
  "bin_location_name": "A-15"
}
```

### Response

Returns updated fill object with new bin location.

## Set Fill Status

Update the status of a prescription fill.

### Endpoint

`POST /api/v2/prescription-fills/{fill_id}/status`

### Request Body

```json
{
  "status": "ready"
}
```

### Valid Status Values

- Hold
- Ready
- Sold
- Rejected
- Verified
- Scanning
- Adjudicating
- Out of Stock

### Important Notes

Status changes may trigger automated workflows:
- Ready → Notification to patient
- Sold → Inventory adjustment
- Rejected → Prescriber notification
- Out of Stock → Ordering system alert

## Best Practices

1. Fill Management
   - Validate quantities
   - Check days supply
   - Monitor fill status
   - Track bin locations

2. Robot Integration
   - Check robot status
   - Monitor fill progress
   - Handle errors gracefully
   - Track completion

3. Claims Processing
   - Verify insurance
   - Track claim status
   - Handle reversals properly
   - Document rejections

4. Status Updates
   - Follow proper workflow
   - Update related records
   - Notify relevant parties
   - Maintain audit trail

### Additional Information

- URL requests expire after 30 days
- All updates are logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported
- Integration with:
  * Dispensing robots
  * Insurance systems
  * Inventory management
  * Patient notifications