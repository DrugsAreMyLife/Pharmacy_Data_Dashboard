# Allergies

This section covers all allergy-related endpoints in the DRX API, including looking up allergies, listing allergies, and adding allergies to patients.

## Look Up an Allergy

Retrieve detailed information about a specific allergy using its unique identifier.

### Endpoint

`GET /api/v2/allergies/{allergy_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| allergy_id | string | Unique identifier of the allergy to retrieve |

### Response

#### Success Response (200 OK)

```json
{
  "id": "alg_12345",
  "name": "Penicillin",
  "category": "medication",
  "description": "Beta-lactam antibiotic",
  "common_reactions": [
    "Rash",
    "Hives",
    "Difficulty breathing"
  ],
  "severity_levels": [
    "mild",
    "moderate",
    "severe"
  ],
  "contraindications": [
    "Previous anaphylactic reaction",
    "Family history of severe reactions"
  ],
  "alternatives": [
    "Erythromycin",
    "Azithromycin"
  ],
  "created_at": "2025-02-19T09:00:00Z",
  "updated_at": "2025-02-19T09:00:00Z"
}
```

#### Error Responses

- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Allergy ID does not exist

### Notes

- All allergy details are included in the response
- Common reactions are listed in order of frequency
- Severity levels indicate possible reaction intensities
- Contraindications help identify high-risk situations
- Alternatives suggest substitute medications/substances
- Response includes both the created_at and updated_at timestamps

## Get a List of Allergies

Retrieve a list of all allergies in the system with pagination and filtering options.

### Endpoint

`GET /api/v2/allergies`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| page | integer | Page number for pagination (default: 1) |
| per_page | integer | Number of items per page (default: 20, max: 100) |
| category | string | Filter by allergy category (e.g., "medication", "food") |
| severity | string | Filter by severity level |
| search | string | Search term to filter allergies by name or description |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "alg_12345",
      "name": "Penicillin",
      "category": "medication",
      "description": "Beta-lactam antibiotic",
      "common_reactions": [
        "Rash",
        "Hives",
        "Difficulty breathing"
      ],
      "severity_levels": [
        "mild",
        "moderate",
        "severe"
      ],
      "created_at": "2025-02-19T09:00:00Z",
      "updated_at": "2025-02-19T09:00:00Z"
    }
  ],
  "pagination": {
    "total_items": 150,
    "total_pages": 8,
    "current_page": 1,
    "per_page": 20,
    "next_page": 2,
    "prev_page": null
  }
}
```

#### Error Responses

- 401 Unauthorized: Invalid or missing API key
- 400 Bad Request: Invalid query parameters

### Notes

- Results are sorted alphabetically by allergy name
- Empty or invalid filters are ignored
- All allergy details are included in the response
- Pagination metadata is always included
- Maximum of 100 allergies can be retrieved per request
- Use the search parameter for partial name matches

## Add an Allergy to a Patient

Record a new allergy for a specific patient in the system.

### Endpoint

`POST /api/v2/patients/{patient_id}/allergies`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| patient_id | string | Unique identifier of the patient |

### Request Body

| Field | Type | Description |
|-------|------|-------------|
| allergy_id | string | Unique identifier of the allergy |
| severity | string | Severity level of the allergy ("mild", "moderate", "severe") |
| reaction | string | Description of the allergic reaction |
| notes | string | Additional notes about the allergy (optional) |
| onset_date | string | Date when the allergy was first observed (ISO 8601) |

### Example Request

```json
{
  "allergy_id": "alg_12345",
  "severity": "moderate",
  "reaction": "Hives and difficulty breathing",
  "notes": "Requires immediate medical attention if exposed",
  "onset_date": "2025-01-15"
}
```

### Response

#### Success Response (201 Created)

```json
{
  "id": "pat_alg_67890",
  "patient_id": "pat_12345",
  "allergy_id": "alg_12345",
  "severity": "moderate",
  "reaction": "Hives and difficulty breathing",
  "notes": "Requires immediate medical attention if exposed",
  "onset_date": "2025-01-15",
  "created_at": "2025-02-19T09:00:00Z",
  "updated_at": "2025-02-19T09:00:00Z"
}
```

#### Error Responses

- 400 Bad Request: Invalid request data
- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Patient or allergy not found
- 422 Unprocessable Entity: Missing required fields

### Notes

- All fields except notes are required
- Severity must be one of: "mild", "moderate", "severe"
- Onset date must be in ISO 8601 format (YYYY-MM-DD)
- The allergy_id must reference a valid allergy in the system
- Multiple allergies can be recorded for the same patient
- Historical allergy records are preserved for medical history