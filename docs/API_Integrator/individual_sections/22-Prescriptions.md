# Prescriptions

This section covers the endpoints related to managing prescriptions in the DRX API.

## Get a List of Prescriptions

Retrieve a list of prescriptions with optional filtering.

### Endpoint

`GET /api/v2/prescriptions`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| patient_id | string | Filter by patient |
| status | string | Filter by status |
| facility_id | string | Filter by patient's facility |
| ehr_message_id | string | Filter by EHR message ID |
| ehr_order_number | string | Filter by EHR order number |
| expiration_date | string | Filter by expiration date |
| before_date | string | Get prescriptions filled before date |
| after_date | string | Get prescriptions filled after date |

### Valid Status Values

- Hold
- Waiting Bin
- Sold
- Print
- Rejected
- Verify
- Scan
- Adjudicating
- OOS (Out of Stock)

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "rx_12345",
      "patient_id": "pat_67890",
      "doctor_id": "doc_11111",
      "status": "active",
      "prescribed_quantity": 30,
      "dispensed_quantity": 30,
      "days_supply": 30,
      "refills_remaining": 2,
      "date_written": "2025-02-01",
      "date_expires": "2026-02-01",
      "medication": {
        "id": "med_22222",
        "name": "Example Medication 10mg Tablet",
        "ndc": "12345-6789-10"
      },
      "sig": "Take 1 tablet by mouth daily",
      "daw": "0",
      "origin_code": "Electronic",
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

## Look Up a Prescription

Retrieve details for a specific prescription.

### Endpoint

`GET /api/v2/prescriptions/{prescription_id}`

### Response

Returns detailed prescription object including:
- Basic prescription information
- Patient details
- Prescriber information
- Medication details
- Fill history
- Insurance information
- Status history

## Send Hard Copy Image to Intake

Send a prescription hard copy image for processing.

### Endpoint

`POST /api/v2/prescriptions/intake`

### Required Fields

| Field | Definition |
|-------|------------|
| base64_image_data | Image data in base64 format |
| drug_name | Name of prescribed medication |

### Optional Fields

| Field | Definition |
|-------|------------|
| sig | Medication instructions |
| comment | Additional notes |

### Patient Identification

Either provide:
- Patient ID, or
- Patient Details:
  * first_name
  * last_name
  * dob (ISO format)
  * gender ('M' or 'F')

### Doctor Identification

Either provide:
- Doctor ID, or
- Doctor Details:
  * first_name
  * last_name

## Generate a Prescription

Create a new prescription and assign an Rx number.

### Endpoint

`POST /api/v2/prescriptions`

### Required Fields

| Field | Definition |
|-------|------------|
| patient_id | Patient Primary Key |
| doctor_id | Doctor Primary Key |
| prescribed_quantity | Decimal quantity prescribed |
| dispensed_quantity | Decimal quantity dispensed |
| item_id | Item Primary Key |
| days_supply | Integer days supply |

### Optional Fields

| Field | Definition |
|-------|------------|
| pharmacist_id | Pharmacist User Primary Key |
| date_written | ISO format date |
| date_expires | ISO format date |
| daw | String: 0-9 (defaults to 0) |
| origin_code | Source of prescription |
| refills | Integer number of refills |
| fill_date | ISO format date |
| serial_number | String serial number |
| pickup_time | ISO format date |
| primary_third_party_id | Primary Insurance ID |
| secondary_third_party_id | Secondary Insurance ID |
| tertiary_third_party_id | Tertiary Insurance ID |
| primary_third_party_bin | Primary Insurance BIN |
| secondary_third_party_bin | Secondary Insurance BIN |
| tertiary_third_party_bin | Tertiary Insurance BIN |
| sig | Medication instructions |
| fill_tags | Array of tag strings |
| base64_image_data | Image data in base64 format |
| status | Current status (defaults to 'Hold') |

## Inactivate Prescription

Halt future adjudications and scheduled fill dates.

### Endpoint

`POST /api/v2/prescriptions/{prescription_id}/inactivate`

### Optional Parameters

| Field | Description |
|-------|-------------|
| reason | Reason for inactivation |

### Response

Returns updated prescription object with inactive status.

## Reactivate Prescription

Reactivate a previously inactivated prescription.

### Endpoint

`POST /api/v2/prescriptions/{prescription_id}/reactivate`

### Response

Returns updated prescription object with active status.

## Best Practices

1. Prescription Management
   - Validate all required fields
   - Check expiration dates
   - Monitor refill counts
   - Track prescription status

2. Image Processing
   - Use appropriate resolution
   - Validate image quality
   - Include all pages
   - Check file size limits

3. Status Updates
   - Handle transitions properly
   - Update related records
   - Notify relevant parties
   - Maintain audit trail

4. Security Considerations
   - Validate permissions
   - Track all changes
   - Monitor suspicious activity
   - Protect sensitive data

### Additional Information

- URL requests expire after 30 days
- All updates are logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported