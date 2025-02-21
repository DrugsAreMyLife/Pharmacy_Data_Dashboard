# Webhooks

This section covers the endpoints related to managing webhooks in the DRX API.

## Look Up a Webhook

Retrieve details for a specific webhook subscription.

### Endpoint

`GET /api/v2/webhooks/{webhook_id}`

### Response

#### Success Response (200 OK)

```json
{
  "id": "whk_12345",
  "url": "https://example.com/webhook",
  "event": "prescription.status.changed",
  "status": "active",
  "header_key": "X-Webhook-Key",
  "header_value": "your-secret-key",
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-02-19T08:50:00Z",
  "last_triggered": "2025-02-19T08:45:00Z",
  "success_count": 150,
  "failure_count": 2
}
```

## Get a List of Webhooks

Retrieve a list of webhook subscriptions.

### Endpoint

`GET /api/v2/webhooks`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Records to return |
| offset | integer | Offset for pagination |
| event | string | Filter by event type |
| status | string | Filter by status |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "whk_12345",
      "url": "https://example.com/webhook",
      "event": "prescription.status.changed",
      "status": "active",
      "created_at": "2025-01-01T00:00:00Z"
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

## Add a Webhook

Subscribe to webhook notifications.

### Endpoint

`POST /api/v2/webhooks`

### Required Fields

| Field | Description |
|-------|-------------|
| url | Webhook destination URL |
| header_key | Authentication header key |
| header_value | Authentication header value |
| event | Event to subscribe to |

### Available Events

1. Prescription Fill Status Changes:
   | Event | Payload |
   |-------|---------|
   | Hold | Prescription Fill Object |
   | Print | Prescription Fill Object |
   | Scan | Prescription Fill Object |
   | Rejected | Prescription Fill Object |
   | Verify | Prescription Fill Object |
   | OOS | Prescription Fill Object |
   | Waiting Bin | Prescription Fill Object |
   | Sold | Prescription Fill Object |
   | Pre-Check | Prescription Fill Object |

2. Prescription Events:
   | Event | Payload |
   |-------|---------|
   | Prescription Created | Prescription Object |

3. Delivery Events:
   | Event | Payload |
   |-------|---------|
   | Delivery | Delivery Object |

4. Miscellaneous Events:
   | Event | Description | Payload |
   |-------|-------------|---------|
   | Update Bin Location | Bin Location updated | Prescription Fill Object |
   | Confirm Pickup | Prescriptions confirmed | Array of Fill Objects |
   | Return to Stock | Items returned | Array of Prescription Objects |

### Example Request

```json
{
  "url": "https://example.com/webhook",
  "header_key": "X-Webhook-Key",
  "header_value": "your-secret-key",
  "event": "prescription.status.changed"
}
```

## Delete a Webhook

Remove a webhook subscription.

### Endpoint

`DELETE /api/v2/webhooks/{webhook_id}`

### Response

#### Success Response (200 OK)

```json
{
  "success": true,
  "message": "Webhook deleted successfully"
}
```

## Best Practices

1. Security
   - Use HTTPS endpoints
   - Validate webhook source
   - Rotate secret keys
   - Monitor access

2. Reliability
   - Implement retry logic
   - Handle timeouts
   - Monitor failures
   - Log all events

3. Performance
   - Process async
   - Handle high volume
   - Monitor latency
   - Scale as needed

4. Error Handling
   - Validate payloads
   - Handle failures
   - Log issues
   - Alert on problems

### Webhook Payload Format

All webhook payloads follow this format:

```json
{
  "id": "evt_12345",
  "event": "prescription.status.changed",
  "created": "2025-02-19T08:50:00Z",
  "data": {
    "id": "rx_67890",
    "status": "ready",
    "previous_status": "processing",
    "changed_at": "2025-02-19T08:50:00Z"
  }
}
```

### Additional Information

- URL requests expire after 30 days
- All events logged
- Audit trail maintained
- Historical data preserved
- Real-time delivery
- Integration with:
  * Event system
  * Monitoring tools
  * Logging system
  * Analytics platform