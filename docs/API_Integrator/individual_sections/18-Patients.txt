# Patients

This section covers the endpoints related to managing patient information in the DRX API.

## Look Up a Patient

Retrieve detailed information about a specific patient.

### Endpoint

`GET /api/v2/patients/{patient_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| patient_id | string | Unique identifier of the patient |

### Response

#### Success Response (200 OK)

```json
{
  "id": "pat_12345",
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1980-01-15",
  "gender": "M",
  "email": "john.doe@example.com",
  "middle_initial": "R",
  "status": "active",
  "delivery_method": "Pickup",
  "drivers_license": "12345678",
  "social_security_number": "123-45-6789",
  "alternate_id": "ALT123",
  "auto_refill": true,
  "height_in_centimeters": 180,
  "weight_in_grams": 80000,
  "automatically_charge_rx_to_account": false,
  "blister_pack": false,
  "notify_method": 1,
  "easy_open": true,
  "cycle_fill_date": "2025-03-01",
  "cycle_interval": 30,
  "race": "Human",
  "primary_language": "English",
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

## Get a List of Patients

Retrieve a list of patients with optional filtering and search capabilities.

### Endpoint

`GET /api/v2/patients`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Number of records to return |
| offset | integer | Offset for pagination |
| q | string | Search query |
| before_date | string | Patients who filled before date |
| after_date | string | Patients who filled after date |
| facility_id | string | Filter by facility |

### Search Criteria

| Criteria | Example | Format |
|----------|---------|---------|
| Date of Birth | 01201986 | MMDDYYYY |
| Phone Number | 5852984455 | 10 digits, no formatting |
| Name | safee,dani | last_name,first_name |
| Name | safee | last name only |
| Name | safee,d | partial names allowed |

## Add a Patient

Create a new patient record in the system.

### Endpoint

`POST /api/v2/patients`

### Required Patient Fields

| Field | Definition |
|-------|------------|
| first_name | Patient First Name |
| last_name | Patient Last Name |
| date_of_birth | ISO formatted date string |
| gender | 'M' or 'F' |

### Optional Patient Fields

| Field | Definition |
|-------|------------|
| email | Email address |
| middle_initial | Middle initial |
| dont_notify_again_until | Pause notifications until date |
| delivery_method | 'Ship', 'Pickup', or 'Delivery' |
| drivers_license | Driver's license number |
| social_security_number | Format: 123-45-6789 |
| alternate_id | External ID |
| auto_refill | Boolean |
| height_in_centimeters | Height |
| weight_in_grams | Weight |
| automatically_charge_rx_to_account | Boolean |
| facility_room_id | Facility room reference |
| facility_wing_id | Facility wing reference |
| blister_pack | Boolean |
| notify_method | 1=Email, 2=Phone, 3=Do not notify, 0=Text |
| easy_open | Boolean for non-safety caps |
| cycle_fill_date | Next sync list fill date |
| cycle_interval | Days between fills |
| race | 'Human', 'Dog', 'Cat', 'Bird', 'Reptile', 'Rodent', 'Horse', 'Other' |
| primary_language | 'English' or 'Spanish' |

### Required Address Fields

Each address object must include:
| Field | Definition |
|-------|------------|
| street | Street address |
| city | City |
| state | State |
| zip | ZIP code |
| type_ | 'default', 'delivery', 'shipping', or 'billing' |

### Required Phone Number Fields

Each phone number object must include:
| Field | Definition |
|-------|------------|
| number | 10-digit phone number |
| phone_type | 'cell', 'home', 'other' |

### Example Request

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1980-01-15",
  "gender": "M",
  "email": "john.doe@example.com",
  "delivery_method": "Pickup",
  "addresses": [
    {
      "street": "123 Main St",
      "city": "Austin",
      "state": "TX",
      "zip": "78701",
      "type_": "default"
    }
  ],
  "phone_numbers": [
    {
      "number": "5551234567",
      "phone_type": "cell"
    }
  ]
}
```

## Edit a Patient

Update an existing patient's information.

### Endpoint

`PATCH /api/v2/patients/{patient_id}`

### Editable Fields

All fields listed in the Add a Patient section can be updated, plus:
| Field | Definition |
|-------|------------|
| active | Boolean. Inactive patients hidden from search |
| deceased | Boolean. Shows deceased icon on profile |

## Get a Patient's Profile

Retrieve comprehensive patient profile information.

### Endpoint

`GET /api/v2/patients/{patient_id}/profile`

### Response

Includes all patient information plus:
- Prescription history
- Allergies
- Insurance information
- Payment methods
- Communication preferences
- Family members
- Healthcare providers

## Get a Patient's Sync List

Retrieve a patient's medication synchronization list.

### Endpoint

`GET /api/v2/patients/{patient_id}/sync-list`

### Response

Lists all medications on sync schedule with:
- Next fill dates
- Days supply
- Fill intervals
- Special instructions

## Best Practices

1. Patient Information
   - Validate all required fields
   - Use consistent formats
   - Keep contact info current
   - Document special needs

2. Search Implementation
   - Use appropriate search criteria
   - Handle partial matches
   - Consider phonetic matching
   - Implement smart filtering

3. Data Security
   - Protect sensitive information
   - Log access attempts
   - Implement role-based access
   - Regular security audits

4. System Integration
   - Sync with other systems
   - Maintain data consistency
   - Handle conflicts properly
   - Regular data validation

### Additional Information

- URL requests expire after 30 days
- All updates are logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported