# Doctors

This section covers the endpoints related to managing doctor information and searching the provider catalog in the DRX API.

## Look Up a Doctor

Retrieve detailed information about a specific doctor.

### Endpoint

`GET /api/v2/doctors/{identifier}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| identifier | string | Doctor primary key, DEA number, or NPI |

### Response

#### Success Response (200 OK)

```json
{
  "id": "doc_12345",
  "first_name": "John",
  "last_name": "Smith",
  "prescriber_type": "M.D.",
  "npi": "1234567890",
  "dea": "AB1234567",
  "spi": "12345",
  "renewal_method": "E-Script",
  "fax_number": "5551234567",
  "email": "john.smith@example.com",
  "website": "www.example.com",
  "state_license": "TX12345",
  "practice_location": "Austin Medical Center",
  "comments": "Preferred contact method: E-Script",
  "addresses": [
    {
      "type": "default",
      "street": "123 Medical Pkwy",
      "line_two": "Suite 100",
      "city": "Austin",
      "state": "TX",
      "zip": "78701"
    }
  ],
  "phone_numbers": [
    {
      "type": "office",
      "number": "5551234567"
    }
  ],
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

### Notes

- Multiple identifiers can be used to look up doctors
- All contact information is included when available
- Historical data is preserved for audit purposes

## Get a List of Doctors

Retrieve a list of doctors with optional filtering and search capabilities.

### Endpoint

`GET /api/v2/doctors`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Number of records to return |
| offset | integer | Offset for pagination |
| q | string | Search query |

### Search Criteria

| Criteria | Example | Format |
|----------|---------|---------|
| Date of Birth | 01201986 | MMDDYYYY |
| Phone Number | 5852984455 | 10 digits, no formatting |
| Name | naugle,ron | last_name,first_name |
| Name | naugle | last name only |
| Name | naugle,r | partial names allowed |
| Fax Number | 5852984455 | 10 digits |
| NPI | 1234567890 | 10 digits |
| DEA | AB1234567 | Standard DEA format |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "doc_12345",
      "first_name": "John",
      "last_name": "Smith",
      "prescriber_type": "M.D.",
      "npi": "1234567890",
      "dea": "AB1234567",
      "spi": "12345",
      "renewal_method": "E-Script",
      "created_at": "2025-01-01T00:00:00Z",
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

## Search Provider Catalog

Search the SureScripts list of providers.

### Endpoint

`GET /api/v2/providers/search`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| first_name | string | Provider first name |
| last_name | string | Provider last name |
| spi | string | SureScripts Provider ID |
| dea | string | DEA number |
| npi | string | NPI number |
| state | string | Two-letter state code |

### Response

#### Success Response (200 OK)

```json
{
  "providers": [
    {
      "first_name": "John",
      "last_name": "Smith",
      "prescriber_type": "M.D.",
      "npi": "1234567890",
      "dea": "AB1234567",
      "spi": "12345",
      "address": {
        "street": "123 Medical Pkwy",
        "city": "Austin",
        "state": "TX",
        "zip": "78701"
      }
    }
  ]
}
```

## Add a Doctor

Add a new doctor to the system.

### Endpoint

`POST /api/v2/doctors`

### Request Body

#### Required Prescriber Object Fields

| Field | Definition |
|-------|------------|
| first_name | Prescriber first name |
| last_name | Prescriber last name |
| npi | National Provider Identifier |

#### Optional Prescriber Fields

| Field | Definition |
|-------|------------|
| prescriber_type | M.D., N.P., ARNP, D.V.M., P.A., F.P.N |
| supervising_physician_id | Foreign key to Supervising Physician |
| dea | DEA number |
| spi | SureScripts Prescriber ID |
| renewal_method | 'E-Script', 'Fax', 'Phone' |
| fax_number | 10 digit fax number |
| email | Doctor email |
| website | Doctor website |
| state_license | Doctor's state license |
| practice_location | Doctor's practice location |
| comments | Additional comments |

#### Required Address Fields

Each address object must include:
| Field | Definition |
|-------|------------|
| street | Street address |
| city | City |
| state | State |
| zip | ZIP code |
| type_ | 'default', 'delivery', 'shipping', or 'billing' |

#### Optional Address Fields

| Field | Definition |
|-------|------------|
| line_two | Additional address line |

#### Required Phone Number Fields

Each phone number object must include:
| Field | Definition |
|-------|------------|
| number | 10-digit phone number |
| phone_type | 'cell', 'home', 'other' |

### Example Request

```json
{
  "prescriber": {
    "first_name": "John",
    "last_name": "Smith",
    "npi": "1234567890",
    "prescriber_type": "M.D.",
    "dea": "AB1234567",
    "renewal_method": "E-Script"
  },
  "addresses": [
    {
      "street": "123 Medical Pkwy",
      "city": "Austin",
      "state": "TX",
      "zip": "78701",
      "type_": "default"
    }
  ],
  "phone_numbers": [
    {
      "number": "5551234567",
      "phone_type": "office"
    }
  ]
}
```

### Response

#### Success Response (201 Created)

Returns the created doctor object with all fields.

### Notes

- NPI validation is performed on submission
- DEA number format is validated if provided
- At least one address is required
- At least one phone number is required
- All phone/fax numbers must be 10 digits
- URL requests expire after 30 days

## Best Practices

1. Validate all identifiers before submission
2. Keep contact information current
3. Use appropriate prescriber types
4. Maintain accurate renewal preferences
5. Document special instructions in comments
6. Regularly verify provider credentials

## Additional Information

- Provider catalog is updated daily
- Historical provider data is preserved
- All updates are logged for audit purposes
- Provider relationships are maintained
- Credential verification is automated