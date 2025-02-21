# Store Management

This section covers the endpoints related to managing store settings and information in the DRX API.

## Get Store Settings

Retrieve store settings including operating hours and delivery methods.

### Endpoint

`GET /api/v2/stores/settings`

### Response

#### Success Response (200 OK)

```json
{
  "store": {
    "id": "str_12345",
    "name": "Example Pharmacy",
    "npi": "1234567890",
    "ncpdp": "1234567",
    "address": {
      "street": "123 Main St",
      "city": "Austin",
      "state": "TX",
      "zip": "78701"
    },
    "phone": "5551234567",
    "fax": "5551234568",
    "email": "pharmacy@example.com",
    "timezone": "America/Chicago"
  },
  "hours": {
    "monday": {
      "open": 800,
      "close": 2000,
      "closed": false
    },
    "tuesday": {
      "open": 800,
      "close": 2000,
      "closed": false
    },
    "wednesday": {
      "open": 800,
      "close": 2000,
      "closed": false
    },
    "thursday": {
      "open": 800,
      "close": 2000,
      "closed": false
    },
    "friday": {
      "open": 800,
      "close": 2000,
      "closed": false
    },
    "saturday": {
      "open": 900,
      "close": 1700,
      "closed": false
    },
    "sunday": {
      "closed": true
    }
  },
  "delivery": {
    "methods": {
      "pickup": {
        "enabled": true,
        "fee": 0.00
      },
      "delivery": {
        "enabled": true,
        "fee": 5.00,
        "minimum_order": 25.00,
        "radius_miles": 10
      },
      "shipping": {
        "enabled": true,
        "carriers": ["ups", "usps", "fedex"]
      }
    },
    "cutoff_time": 1600,
    "same_day_enabled": true,
    "blackout_dates": [
      "2025-12-25",
      "2026-01-01"
    ]
  },
  "preferences": {
    "auto_refill_enabled": true,
    "med_sync_enabled": true,
    "notification_methods": ["sms", "email", "voice"],
    "default_notification": "sms",
    "prescription_expiry_warning_days": 30,
    "refill_reminder_days": 7
  }
}
```

### Notes

- Hours are in store's local timezone
- Times expressed as 24-hour integer values (800 = 8:00 AM)
- Days of week represented as full names
- All monetary values in USD

## Get a List of Stores

Retrieve a list of all stores in the system.

### Endpoint

`GET /api/v2/stores`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Records to return |
| offset | integer | Offset for pagination |
| state | string | Filter by state |
| active | boolean | Filter by active status |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "str_12345",
      "name": "Example Pharmacy",
      "npi": "1234567890",
      "ncpdp": "1234567",
      "address": {
        "street": "123 Main St",
        "city": "Austin",
        "state": "TX",
        "zip": "78701"
      },
      "phone": "5551234567",
      "status": "active",
      "timezone": "America/Chicago"
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

## Best Practices

1. Store Configuration
   - Validate hours format
   - Check timezone settings
   - Verify delivery options
   - Monitor preferences

2. Hours Management
   - Handle special hours
   - Track holidays
   - Update seasonal changes
   - Monitor cutoff times

3. Delivery Settings
   - Validate service areas
   - Update fee structures
   - Check carrier options
   - Monitor blackout dates

4. System Integration
   - Sync with POS
   - Update delivery system
   - Connect notification services
   - Maintain preferences

### Additional Information

- URL requests expire after 30 days
- All updates are logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported
- Integration with:
  * POS system
  * Delivery services
  * Notification system
  * Scheduling system