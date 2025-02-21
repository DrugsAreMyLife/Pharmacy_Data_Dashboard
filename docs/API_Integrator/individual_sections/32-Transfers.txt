# Transfers

This section covers the endpoints related to managing prescription transfers between pharmacies in the DRX API.

## Look Up a Competing Pharmacy

Retrieve information about a competing pharmacy for transfers.

### Endpoint

`GET /api/v2/competing-pharmacies/{identifier}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| identifier | string | Pharmacy ID, NPI, or DEA |

### Response

#### Success Response (200 OK)

```json
{
  "id": "pharm_12345",
  "name": "Example Pharmacy",
  "npi": "1234567890",
  "dea": "AB1234567",
  "ncpdp": "1234567",
  "phone": "+11234567890",
  "fax": "+11234567890",
  "address": {
    "street": "123 Main St",
    "city": "Austin",
    "state": "TX",
    "zip_code": "78701"
  },
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

## Get a List of Competing Pharmacies

Retrieve a list of pharmacies available for transfers.

### Endpoint

`GET /api/v2/competing-pharmacies`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Records to return |
| offset | integer | Offset for pagination |
| search | string | Search by name, NPI, DEA, etc. |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "pharm_12345",
      "name": "Example Pharmacy",
      "npi": "1234567890",
      "phone": "+11234567890",
      "address": {
        "city": "Austin",
        "state": "TX"
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

## Add a Competing Pharmacy

Add a new pharmacy to the system for future transfers.

### Endpoint

`POST /api/v2/competing-pharmacies`

### Required Fields

| Field | Description |
|-------|-------------|
| name | Pharmacy name |
| fax_number | Format: +11234567890 |

### Optional Fields

| Field | Description |
|-------|-------------|
| npi | National Provider Identifier |
| dea | DEA number |
| ncpdp | NCPDP number |
| phone | Format: +11234567890 |
| address | Street address |
| city | City |
| state | State |
| zip_code | ZIP code |

### Example Request

```json
{
  "name": "Example Pharmacy",
  "fax_number": "+11234567890",
  "npi": "1234567890",
  "phone": "+11234567890",
  "address": "123 Main St",
  "city": "Austin",
  "state": "TX",
  "zip_code": "78701"
}
```

## Send a Transfer Out

Transfer prescriptions to another pharmacy.

### Endpoint

`POST /api/v2/transfers/out`

### Pharmacy Identification (One Required)

| Field | Description |
|-------|-------------|
| id | Competing Pharmacy Primary Key |
| dea | Competing Pharmacy DEA |
| npi | Competing Pharmacy NPI |

### Transfer Object (Required)

Array of objects, each containing:
| Field | Description |
|-------|-------------|
| prescription_id | Prescription Primary Key |
| qty | Transfer quantity |

### Required Fields

| Field | Description |
|-------|-------------|
| receiving_rph | Receiving pharmacist name |
| transferring_rph | Transferring pharmacist name |

### Optional Fields

| Field | Description |
|-------|-------------|
| fax_transfer | Send via fax (requires fax number) |
| fax_number | Format: +11234567890 |

### Example Request

```json
{
  "id": "pharm_12345",
  "transfers": [
    {
      "prescription_id": "rx_67890",
      "qty": 30
    }
  ],
  "receiving_rph": "Jane Smith",
  "transferring_rph": "John Doe",
  "fax_transfer": true
}
```

### Create Pharmacy On-the-Fly

If pharmacy doesn't exist, provide:
1. Required (One of):
   - DEA number
   - NPI number
2. Required:
   - Pharmacy name
3. Optional:
   - Fax number

## Best Practices

1. Pharmacy Verification
   - Validate identifiers
   - Verify contact info
   - Check credentials
   - Confirm hours

2. Transfer Processing
   - Check prescription eligibility
   - Verify quantities
   - Document transfer
   - Update records

3. Communication
   - Confirm receipt
   - Track fax status
   - Follow up if needed
   - Document contacts

4. Record Keeping
   - Log all transfers
   - Maintain audit trail
   - Track outcomes
   - Document issues

### Additional Information

- URL requests expire after 30 days
- All transfers logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported
- Integration with:
  * Prescription system
  * Fax system
  * Patient records
  * Regulatory reporting