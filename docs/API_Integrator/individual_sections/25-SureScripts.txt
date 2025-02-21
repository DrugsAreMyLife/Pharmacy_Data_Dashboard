# SureScripts

This section covers the endpoints related to managing SureScripts electronic prescriptions in the DRX API.

## Look Up a SureScript

Retrieve details for a specific SureScript record.

### Endpoint

`GET /api/v2/surescripts/{surescript_id}`

### Response

#### Success Response (200 OK)

```json
{
  "id": "ss_12345",
  "message_id": "msg_67890",
  "status": "pending",
  "patient": {
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1980-01-15",
    "gender": "M"
  },
  "prescriber": {
    "first_name": "Jane",
    "last_name": "Smith",
    "npi": "1234567890",
    "dea": "AB1234567"
  },
  "medication": {
    "name": "Example Medication 10mg Tablet",
    "ndc": "12345-6789-10",
    "quantity": 30,
    "days_supply": 30,
    "refills": 2,
    "sig": "Take 1 tablet by mouth daily"
  },
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

## Get a List of SureScripts (Intake Queue)

Retrieve scripts in the Intake Queue or processed scripts.

### Endpoint

`GET /api/v2/surescripts`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Records to return |
| offset | integer | Offset for pagination |
| showOldItems | boolean | Show processed scripts |
| external_id | string | Search by external ID |
| search | string | Search patient/drug name |
| ehrMessageId | string | Filter by message ID |
| ehrOrderNumber | string | Filter by order number |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "ss_12345",
      "status": "pending",
      "patient": {
        "first_name": "John",
        "last_name": "Doe"
      },
      "medication": {
        "name": "Example Medication 10mg Tablet"
      },
      "created_at": "2025-02-19T08:50:00Z"
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

## Generate SureScript

Create a new SureScript in the intake queue.

### Endpoint

`POST /api/v2/surescripts`

### Required Objects

1. Patient Object (One Required):
   - Option 1: ID
     ```json
     {
       "id": "pat_12345"
     }
     ```
   - Option 2: Details
     ```json
     {
       "first_name": "John",
       "last_name": "Doe",
       "gender": "M",
       "dob": "1980-01-15"
     }
     ```

2. Doctor Object (One Required):
   - Option 1: Identifier
     ```json
     {
       "id": "doc_12345"
     }
     ```
   - Option 2: Details
     ```json
     {
       "first_name": "Jane",
       "last_name": "Smith",
       "npi": "1234567890"
     }
     ```

3. Medication Object (One Required):
   - Option 1: Identifier
     ```json
     {
       "id": "med_12345"
     }
     ```
   - Option 2: Details
     ```json
     {
       "name": "Example Medication 10mg Tablet"
     }
     ```

### Optional Fields

| Field | Definition |
|-------|------------|
| comment | Additional notes |
| external_id | External reference |

## Cancel Message

Cancel a prescription message.

### Endpoint

`POST /api/v2/surescripts/cancel`

### Required Components

1. Item Identification (One Required):
   - item_id or item_ndc
   - Or Item Object with name and NDC

2. Patient Identification (One Required):
   - patient_id
   - Or Patient Object with details

3. Doctor Identification (One Required):
   - doctor_id (Primary Key, DEA, or NPI)
   - Or Doctor Object with details

4. Cancel Order Object:
   ```json
   {
     "unit": "EA",
     "refills": 0,
     "quantity": 30,
     "directions": "Take 1 tablet daily"
   }
   ```

## Delete a SureScript from the Intake Queue

Permanently delete a SureScript from the queue.

### Endpoint

`DELETE /api/v2/surescripts/{surescript_id}`

### Important Note

- Deletion is permanent
- No recovery possible
- Verify before deleting

## Edit Intake Item

Update a SureScript in the intake queue.

### Endpoint

`PATCH /api/v2/surescripts/{surescript_id}`

### Editable Fields

| Field | Definition |
|-------|------------|
| consumed | Remove from intake queue |
| patient_id | Patient Primary key |
| patient_first_name | Patient First Name |
| patient_last_name | Patient Last Name |
| doctor_first_name | Doctor First Name |
| doctor_last_name | Doctor Last Name |
| drug_name | Medication Name |
| note | Additional Notes |
| external_id | External Reference |

## Best Practices

1. Message Management
   - Validate all required fields
   - Check message format
   - Monitor message status
   - Handle errors properly

2. Queue Processing
   - Process in order
   - Check for duplicates
   - Verify patient matches
   - Document actions

3. Cancellation Handling
   - Verify cancel eligibility
   - Document reason
   - Notify relevant parties
   - Track cancellation status

4. System Integration
   - Monitor connectivity
   - Handle timeouts
   - Verify message delivery
   - Track message status

### Additional Information

- URL requests expire after 30 days
- All actions logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported
- Integration with:
  * EHR systems
  * Pharmacy system
  * Provider networks
  * Regulatory reporting