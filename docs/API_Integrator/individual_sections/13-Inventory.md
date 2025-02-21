# Inventory

This section covers the endpoints related to managing and tracking inventory in the DRX API.

## Get All Inventory

Retrieve the current inventory status for all items.

### Endpoint

`GET /api/v2/inventory`

### Important Note

This endpoint is an exception to the normal pagination rules. It returns all items with either positive or negative balance on hand. Due to the comprehensive nature of the response, this endpoint may take several seconds to respond for stores with large inventory.

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| as_of_date | string | Optional date to see historical inventory (ISO 8601) |

### Response

#### Success Response (200 OK)

```json
{
  "items": [
    {
      "id": "itm_12345",
      "ndc": "12345-6789-10",
      "name": "Example Medication 10mg Tablet",
      "balance_on_hand": 500,
      "reorder_point": 100,
      "maximum_on_hand": 1000,
      "package_size": 100,
      "unit_of_measure": "EA",
      "last_count_date": "2025-02-01T00:00:00Z",
      "last_received_date": "2025-02-15T00:00:00Z",
      "last_dispensed_date": "2025-02-19T08:50:00Z",
      "on_order": 200,
      "pending_fills": 50,
      "location": "SHELF-A1",
      "status": "active"
    }
  ],
  "metadata": {
    "total_items": 1500,
    "total_value": 125000.00,
    "count_date": "2025-02-19T08:50:00Z"
  }
}
```

### Notes

- Response includes all items regardless of status
- Balance calculations include pending transactions
- Historical data available through as_of_date parameter
- Monetary values are in store's local currency

## Get Item Inventory History

Retrieve detailed inventory history for a specific item.

### Endpoint

`GET /api/v2/inventory/{item_id}/history`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| item_id | string | Unique identifier of the item |

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| start_date | string | Start of date range (ISO 8601) |
| end_date | string | End of date range (ISO 8601) |
| include_equivalents | boolean | Include equivalent items in history |

### Notes

- Default date range is last 14 days if not specified
- Response includes two arrays:
  1. Starting balances
  2. Individual inventory entries

### Response

#### Success Response (200 OK)

```json
{
  "starting_balances": [
    {
      "item_id": "itm_12345",
      "balance": 500,
      "date": "2025-02-05T00:00:00Z"
    }
  ],
  "entries": [
    {
      "id": "inv_67890",
      "item_id": "itm_12345",
      "type": "receipt",
      "quantity": 100,
      "balance_after": 600,
      "reference": "PO#12345",
      "notes": "Regular stock order",
      "user": "john.doe",
      "timestamp": "2025-02-05T10:30:00Z"
    },
    {
      "id": "inv_67891",
      "item_id": "itm_12345",
      "type": "dispense",
      "quantity": -30,
      "balance_after": 570,
      "reference": "RX#789012",
      "notes": "Regular prescription fill",
      "user": "jane.smith",
      "timestamp": "2025-02-05T14:15:00Z"
    }
  ],
  "metadata": {
    "item_details": {
      "ndc": "12345-6789-10",
      "name": "Example Medication 10mg Tablet",
      "package_size": 100,
      "unit_of_measure": "EA"
    },
    "date_range": {
      "start": "2025-02-05T00:00:00Z",
      "end": "2025-02-19T08:50:00Z"
    }
  }
}
```

### Entry Types

| Type | Description |
|------|-------------|
| receipt | Inventory received |
| dispense | Prescription fill |
| adjustment | Manual adjustment |
| return | Return to stock |
| transfer_in | Transfer from another location |
| transfer_out | Transfer to another location |
| cycle_count | Physical inventory count |

### Best Practices

1. Inventory Management
   - Regular cycle counts
   - Prompt recording of receipts
   - Accurate dispensing records
   - Proper adjustment documentation

2. Data Analysis
   - Monitor usage patterns
   - Track adjustments
   - Review discrepancies
   - Analyze trends

3. System Integration
   - Sync with ordering system
   - Connect to dispensing equipment
   - Link to point of sale
   - Interface with accounting

4. Error Prevention
   - Validate quantities
   - Check unit conversions
   - Verify package sizes
   - Monitor negative balances

### Additional Information

- Historical data retained indefinitely
- All transactions are logged
- Audit trail maintained
- System enforces data integrity
- Real-time balance updates