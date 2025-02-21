# Eligibility

This section covers the real-time eligibility check functionality in the DRX API.

## Real Time Eligibility Check

Perform a real-time E1 Eligibility Search Transaction to verify patient insurance coverage.

### Important Notice

This endpoint will send an E1 Eligibility Search Transaction and incur a cost that will be billed to your store.

### Endpoint

`GET /api/v2/eligibility/check/{patient_id}`

### Prerequisites

- Patient must have a default address in the system
- If no default address exists, use the Add an Address endpoint first

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| patient_id | string | Unique identifier of the patient |

### Response

#### Success Response (200 OK)

```json
{
  "status": "active",
  "coverage": {
    "plan_name": "Example Health Insurance",
    "member_id": "MEM123456",
    "group_number": "GRP789",
    "bin": "123456",
    "pcn": "ABCD",
    "coverage_status": "active",
    "effective_date": "2025-01-01",
    "termination_date": null,
    "coverage_type": "prescription",
    "relationship": "self"
  },
  "benefits": {
    "copays": {
      "retail": {
        "generic": 10.00,
        "brand": 30.00,
        "specialty": 100.00
      },
      "mail_order": {
        "generic": 20.00,
        "brand": 60.00,
        "specialty": 200.00
      }
    },
    "deductible": {
      "individual": 500.00,
      "family": 1000.00,
      "remaining": 250.00
    },
    "out_of_pocket": {
      "individual": 2500.00,
      "family": 5000.00,
      "remaining": 1500.00
    }
  },
  "restrictions": {
    "prior_auth_required": false,
    "step_therapy_required": false,
    "quantity_limits": false
  },
  "transaction": {
    "id": "txn_12345",
    "timestamp": "2025-02-19T08:50:00Z",
    "cost": 0.25
  }
}
```

#### Error Responses

- 400 Bad Request: Invalid patient ID or missing required data
- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Patient not found
- 422 Unprocessable Entity: Patient missing required information (e.g., default address)
- 503 Service Unavailable: Eligibility check service temporarily unavailable

### Notes

1. Transaction Costs
   - Each check incurs a fee
   - Fees are billed to the store
   - Cost is included in response

2. Coverage Information
   - Plan details
   - Member information
   - Coverage dates
   - Benefit levels

3. Benefit Details
   - Copay structures
   - Deductible information
   - Out-of-pocket maximums
   - Coverage restrictions

4. Response Handling
   - Cache results appropriately
   - Monitor transaction costs
   - Log all responses
   - Handle errors gracefully

### Best Practices

1. Cache Eligibility Results
   - Store results for reasonable duration
   - Refresh before critical transactions
   - Clear cache on coverage changes

2. Cost Management
   - Monitor transaction volume
   - Implement rate limiting
   - Track costs by patient/user

3. Error Handling
   - Retry on service failures
   - Log all errors
   - Notify users of issues
   - Provide alternative workflows

4. Data Validation
   - Verify patient information
   - Validate addresses
   - Check coverage dates
   - Monitor response patterns

### Additional Information

- URL requests expire after 30 days
- Results should be cached according to plan rules
- Service availability may vary by time of day
- Some plans may have restricted check hours
- Response times may vary by insurance provider