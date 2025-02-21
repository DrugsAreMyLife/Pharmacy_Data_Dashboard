# Refills and Renewals

This section covers the endpoints related to managing prescription refills and renewals in the DRX API.

## Send a Refill Request

Submit a request to refill prescriptions for a patient.

### Endpoint

`POST /api/v2/refills/request`

### Requirements

- Must submit at least patient date of birth OR patient ID (both validated if provided)
- Can only submit refill requests for one patient at a time

### Request Body

```json
{
  "patient_id": "pat_12345",
  "date_of_birth": "1980-01-15",
  "prescriptions": ["rx_67890", "rx_67891"]
}
```

### Response Examples

#### Success Response (200 OK)

```json
{
  "success": true,
  "errors": [],
  "processed": [
    {
      "success": true,
      "message": "Sent to queue for adjudication: Task ID c3ba0298-b145-4f62-abc3-c0988ebccbdd",
      "estimated_pickup_time": "2025-02-19T16:51:20.880789",
      "item_name": "CITALOPRAM HBR 20 MG TABLET",
      "rx_id": "rx_67890"
    }
  ]
}
```

#### Error Response Examples

1. Expired Prescription
```json
{
  "success": true,
  "errors": [
    {
      "success": false,
      "message": "Rx is expired",
      "item_name": "RISPERIDONE 0.25 MG TABLET",
      "rx_id": "rx_67890"
    }
  ],
  "processed": []
}
```

2. Fill in Progress
```json
{
  "success": true,
  "errors": [
    {
      "success": false,
      "message": "Most recent fill still in progress",
      "rx_id": "rx_67890"
    }
  ],
  "processed": []
}
```

3. Patient ID Mismatch
```json
{
  "success": true,
  "errors": [
    {
      "success": false,
      "message": "Patient ID Mismatch",
      "rx_id": "rx_67890"
    }
  ],
  "processed": []
}
```

4. Missing Patient Information
```json
{
  "success": true,
  "errors": [
    {
      "success": false,
      "message": "Patient ID or Date of Birth must be submitted with the request",
      "rx_id": "rx_67890"
    }
  ],
  "processed": []
}
```

5. Insufficient Quantity
```json
{
  "success": true,
  "errors": [
    {
      "success": false,
      "message": "Insufficient qty remaining",
      "remaining": 0,
      "item_name": "CITALOPRAM HBR 20 MG TABLET",
      "rx_id": "rx_67890"
    }
  ],
  "processed": []
}
```

### Notes

- Estimated pickup time is set in store location settings
- Present pickup time as estimate only
- Multiple prescriptions can be requested together
- Each prescription processed independently

## Send in a Renewal

Submit a prescription renewal request to the prescriber.

### Endpoint

`POST /api/v2/renewals/request`

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| rx_number | string | Prescription number |

### Optional Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| renewal_message | string | Message to prescriber |

### Example Request

```json
{
  "rx_number": "123456",
  "renewal_message": "Patient is requesting 90 days supply"
}
```

### Response

#### Success Response (200 OK)

```json
{
  "success": true,
  "message": "Renewal request sent successfully",
  "details": {
    "request_id": "rnw_12345",
    "status": "pending",
    "sent_to": {
      "name": "Dr. Jane Smith",
      "npi": "1234567890"
    },
    "estimated_response": "24-48 hours"
  }
}
```

#### Error Response (200 OK with Error)

```json
{
  "success": false,
  "message": "Renewal recently sent",
  "details": {
    "previous_request": {
      "date": "2025-02-18T08:50:00Z",
      "status": "pending"
    }
  }
}
```

### Demo Environment Note

- Electronic renewals prevented in demo
- Only success or "renewal recently sent" responses
- Production may return additional failure messages

## Best Practices

1. Refill Management
   - Validate eligibility
   - Check remaining refills
   - Monitor fill status
   - Track request history

2. Renewal Processing
   - Verify prescriber information
   - Include relevant details
   - Monitor response times
   - Track renewal status

3. Error Handling
   - Handle all error types
   - Provide clear messages
   - Log failed requests
   - Monitor error patterns

4. System Integration
   - Connect to e-prescribing
   - Update patient records
   - Track communications
   - Monitor workflows

### Additional Information

- URL requests expire after 30 days
- All requests logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported
- Integration with:
  * E-prescribing system
  * Patient portal
  * Provider networks
  * Pharmacy workflow