# Images

This section covers the endpoints related to managing images in the DRX API.

## Get an Image

Retrieve an image associated with a specific record type and ID.

### Endpoint

`GET /api/v2/images/{type}/{id}`

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| type | string | Type of record the image is associated with |
| id | string | Unique identifier for the record |

### Valid Types

| Type | Description |
|------|-------------|
| pos_event | Images associated with a sale ID |
| prescription | Images associated with a prescription |
| patient | Images associated with a patient |
| delivery | Images associated with a delivery |

### Response

#### Success Response (200 OK)

```json
{
  "images": [
    {
      "id": "img_12345",
      "name": "prescription_scan.jpg",
      "type": "prescription",
      "content_type": "image/jpeg",
      "size": 256000,
      "url": "https://example.com/images/prescription_scan.jpg",
      "created_at": "2025-02-19T08:50:00Z",
      "metadata": {
        "width": 1200,
        "height": 1600,
        "dpi": 300
      }
    }
  ]
}
```

#### Error Responses

- 400 Bad Request: Invalid type or ID
- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Image not found

### Notes

- Some records may have multiple associated images
- Response will be an array of all images for the record
- Images are returned as URLs with temporary access tokens
- URLs expire after 24 hours

## Add an Image

Upload and associate a new image with a record in the system.

### Endpoint

`POST /api/v2/images`

### Request Body

| Field | Description |
|-------|-------------|
| image_data | Base64 encoded image data |
| name | Name of the image |
| patient_id | Link to Patient (optional) |
| user_id | Link to User (optional) |
| item_id | Link to Item (optional) |
| pos_event_id | Link to POS Event (optional) |
| compound_batch_id | Link to Compound Batch (optional) |
| delivery_id | Link to Delivery (optional) |
| created_on | Time image was created (DateTime) |

### Example Request

```json
{
  "image_data": "base64_encoded_image_data_here",
  "name": "prescription_front.jpg",
  "patient_id": "pat_12345",
  "created_on": "2025-02-19T08:50:00Z"
}
```

### Response

#### Success Response (201 Created)

```json
{
  "id": "img_12345",
  "name": "prescription_front.jpg",
  "url": "https://example.com/images/prescription_front.jpg",
  "content_type": "image/jpeg",
  "size": 256000,
  "created_at": "2025-02-19T08:50:00Z",
  "metadata": {
    "width": 1200,
    "height": 1600,
    "dpi": 300
  }
}
```

#### Error Responses

- 400 Bad Request: Invalid image data or parameters
- 401 Unauthorized: Invalid or missing API key
- 413 Payload Too Large: Image exceeds size limit
- 415 Unsupported Media Type: Invalid image format

### Supported Image Formats

- JPEG/JPG
- PNG
- TIFF
- BMP
- PDF (first page will be converted to image)

### Size Limits

- Maximum file size: 10MB
- Maximum dimensions: 4000x4000 pixels
- Minimum dimensions: 300x300 pixels

### Best Practices

1. Image Quality
   - Use appropriate resolution for intended use
   - Maintain aspect ratios
   - Consider file size vs. quality
   - Use compression when appropriate

2. Organization
   - Use descriptive file names
   - Add relevant metadata
   - Link to appropriate records
   - Maintain consistent naming conventions

3. Security
   - Validate file types
   - Scan for malware
   - Use secure transmission
   - Monitor access patterns

4. Performance
   - Optimize image sizes
   - Cache frequently accessed images
   - Use appropriate formats
   - Consider bandwidth limitations

### Additional Information

- Images are stored securely
- Backup copies are maintained
- Access is logged for audit purposes
- Original files are preserved
- Automatic image optimization available