# Tasks

This section covers the endpoints related to managing background tasks and exports in the DRX API.

## Get Task Status Updates

Check the status and details of a specific task.

### Endpoint

`GET /api/v2/tasks/{task_id}`

### Response

#### Success Response (200 OK)

```json
{
  "id": "task_12345",
  "type": "fill_export",
  "status": "completed",
  "progress": 100,
  "created_at": "2025-02-19T08:50:00Z",
  "started_at": "2025-02-19T08:50:05Z",
  "completed_at": "2025-02-19T09:00:00Z",
  "meta": {
    "details": {
      "records_processed": 1500,
      "file_size": 256000,
      "path": "https://example.com/exports/export_12345.csv"
    }
  }
}
```

### Notes

- Completed files uploaded to pharmacy's storage
- Files guaranteed available for 30 days
- Complete file URL in meta.details.path
- Status values: pending, processing, completed, failed

## Start a New Task

Start a background task for bulk data exports.

### Endpoint

`POST /api/v2/tasks`

### Required Fields

| Field | Definition |
|-------|------------|
| task_name | Name of task to start |
| start_date | Start date (if required) |
| end_date | End date (if required) |

### Optional Fields

| Field | Definition |
|-------|------------|
| fields | Desired output fields |
| format | 'json' or 'csv' (default: json) |
| delimiter | CSV delimiter |
| sold_after | Fills sold after date |
| sold_before | Fills sold before date |

### Available Tasks

| Task | Description | Required Parameters | Optional Parameters |
|------|-------------|-------------------|-------------------|
| fill_export | Bulk prescription fill export | start_date, end_date | fields, format, delimiter, sold_after, sold_before |

### Available Fields for fill_export

1. Prescription Information
   - Rx number
   - Written date
   - Expiration date
   - Status
   - Quantity
   - Days supply
   - Refills remaining

2. Patient Information
   - ID
   - Name
   - Date of birth
   - Gender
   - Address
   - Phone numbers

3. Doctor Information
   - ID
   - Name
   - NPI
   - DEA
   - Address
   - Phone numbers

4. Fill Details
   - Fill date
   - Fill number
   - Quantity dispensed
   - Days supply
   - Status
   - Bin location
   - Fill tags

5. Third Party Information
   - Insurance carrier
   - Plan information
   - Claim details
   - Payment information
   - Rejection codes

6. Store Information
   - Store ID
   - Location
   - Pharmacist
   - Fill date/time
   - Verification date/time

### Example Request

```json
{
  "task_name": "fill_export",
  "start_date": "2025-01-01",
  "end_date": "2025-02-19",
  "format": "csv",
  "fields": [
    "rx_number",
    "patient_name",
    "fill_date",
    "quantity",
    "days_supply"
  ]
}
```

### Response

#### Success Response (200 OK)

```json
{
  "task_id": "task_12345",
  "status": "pending",
  "message": "Export task created successfully",
  "estimated_completion": "2025-02-19T09:00:00Z"
}
```

#### Error Response (400 Bad Request)

```json
{
  "error": {
    "code": "invalid_parameters",
    "message": "Invalid date range",
    "details": {
      "start_date": "must be before end_date"
    }
  }
}
```

## Best Practices

1. Task Management
   - Monitor task status
   - Handle timeouts
   - Implement retries
   - Clean up completed tasks

2. Export Configuration
   - Select needed fields
   - Use appropriate format
   - Consider file size
   - Plan for large datasets

3. Resource Usage
   - Schedule during off-hours
   - Monitor system load
   - Limit concurrent tasks
   - Clean up old exports

4. Error Handling
   - Validate parameters
   - Handle failures gracefully
   - Provide clear messages
   - Log all issues

### Additional Information

- URL requests expire after 30 days
- All tasks logged
- Audit trail maintained
- Historical data preserved
- Real-time status updates
- Integration with:
  * Storage system
  * Notification system
  * Monitoring tools
  * Analytics platform