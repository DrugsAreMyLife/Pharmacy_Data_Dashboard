# Phone Numbers

This section covers the endpoints related to managing phone numbers in the DRX API.

## Look Up a Phone Number

Retrieve details for a specific phone number.

### Endpoint

`GET /api/v2/phone-numbers/{phone_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| phone_id | string | Primary key of the phone number |

### Response

#### Success Response (200 OK)

```json
{
  "id": "phn_12345",
  "number": "5551234567",
  "phone_type": "cell",
  "primary": true,
  "verified": true,
  "do_not_call": false,
  "linked_to": {
    "type": "patient",
    "id": "pat_67890",
    "name": "John Doe"
  },
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

## Get a List of Phone Numbers

Retrieve a list of phone numbers with optional filtering and search.

### Endpoint

`GET /api/v2/phone-numbers`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Number of records to return |
| offset | integer | Offset for pagination |
| q | string | Search query |

### Search Criteria

| Criteria | Example | Format |
|----------|---------|---------|
| Phone Number | 5852984455 | 10 digits, partial matches supported |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "phn_12345",
      "number": "5551234567",
      "phone_type": "cell",
      "primary": true,
      "linked_to": {
        "type": "patient",
        "id": "pat_67890",
        "name": "John Doe"
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

## Add a Phone Number

Add a new phone number for a patient or doctor.

### Endpoint

`POST /api/v2/phone-numbers`

### Required Fields

| Field | Definition |
|-------|------------|
| number | 10-digit phone number |
| phone_type | 'cell', 'home', or 'other' |

### Link Fields (One Required)

| Field | Definition |
|-------|------------|
| patient_id | Patient ID to link number to |
| doctor_id | Doctor ID to link number to |

### Example Request

```json
{
  "number": "5551234567",
  "phone_type": "cell",
  "patient_id": "pat_67890"
}
```

### Response

#### Success Response (201 Created)

```json
{
  "id": "phn_12345",
  "number": "5551234567",
  "phone_type": "cell",
  "primary": false,
  "verified": false,
  "do_not_call": false,
  "linked_to": {
    "type": "patient",
    "id": "pat_67890",
    "name": "John Doe"
  },
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

## Edit a Phone Number

Update an existing phone number's information.

### Endpoint

`PATCH /api/v2/phone-numbers/{phone_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| phone_id | string | Primary key of the phone number |

### Editable Fields

| Field | Definition |
|-------|------------|
| number | Phone number |
| phone_type | 'home', 'cell', 'other' |
| primary | Boolean |
| do_not_call | Boolean |

### Example Request

```json
{
  "phone_type": "home",
  "primary": true
}
```

### Response

#### Success Response (200 OK)

Returns the updated phone number object.

### Notes

- Omitted fields remain unchanged
- Only one primary number allowed per type
- Setting a new primary automatically unsets old primary

## Best Practices

1. Phone Number Management
   - Validate formats
   - Verify numbers when possible
   - Maintain accurate types
   - Track primary numbers

2. Data Quality
   - Remove formatting
   - Store consistent format
   - Check for duplicates
   - Validate area codes

3. Communication Preferences
   - Respect do-not-call flags
   - Track preferred numbers
   - Note best contact times
   - Monitor delivery success

4. System Integration
   - Link to messaging system
   - Connect to auto-dialers
   - Update related records
   - Sync contact lists

### Additional Information

- URL requests expire after 30 days
- All updates are logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported