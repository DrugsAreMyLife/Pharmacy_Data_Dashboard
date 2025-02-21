# Items

This section covers the endpoints related to managing items in the DRX API.

## Look Up an Item

Retrieve detailed information about a specific item.

### Important Note for Central Site Stores

If you are accessing this API against a store that is in a group of central site stores (shared database), the primary key for the same NDC will be different for each store.

Example:
- Omeprazole 40 MG
  - Store A: NDC = 99988222211, Primary Key = 61
  - Store B: NDC = 99988222211, Primary Key = 7817

When looking up an item:
- By NDC: DRX will pull the correct item based on the store slug in the hostname
- By Primary Key: Item must belong to the store whose endpoint you're using

### Endpoint

`GET /api/v2/items/{identifier}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| identifier | string | NDC, UPC, or Primary Key |

### Response

#### Success Response (200 OK)

```json
{
  "id": "itm_12345",
  "ndc": "12345-6789-10",
  "upc": "123456789012",
  "name": "Example Medication 10mg Tablet",
  "manufacturer": "Example Pharma",
  "package_size": 100,
  "unit_of_measure": "EA",
  "strength": "10mg",
  "form": "tablet",
  "controlled_substance": false,
  "schedule": null,
  "refrigerated": false,
  "hazardous": false,
  "use_equivalents_for_ordering": true,
  "respect_package_size": false,
  "reorder_point": 100,
  "maximum_on_hand": 1000,
  "balance_on_hand": 500,
  "average_cost": 1.50,
  "retail_price": 3.00,
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

## Get a List of Items

Retrieve a list of items with optional filtering.

### Endpoint

`GET /api/v2/items`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| limit | integer | Number of records to return |
| ndc | string | Filter by NDC (partial matches supported) |
| gcn | string | Filter by GCN Code (exact match only) |
| item_type | string | Filter by item type |

### Response

#### Success Response (200 OK)

```json
{
  "data": [
    {
      "id": "itm_12345",
      "ndc": "12345-6789-10",
      "name": "Example Medication 10mg Tablet",
      "manufacturer": "Example Pharma",
      "balance_on_hand": 500
    }
  ],
  "pagination": {
    "total_items": 1500,
    "total_pages": 75,
    "current_page": 1,
    "per_page": 20,
    "next_page": 2,
    "prev_page": null
  }
}
```

## Import from FDB Catalog

Import an item from the First Databank catalog using UPC or NDC.

### Endpoint

`GET /api/v2/items/import`

### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| identifier | string | Item UPC or NDC (Required) |
| supplier_id | string | Optional Supplier Primary Key |

### Response

#### Success Response (200 OK)

Returns the newly imported item object.

## Update Reorder Points

Update minimum and maximum stock levels for an item.

### Endpoint

`POST /api/v2/items/{identifier}/reorder-points`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| identifier | string | NDC, UPC, or ID of item |

### Request Body

| Parameter | Type | Description |
|-----------|------|-------------|
| minimum | integer | Minimum to keep on hand |
| maximum | integer | Maximum to keep on hand |

### Notes on Ordering Groups

DRX has three different ordering "groupings":

1. Plain Item
   - Balance considers only this specific item
   - Used when store wants to maintain specific item stock

2. Equivalents for Reordering
   - Considers all equivalent items
   - Example: All manufacturers of Atorvastatin 40MG

3. Equivalents with Stock Size
   - Uses equivalents but respects package size
   - Example: Atorvastatin 40MG PKG 1000 vs PKG 100

Group determination:
```json
{
  "use_equivalents_for_ordering": true,
  "respect_package_size": false
}
```
- Both false: Group 1
- Equivalents true, size false: Group 2
- Both true: Group 3

## Update Equivalents for Reordering

Update the ordering grouping configuration for an item.

### Endpoint

`POST /api/v2/items/{identifier}/equivalents`

### Request Body

```json
{
  "use_equivalents_for_ordering": true,
  "respect_package_size": false
}
```

### Important Note

The configuration where:
```json
{
  "use_equivalents_for_ordering": false,
  "respect_package_size": true
}
```
is invalid. DRX will set both to false if use_equivalents_for_ordering is false.

## Update Balance on Hand

Update the current inventory balance for an item.

### Endpoint

`POST /api/v2/items/{identifier}/balance`

### Request Body

| Parameter | Type | Description |
|-----------|------|-------------|
| new_boh | number | New Balance On Hand value |
| reason | string | Description for the BOH change |

### Best Practices

1. Item Management
   - Maintain accurate NDC/UPC data
   - Review equivalent groupings regularly
   - Monitor reorder points
   - Document balance adjustments

2. Inventory Control
   - Regular cycle counts
   - Accurate receiving
   - Proper adjustment documentation
   - Monitor stock levels

3. Data Quality
   - Validate identifiers
   - Check package sizes
   - Verify unit costs
   - Update prices regularly

4. System Integration
   - Sync with ordering system
   - Connect to point of sale
   - Link to dispensing equipment
   - Interface with accounting

### Additional Information

- URL requests expire after 30 days
- All updates are logged
- Audit trail maintained
- Historical data preserved
- Real-time balance updates