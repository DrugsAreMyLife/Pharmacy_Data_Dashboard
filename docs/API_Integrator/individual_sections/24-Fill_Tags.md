# Fill Tags

This section covers the endpoints related to managing prescription fill tags in the DRX API.

## Look Up a Fill Tag

Retrieve details for a specific fill tag.

### Endpoint

`GET /api/v2/fill-tags/{tag_id}`

### Response

#### Success Response (200 OK)

```json
{
  "id": "tag_12345",
  "name": "urgent",
  "description": "Priority processing required",
  "color": "#FF0000",
  "icon": "exclamation-circle",
  "active": true,
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-02-19T08:50:00Z",
  "metadata": {
    "priority_level": "high",
    "notification_required": true
  }
}
```

## Get a List of Fill Tags

Retrieve a list of fill tags with optional filtering.

### Endpoint

`GET /api/v2/fill-tags`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| offset | integer | Offset for pagination |
| limit | integer | Maximum records to return |
| name | string | Filter tags by name |
| fill_id | string | Filter tags by fill ID |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "tag_12345",
      "name": "urgent",
      "description": "Priority processing required",
      "color": "#FF0000",
      "icon": "exclamation-circle",
      "active": true
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

## Add Tags to a Fill

Associate one or more tags with a prescription fill.

### Endpoint

`POST /api/v2/fill-tags/add`

### Request Body

Array of objects, each containing:
| Field | Definition |
|-------|------------|
| prescription_fill_id | Fill Primary Key |
| tag_names | Array of tag names to add |

### Example Request

```json
[
  {
    "prescription_fill_id": "fill_12345",
    "tag_names": ["urgent", "refrigerate"]
  }
]
```

### Response

#### Success Response (200 OK)

```json
{
  "success": true,
  "updated_fills": [
    {
      "fill_id": "fill_12345",
      "added_tags": ["urgent", "refrigerate"],
      "current_tags": ["urgent", "refrigerate", "controlled"]
    }
  ]
}
```

## Remove Tags from Fills

Remove one or more tags from prescription fills.

### Endpoint

`DELETE /api/v2/fill-tags/remove`

### Request Body

Array of objects, each containing:
| Field | Definition |
|-------|------------|
| prescription_fill_id | Fill Primary Key |
| tag_names | Array of tag names to remove |

### Example Request

```json
[
  {
    "prescription_fill_id": "fill_12345",
    "tag_names": ["urgent"]
  }
]
```

### Response

#### Success Response (200 OK)

```json
{
  "success": true,
  "updated_fills": [
    {
      "fill_id": "fill_12345",
      "removed_tags": ["urgent"],
      "current_tags": ["refrigerate", "controlled"]
    }
  ]
}
```

## Common Tag Types

| Tag | Description | Impact |
|-----|-------------|---------|
| urgent | Priority processing | Moves to front of queue |
| refrigerate | Requires refrigeration | Special handling |
| controlled | Controlled substance | Additional verification |
| partial | Partial fill | Remaining quantity tracked |
| delivery | For delivery | Added to delivery queue |
| sync | Part of med sync | Coordinated fill date |

## Best Practices

1. Tag Management
   - Use consistent naming
   - Document tag purposes
   - Review tag usage
   - Archive unused tags

2. Fill Processing
   - Check tag requirements
   - Follow tag procedures
   - Update tags promptly
   - Verify tag removal

3. Workflow Integration
   - Automate tag assignment
   - Monitor tagged fills
   - Track tag history
   - Report on tag usage

4. System Configuration
   - Define standard tags
   - Set tag colors
   - Configure icons
   - Update tag rules

### Additional Information

- URL requests expire after 30 days
- All tag changes logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported
- Integration with:
  * Workflow system
  * Reporting tools
  * Notification system
  * Quality control