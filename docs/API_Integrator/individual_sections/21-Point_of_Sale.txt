# Point of Sale

This section covers the endpoints related to point of sale operations in the DRX API.

## Get a List of Sale Events

Retrieve a list of point of sale events.

### Endpoint

`GET /api/v2/pos/events`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Number of records to return |
| offset | integer | Offset for pagination |
| date | string | Filter by sale date (ISO 8601) |
| status | string | Filter by sale status |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "pos_12345",
      "status": "completed",
      "sub_total": 125.00,
      "tax": 10.00,
      "total": 135.00,
      "discounts": [
        {
          "type": "senior",
          "amount": 12.50
        }
      ],
      "credit_card_fee": 2.50,
      "remaining": 0.00,
      "sale_comment": "Regular pickup",
      "payment_method": "credit_card",
      "cashier": "john.doe",
      "created_at": "2025-02-19T08:50:00Z",
      "completed_at": "2025-02-19T08:55:00Z"
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

## Look Up a Sale Event

Retrieve details for a specific sale event.

### Endpoint

`GET /api/v2/pos/events/{event_id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| event_id | string | Primary key of the sale event |

### Response

#### Success Response (200 OK)

```json
{
  "id": "pos_12345",
  "status": "completed",
  "items": [
    {
      "id": "itm_67890",
      "name": "Example Medication 10mg Tablet",
      "quantity": 30,
      "price": 125.00,
      "prescription_id": "rx_11111"
    }
  ],
  "payments": [
    {
      "method": "credit_card",
      "amount": 135.00,
      "reference": "txn_98765",
      "timestamp": "2025-02-19T08:53:00Z"
    }
  ],
  "sub_total": 125.00,
  "tax": 10.00,
  "total": 135.00,
  "created_at": "2025-02-19T08:50:00Z",
  "completed_at": "2025-02-19T08:55:00Z"
}
```

## Look Up a Barcode

Retrieve information about a scanned prescription barcode.

### Endpoint

`GET /api/v2/pos/barcode/{barcode}`

### Barcode Format Details

- Every prescription label includes a 1D barcode
- Format: `<bottle_or_label_flag:len(1)><prescription_fill_id:len(varies)><delimiter:(:)><label_version:len(varies)>`
- Example: 'b209827:a5g'
- Components:
  * Bottle/label flag: Indicates prescription bottle or paper label
  * Fill ID: Primary key for specific prescription fill
  * Delimiter: Always a colon
  * Version: Alphanumeric string (typically 3 characters)

### Response

#### Success Response (200 OK)

```json
{
  "prescription_fill": {
    "id": "fill_12345",
    "prescription_id": "rx_67890",
    "status": "ready",
    "quantity": 30,
    "price": 125.00,
    "patient": {
      "id": "pat_11111",
      "name": "John Doe"
    },
    "medication": {
      "name": "Example Medication 10mg Tablet",
      "ndc": "12345-6789-10"
    }
  }
}
```

## Send a Sale Event to DRX

Record a completed sale event.

### Endpoint

`POST /api/v2/pos/events`

### Important Notes

- Events are processed asynchronously
- All requests return 200 status initially
- Validation occurs after HTTP response
- Design allows for:
  * Third-party monitoring
  * Event replay if issues detected
  * Vendor-specific input variations

### Request Body

| Field | Type | Description |
|-------|------|-------------|
| items | array | List of items sold |
| payments | array | List of payments received |
| sub_total | number | Pre-tax total |
| tax | number | Tax amount |
| total | number | Final total |
| payment_method | string | Primary payment method |
| sale_comment | string | Optional notes |

### Example Request

```json
{
  "items": [
    {
      "prescription_fill_id": "fill_12345",
      "quantity": 30,
      "price": 125.00
    }
  ],
  "payments": [
    {
      "method": "credit_card",
      "amount": 135.00,
      "reference": "txn_98765"
    }
  ],
  "sub_total": 125.00,
  "tax": 10.00,
  "total": 135.00,
  "payment_method": "credit_card",
  "sale_comment": "Regular pickup"
}
```

## Edit a Point of Sale Event

Update an existing sale event.

### Endpoint

`PATCH /api/v2/pos/events/{event_id}`

### Editable Fields

| Field | Description |
|-------|-------------|
| sub_total | Subtotal amount |
| tax | Tax amount |
| total | Total amount |
| discounts | Discount amounts |
| credit_card_fee | Processing fee |
| remaining | Remaining balance |
| sale_comment | Sale notes |
| status | Event status |

## Click 2 Pay

Process a Click 2 Pay transaction.

### Endpoint

`POST /api/v2/pos/click2pay/{event_id}`

### Response

Returns payment processing status and transaction details.

## Best Practices

1. Transaction Processing
   - Validate amounts
   - Verify prescriptions
   - Check payment methods
   - Handle refunds properly

2. Barcode Handling
   - Validate format
   - Check checksums
   - Handle duplicates
   - Track scans

3. Event Management
   - Monitor async processing
   - Track event status
   - Handle failures
   - Maintain audit trail

4. Payment Processing
   - Secure transactions
   - Validate amounts
   - Handle declines
   - Process refunds

### Additional Information

- URL requests expire after 30 days
- All transactions logged
- Audit trail maintained
- Real-time updates supported
- Integration with accounting system