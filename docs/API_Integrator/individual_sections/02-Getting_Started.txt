# Getting Started

The DRX External API allows easy data access for third party vendors and customers to interact with your pharmacy's DRX system programmatically.

## Authentication

To access a store's data via the DRX API, you must first obtain an API key from the store. A store can generate their own API key and transmit that to you, or they can contact the help desk for assistance in creating the key.

The DRX API key format looks like: DRX008ddfdd3d074930a77710707b0de0d5

Note: The pharmacy can revoke permissions and delete the key at any time. The DRX user performing this task must have the correct permission to do so.

## General Request Guidelines

All requests must include:
| Requirement | Value |
|---|---|
| Host | Will vary per store. Format: https://storeslug.drxapp.com |
| X-DRX-Key | API key in request header |
| URL Prefix | All URLs are prefixed with /external_api/v1/ |

Additional requirements:
- All requests must use SSL connection
- All responses are in JSON format
- Requests not properly authenticated will return a 401 error code

## Store Slug

The store slug is a URL-safe value containing only alphanumeric characters (a-z, 0-9). No spaces, underscores, or special characters are allowed.

- For testing: Contact DRX for a test environment store slug
- For production: Get the store slug and API key from the specific store

## Example Request

**cURL:**
```bash
curl --location --request GET 'https://<store_slug>.drxapp.com/external_api/v1/heartbeat' \
--header 'X-DRX-Key: DRXc41ea2a0caf44c88a71af9404df49d13'
```

**Python:**
```python
import requests

url = "https://<store_slug>.drxapp.com/external_api/v1/heartbeat"

headers = {
  'X-DRX-Key': 'DRXc41ea2a0caf44c88a71af9404df49d13'
}

response = requests.request("GET", url, headers=headers)

print(response.text)
```

**Response:**
```json
{
    "pulse": 166
}