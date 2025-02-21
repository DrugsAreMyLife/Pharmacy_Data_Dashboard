# SMS

This section covers the endpoints related to sending SMS messages in the DRX API.

## Send SMS

Send an SMS message to any phone number.

### Endpoint

`POST /api/v2/sms/send`

### Required Fields

| Field | Definition |
|-------|------------|
| to | Phone number (string) |
| body | Message content |

### Optional Fields

| Field | Definition |
|-------|------------|
| from | Custom sender ID (if enabled) |
| scheduled_time | Future send time (ISO 8601) |
| template_id | Message template identifier |
| variables | Template variables object |
| metadata | Custom metadata object |

### Example Request

```json
{
  "to": "5551234567",
  "body": "Your prescription is ready for pickup",
  "metadata": {
    "prescription_id": "rx_12345",
    "patient_id": "pat_67890"
  }
}
```

### Template Example

```json
{
  "to": "5551234567",
  "template_id": "rx_ready",
  "variables": {
    "patient_name": "John",
    "rx_number": "123456",
    "pickup_location": "Main Street"
  }
}
```

### Response

#### Success Response (200 OK)

```json
{
  "id": "sms_12345",
  "status": "sent",
  "to": "5551234567",
  "delivery_status": "pending",
  "segments": 1,
  "created_at": "2025-02-19T08:50:00Z",
  "metadata": {
    "prescription_id": "rx_12345",
    "patient_id": "pat_67890"
  }
}
```

#### Error Response (400 Bad Request)

```json
{
  "error": {
    "code": "invalid_number",
    "message": "Invalid phone number format",
    "details": {
      "field": "to",
      "value": "invalid_number"
    }
  }
}
```

### Message Templates

Pre-defined templates available:
1. Prescription Ready
2. Refill Reminder
3. Prescription Expiring
4. Delivery Update
5. Payment Confirmation

### Character Limits

- Single SMS: 160 characters
- Multi-part SMS: Up to 1600 characters (10 segments)
- Unicode messages: 70 characters per segment

### Best Practices

1. Message Content
   - Keep messages concise
   - Include essential info
   - Avoid sensitive data
   - Use clear language

2. Phone Numbers
   - Validate format
   - Check opt-out status
   - Respect quiet hours
   - Monitor delivery

3. Template Usage
   - Use standard templates
   - Validate variables
   - Test rendering
   - Monitor success rates

4. Error Handling
   - Handle invalid numbers
   - Track failures
   - Retry failed messages
   - Log all attempts

### Compliance Requirements

1. Opt-in/Opt-out
   - Maintain consent records
   - Honor opt-out requests
   - Provide opt-out instructions
   - Track preference changes

2. Message Content
   - No PHI in messages
   - Include business name
   - Provide contact info
   - Follow regulations

3. Timing Restrictions
   - Respect quiet hours
   - Consider time zones
   - Follow frequency limits
   - Monitor send patterns

4. Record Keeping
   - Store consent records
   - Track message history
   - Maintain audit logs
   - Document compliance

### Additional Information

- URL requests expire after 30 days
- All messages logged
- Audit trail maintained
- Historical data preserved
- Real-time status updates
- Integration with:
  * Patient portal
  * Notification system
  * Compliance monitoring
  * Analytics platform