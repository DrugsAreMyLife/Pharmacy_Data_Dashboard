---
## DRX_API_Documentation_Guide.md
---

> **Note:** Use the clickable links below to jump directly to each section. The internal anchors were formed by converting each heading into an HTML/Markdown-compatible slug (lowercase, hyphenated). Everything else is preserved verbatim from the original document.

---

# **CLICKABLE SECTIONS INDEX**

1. [DRX API Documentation Introduction](#drx-api-documentation-introduction)  
   1.1 [Table of Contents (Original Listing)](#table-of-contents-original-listing)  
   1.2 [API Endpoints (Overview)](#api-endpoints-overview)

2. [Getting Started](#getting-started)  
   2.1 [Authentication](#authentication)  
   2.2 [General Request Guidelines](#general-request-guidelines)  
   2.3 [Store Slug](#store-slug)  
   2.4 [Example Request](#example-request)

3. [Changes to the API](#changes-to-the-api)  
   3.1 [Additional Notes on Evolving Fields](#additional-notes-on-evolving-fields)  

4. [Getting Started with DRX (Additional Section)](#getting-started-with-drx-additional-section)  
   4.1 [Introduction](#introduction)  
   4.2 [Authentication (DRX v2)](#authentication-drx-v2)  
   4.3 [Base URL](#base-url)  
   4.4 [API Versioning](#api-versioning)  
   4.5 [Request Format](#request-format)  
   4.6 [Response Format](#response-format)  
   4.7 [Rate Limiting](#rate-limiting)  
   4.8 [Best Practices](#best-practices)  
   4.9 [Testing](#testing)  
   4.10 [Support](#support)  
   4.11 [Next Steps](#next-steps)

5. [Example Data](#example-data)  
   5.1 [Address Object](#address-object)  
   5.2 [User Object](#user-object)  
   5.3 [Order Object](#order-object)  
   5.4 [Error Response](#error-response)  
   5.5 [Pagination Response](#pagination-response)  
   5.6 [Common Fields](#common-fields)  
   5.7 [Data Types](#data-types)

6. [Dates, Times, and Timezones](#dates-times-and-timezones)  
   6.1 [Date and Time Format](#date-and-time-format)  
   6.2 [Timezone Handling](#timezone-handling)  
   6.3 [Examples](#examples)  
   6.4 [Best Practices (Date/Time)](#best-practices-datetime)  
   6.5 [Date-Only Fields](#date-only-fields)  
   6.6 [Time Ranges](#time-ranges)  
   6.7 [Common Issues](#common-issues)

7. [Changes to the API (Additional Details)](#changes-to-the-api-additional-details)  
   7.1 [API Version Updates](#api-version-updates)  
   7.2 [Breaking Changes](#breaking-changes)  
   7.3 [Deprecation Notices](#deprecation-notices)  
   7.4 [Changelog Access](#changelog-access)  
   7.5 [Best Practices (Changes)](#best-practices-changes)

8. [Addresses](#addresses)  
   8.1 [Look Up an Address](#look-up-an-address)  
   8.2 [Get a List of Addresses](#get-a-list-of-addresses)  
   8.3 [Edit an Address](#edit-an-address)  
   8.4 [Add an Address](#add-an-address)

9. [Allergies](#allergies)  
   9.1 [Look Up an Allergy](#look-up-an-allergy)  
   9.2 [Get a List of Allergies](#get-a-list-of-allergies)  
   9.3 [Add an Allergy to a Patient](#add-an-allergy-to-a-patient)

10. [Charge Accounts](#charge-accounts)  
    10.1 [Look Up a Charge Account](#look-up-a-charge-account)  
    10.2 [Get a List of Charge Accounts](#get-a-list-of-charge-accounts)

11. [Claims](#claims)  
    11.1 [Look Up a Claim](#look-up-a-claim)  
    11.2 [Get a List of Claims](#get-a-list-of-claims)

12. [Deliveries](#deliveries)  
    12.1 [Get a List of Deliveries](#get-a-list-of-deliveries)  
    12.2 [Get a List of Delivery Routes](#get-a-list-of-delivery-routes)  
    12.3 [Look Up a Delivery](#look-up-a-delivery)  
    12.4 [Edit a Delivery](#edit-a-delivery)

13. [Doctors](#doctors)  
    13.1 [Look Up a Doctor](#look-up-a-doctor)  
    13.2 [Get a List of Doctors](#get-a-list-of-doctors)  
    13.3 [Search Provider Catalog](#search-provider-catalog)  
    13.4 [Add a Doctor](#add-a-doctor)

14. [Eligibility](#eligibility)  
    14.1 [Real Time Eligibility Check](#real-time-eligibility-check)

15. [Inventory](#inventory)  
    15.1 [Get All Inventory](#get-all-inventory)  
    15.2 [Get Item Inventory History](#get-item-inventory-history)

16. [Images](#images)  
    16.1 [Get an Image](#get-an-image)  
    16.2 [Add an Image](#add-an-image)

17. [Items](#items)  
    17.1 [Look Up an Item](#look-up-an-item)  
    17.2 [Get a List of Items](#get-a-list-of-items)  
    17.3 [Import from FDB Catalog](#import-from-fdb-catalog)  
    17.4 [Update Reorder Points](#update-reorder-points)  
    17.5 [Update Equivalents for Reordering](#update-equivalents-for-reordering)  
    17.6 [Update Balance on Hand](#update-balance-on-hand)

18. [Packing Lists](#packing-lists)  
    18.1 [Get a List of Packing Lists](#get-a-list-of-packing-lists)  
    18.2 [Get All Prescription Fills on Packing List](#get-all-prescription-fills-on-packing-list)

19. [Partners](#partners)  
    19.1 [Commands](#commands)  
    19.2 [Data Dump Example](#data-dump-example)

20. [Patients](#patients)  
    20.1 [Look Up a Patient](#look-up-a-patient)  
    20.2 [Get a List of Patients](#get-a-list-of-patients)  
    20.3 [Add a Patient](#add-a-patient)  
    20.4 [Edit a Patient](#edit-a-patient)  
    20.5 [Get a List of Charge Accounts](#get-a-list-of-charge-accounts)  
    20.6 [Look Up a Patient Profile](#look-up-a-patient-profile)  
    20.7 [Get a Patient's Sync List](#get-a-patients-sync-list)

21. [Patient Match](#patient-match)  
    21.1 [Find a Match](#find-a-match)

22. [Phone Numbers](#phone-numbers)  
    22.1 [Look Up a Phone Number](#look-up-a-phone-number)  
    22.2 [Get a List of Phone Numbers](#get-a-list-of-phone-numbers)  
    22.3 [Add a Phone Number](#add-a-phone-number)  
    22.4 [Edit a Phone Number](#edit-a-phone-number)

23. [Point of Sale](#point-of-sale)  
    23.1 [Get a List of Sale Events](#get-a-list-of-sale-events)  
    23.2 [Look Up a Sale Event](#look-up-a-sale-event)  
    23.3 [Look Up a Barcode](#look-up-a-barcode)  
    23.4 [Send a Sale Event to DRX](#send-a-sale-event-to-drx)  
    23.5 [Edit a Point of Sale Event](#edit-a-point-of-sale-event)  
    23.6 [Click 2 Pay](#click-2-pay)

24. [Prescriptions](#prescriptions)  
    24.1 [Get a List of Prescriptions](#get-a-list-of-prescriptions)  
    24.2 [Look Up a Prescription](#look-up-a-prescription)  
    24.3 [Send Hard Copy Image to Intake for Processing](#send-hard-copy-image-to-intake-for-processing)  
    24.4 [Generate an E-Script (Deprecated)](#generate-an-e-script-prescription-order-deprecated)  
    24.5 [Generate a Prescription](#generate-a-prescription)  
    24.6 [Inactivate Prescription](#inactivate-prescription)  
    24.7 [Reactivate Prescription](#reactivate-prescription)

25. [Prescription Fills](#prescription-fills)  
    25.1 [Get a List of Prescription Fills](#get-a-list-of-prescription-fills)  
    25.2 [Look Up a Prescription Fill](#look-up-a-prescription-fill)  
    25.3 [Send Fill to Vial Dispensing Robot](#send-fill-to-vial-dispensing-robot)  
    25.4 [Reverse Paid Claims](#reverse-paid-claims)  
    25.5 [Add Bin Location](#add-bin-location)  
    25.6 [Set Fill Status](#set-fill-status)

26. [Fill Tags](#fill-tags)  
    26.1 [Look Up a Fill Tag](#look-up-a-fill-tag)  
    26.2 [Get a List of Fill Tags](#get-a-list-of-fill-tags)  
    26.3 [Add Tags to a Fill](#add-tags-to-a-fill)  
    26.4 [Remove Tags from Fills](#remove-tags-from-fills)

27. [SureScripts](#surescripts)  
    27.1 [Look Up a SureScript](#look-up-a-surescript)  
    27.2 [Get a List of SureScripts (Intake Queue)](#get-a-list-of-surescripts-intake-queue)  
    27.3 [Generate SureScript](#generate-surescript)  
    27.4 [Cancel Message](#cancel-message)  
    27.5 [Delete a SureScript from the Intake Queue](#delete-a-surescript-from-the-intake-queue)  
    27.6 [Edit Intake Item](#edit-intake-item)

28. [Refills and Renewals](#refills-and-renewals)  
    28.1 [Send a Refill Request](#send-a-refill-request)  
    28.2 [Send in a Renewal](#send-in-a-renewal)

29. [Store Management](#store-management)  
    29.1 [Get Store Settings](#get-store-settings)  
    29.2 [Get a List of Stores](#get-a-list-of-stores)

30. [Shipping](#shipping)  
    30.1 [Get a List of Past Shipments](#get-a-list-of-past-shipments)  
    30.2 [Get Shipping Rates](#get-shipping-rates)  
    30.3 [Generate Label](#generate-label)

31. [SMS](#sms)  
    31.1 [Send SMS](#send-sms)

32. [Tasks](#tasks)  
    32.1 [Get Task Status Updates](#get-task-status-updates)  
    32.2 [Start a New Task](#start-a-new-task)

33. [Third Party](#third-party)  
    33.1 [Add a Third Party](#add-a-third-party)

34. [Transfers](#transfers)  
    34.1 [Look Up a Competing Pharmacy](#look-up-a-competing-pharmacy)  
    34.2 [Get a List of Competing Pharmacies](#get-a-list-of-competing-pharmacies)  
    34.3 [Add a Competing Pharmacy](#add-a-competing-pharmacy)  
    34.4 [Send a Transfer Out](#send-a-transfer-out)

35. [Webhooks](#webhooks)  
    35.1 [Look Up a Webhook](#look-up-a-webhook)  
    35.2 [Get a List of Webhooks](#get-a-list-of-webhooks)  
    35.3 [Add a Webhook](#add-a-webhook)  
    35.4 [Delete a Webhook](#delete-a-webhook)

---

# **DRX API Documentation Introduction**

```markdown
# DRX API Documentation
```

## Table of Contents (Original Listing)

```markdown
## Table of Contents

1. [Getting Started](#getting-started)
2. [Changes to the API](#changes-to-the-api)

### API Endpoints

#### Address
- [Look Up an Address](#look-up-an-address)
- [Get a List of Addresses](#get-a-list-of-addresses)
- [Edit an Address](#edit-an-address)
- [Add an Address](#add-an-address)

#### Allergy
- [Look Up an Allergy](#look-up-an-allergy)
- [Get a List of Allergies](#get-a-list-of-allergies)
- [Add an Allergy to a Patient](#add-an-allergy-to-a-patient)

#### Charge Accounts
- [Look Up a Charge Account](#look-up-a-charge-account)
- [Get a List of Charge Accounts](#get-a-list-of-charge-accounts)

#### Claims
- [Look Up a Claim](#look-up-a-claim)
- [Get a List of Claims](#get-a-list-of-claims)

#### Deliveries
- [Get a List of Deliveries](#get-a-list-of-deliveries)
- [Get a List of Delivery Routes](#get-a-list-of-delivery-routes)
- [Look Up a Delivery](#look-up-a-delivery)
- [Edit a Delivery](#edit-a-delivery)

#### Doctors
- [Look Up a Doctor](#look-up-a-doctor)
- [Get a List of Doctors](#get-a-list-of-doctors)
- [Search Provider Catalog](#search-provider-catalog)
- [Add a Doctor](#add-a-doctor)

#### Eligibility
- [Real Time Eligibility Check](#real-time-eligibility-check)

#### Inventory
- [Get All Inventory](#get-all-inventory)
- [Get Item Inventory History](#get-item-inventory-history)

#### Images
- [Get an Image](#get-an-image)
- [Add an Image](#add-an-image)

#### Items
- [Look Up an Item](#look-up-an-item)
- [Get a List of Items](#get-a-list-of-items)
- [Import from FDB Catalog](#import-from-fdb-catalog)
- [Update Reorder Points](#update-reorder-points)
- [Update Equivalents for Reordering](#update-equivalents-for-reordering)
- [Update Balance on Hand](#update-balance-on-hand)

#### Packing Lists
- [Get a List of Packing Lists](#get-a-list-of-packing-lists)
- [Get All Prescription Fills on Packing List](#get-all-prescription-fills-on-packing-list)

#### Patients
- [Look Up a Patient](#look-up-a-patient)
- [Get a List of Patients](#get-a-list-of-patients)
- [Add a Patient](#add-a-patient)
- [Edit a Patient](#edit-a-patient)
- [Find a Match](#find-a-match)
- [Look Up a Patient Profile](#look-up-a-patient-profile)
- [Get a Patient's Sync List](#get-a-patients-sync-list)

#### Phone Numbers
- [Look Up a Phone Number](#look-up-a-phone-number)
- [Get a List of Phone Numbers](#get-a-list-of-phone-numbers)
- [Add a Phone Number](#add-a-phone-number)
- [Edit a Phone Number](#edit-a-phone-number)

#### Point of Sale
- [Get a List of Sale Events](#get-a-list-of-sale-events)
- [Look Up a Sale Event](#look-up-a-sale-event)
- [Look Up a Barcode](#look-up-a-barcode)
- [Send a Sale Event to DRX](#send-a-sale-event-to-drx)
- [Edit a Point of Sale Event](#edit-a-point-of-sale-event)
- [Click 2 Pay](#click-2-pay)

#### Prescriptions
- [Get a List of Prescriptions](#get-a-list-of-prescriptions)
- [Look Up a Prescription](#look-up-a-prescription)
- [Send Hard Copy Image to Intake](#send-hard-copy-image-to-intake-for-processing)
- [Generate an E-Script](#generate-an-e-script-prescription-order)
- [Generate a Prescription](#generate-a-prescription)
- [Inactivate Prescription](#inactivate-prescription)
- [Reactivate Prescription](#reactivate-prescription)

#### Prescription Fills
- [Get a List of Prescription Fills](#get-a-list-of-prescription-fills)
- [Look Up a Prescription Fill](#look-up-a-prescription-fill)
- [Send Fill to Vial Dispensing Robot](#send-fill-to-vial-dispensing-robot)
- [Reverse Paid Claims](#reverse-paid-claims)
- [Add Bin Location](#add-bin-location)
- [Set Fill Status](#set-fill-status)

#### Fill Tags
- [Look Up a Fill Tag](#look-up-a-fill-tag)
- [Get a List of Fill Tags](#get-a-list-of-fill-tags)
- [Add Tags to a Fill](#add-tags-to-a-fill)
- [Remove Tags from Fills](#remove-tags-from-fills)

#### SureScripts
- [Look Up a SureScript](#look-up-a-surescript)
- [Get a List of SureScripts](#get-a-list-of-surescripts-intake-queue)
- [Generate SureScript](#generate-surescript)
- [Cancel Message](#cancel-message)
- [Delete a SureScript](#delete-a-surescript-from-the-intake-queue)
- [Edit Intake Item](#edit-intake-item)

#### Refills and Renewals
- [Send a Refill Request](#send-a-refill-request)
- [Send in a Renewal](#send-in-a-renewal)

#### Store Management
- [Get Store Settings](#get-store-settings)
- [Get a List of Stores](#get-a-list-of-stores)

#### Shipping
- [Get a List of Past Shipments](#get-a-list-of-past-shipments)
- [Get Shipping Rates](#get-shipping-rates)
- [Generate Label](#generate-label)

#### SMS
- [Send SMS](#send-sms)

#### Tasks
- [Get Task Status Updates](#get-task-status-updates)
- [Start a New Task](#start-a-new-task)

#### Third Party
- [Add a Third Party](#add-a-third-party)

#### Transfers
- [Look Up a Competing Pharmacy](#look-up-a-competing-pharmacy)
- [Get a List of Competing Pharmacies](#get-a-list-of-competing-pharmacies)
- [Add a Competing Pharmacy](#add-a-competing-pharmacy)
- [Send a Transfer Out](#send-a-transfer-out)

#### Webhooks
- [Look Up a Webhook](#look-up-a-webhook)
- [Get a List of Webhooks](#get-a-list-of-webhooks)
- [Add a Webhook](#add-a-webhook)
- [Delete a Webhook](#delete-a-webhook)
```

## API Endpoints (Overview)

```markdown
### API Endpoints

#### Address
- [Look Up an Address](#look-up-an-address)
- [Get a List of Addresses](#get-a-list-of-addresses)
- [Edit an Address](#edit-an-address)
- [Add an Address](#add-an-address)

#### Allergy
- [Look Up an Allergy](#look-up-an-allergy)
- [Get a List of Allergies](#get-a-list-of-allergies)
- [Add an Allergy to a Patient](#add-an-allergy-to-a-patient)

...
```
*(The original “API Endpoints” overview list is duplicated above. The full expansions follow in later sections.)*

---

# **Getting Started**

```markdown
## Getting Started

The DRX External API allows easy data access for third party vendors and customers to interact with your pharmacy's DRX system programmatically.

### Authentication

To access a store's data via the DRX API, you must first obtain an API key from the store. A store can generate their own API key and transmit that to you, or they can contact the help desk for assistance in creating the key.

The DRX API key format looks like: DRX008ddfdd3d074930a77710707b0de0d5

Note: The pharmacy can revoke permissions and delete the key at any time. The DRX user performing this task must have the correct permission to do so.

### General Request Guidelines

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

### Store Slug

The store slug is a URL-safe value containing only alphanumeric characters (a-z, 0-9). No spaces, underscores, or special characters are allowed.

- For testing: Contact DRX for a test environment store slug
- For production: Get the store slug and API key from the specific store

### Example Request

**cURL:**
bash
curl --location --request GET 'https://<store_slug>.drxapp.com/external_api/v1/heartbeat' \
--header 'X-DRX-Key: DRXc41ea2a0caf44c88a71af9404df49d13'

**Python:**
python
import requests

url = "https://<store_slug>.drxapp.com/external_api/v1/heartbeat"

headers = {
  'X-DRX-Key': 'DRXc41ea2a0caf44c88a71af9404df49d13'
}

response = requests.request("GET", url, headers=headers)

print(response.text)

**Response:**
json
{
    "pulse": 166
}
```

# **Changes to the API**

```markdown
## Changes to the API

The API may evolve over time, with new fields being added to responses. For example, a response might initially look like:

json
{
  "success": true,
  "item_id": 1,
  "item_name": "Cheez-its"
}

And later be expanded to include additional fields:

json
{
  "success": true,
  "item_id": 1,
  "item_name": "Cheez-its",
  "manufacturer": "Nabisco",
  "price_history": [
     {
       "price": 1.00
     }
  ]
}

Your code should be designed to handle such additions gracefully.
```

---

# **Getting Started with DRX (Additional Section)**

```markdown
## Getting Started with DRX

### Introduction

Welcome to the DRX API documentation. This guide will help you get started with integrating DRX services into your application.

### Authentication

All API requests require authentication using an API key. Include your API key in the request header:

Authorization: Bearer your-api-key-here

To obtain an API key:
1. Register for a DRX developer account
2. Navigate to the API Keys section in your dashboard
3. Generate a new API key
4. Store the key securely - it won't be shown again

### Base URL

All API endpoints are accessed from the base URL:

https://api.drx.com/v2

### API Versioning

The current API version is v2. Include the version in the URL path:

https://api.drx.com/v2/endpoint

### Request Format

- Use HTTPS for all requests
- Send data in JSON format
- Set Content-Type header to application/json
- Include API key in Authorization header

Example request:
bash
curl -X POST \
  https://api.drx.com/v2/addresses \
  -H 'Authorization: Bearer your-api-key-here' \
  -H 'Content-Type: application/json' \
  -d '{
    "street_1": "123 Main St",
    "city": "Austin",
    "state": "TX"
  }'

### Response Format

All responses are in JSON format and include:
- HTTP status code
- Response body
- Error details (if applicable)

Success response example:
json
{
  "data": {
    "id": "addr_12345",
    "street_1": "123 Main St",
    "city": "Austin",
    "state": "TX"
  }
}

Error response example:
json
{
  "error": {
    "code": "invalid_request",
    "message": "Missing required field: postal_code"
  }
}

### Rate Limiting

- 1000 requests per minute per API key
- Rate limit headers included in responses:
  - X-RateLimit-Limit
  - X-RateLimit-Remaining
  - X-RateLimit-Reset

### Best Practices

1. Store API keys securely
2. Implement retry logic with exponential backoff
3. Handle rate limits appropriately
4. Monitor API status page
5. Subscribe to API updates
6. Test in sandbox environment first

### Testing

Use our sandbox environment for testing:
https://sandbox-api.drx.com/v2

Test API keys are available in the developer dashboard.

### Support

- Documentation: docs.drx.com
- Support Email: api-support@drx.com
- Status Page: status.drx.com
- Developer Forum: community.drx.com

### Next Steps

1. Review the API endpoints
2. Set up authentication
3. Try example requests
4. Implement error handling
5. Test your integration
6. Monitor usage and performance
```

---

# **Example Data**

```markdown
## Example Data

### Overview

This section provides example data structures and responses that you'll encounter when using the DRX API. These examples help illustrate the expected format and content of various API objects.

### Address Object

json
{
  "id": "addr_12345",
  "street_1": "123 Main St",
  "street_2": "Suite 100",
  "city": "Austin",
  "state": "TX",
  "postal_code": "78701",
  "country": "US",
  "type": "billing",
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}

### User Object

json
{
  "id": "usr_67890",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "phone": "+1-555-123-4567",
  "status": "active",
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}

### Order Object

json
{
  "id": "ord_24680",
  "customer_id": "usr_67890",
  "status": "processing",
  "items": [
    {
      "id": "item_111",
      "product_id": "prod_555",
      "quantity": 2,
      "price": 29.99
    }
  ],
  "shipping_address": {
    "id": "addr_12345",
    "street_1": "123 Main St",
    "street_2": "Suite 100",
    "city": "Austin",
    "state": "TX",
    "postal_code": "78701",
    "country": "US"
  },
  "total": 59.98,
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}

### Error Response

json
{
  "error": {
    "code": "validation_error",
    "message": "Invalid request parameters",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}

### Pagination Response

json
{
  "data": [...],
  "pagination": {
    "total_items": 100,
    "total_pages": 5,
    "current_page": 1,
    "per_page": 20,
    "next_page": 2,
    "prev_page": null
  }
}

### Common Fields

Most objects in the API include these standard fields:

- id: Unique identifier with appropriate prefix
- created_at: UTC timestamp of creation
- updated_at: UTC timestamp of last update
- status: Current state of the object (when applicable)

### Data Types

| Type | Format | Example |
|------|---------|---------|
| ID | string with prefix | "usr_12345" |
| DateTime | ISO 8601 UTC | "2025-02-19T08:50:00Z" |
| Currency | decimal | 29.99 |
| Phone | E.164 format | "+1-555-123-4567" |
| Country | ISO 3166-1 alpha-2 | "US" |
| State | Standard code | "TX" |
```

---

# **Dates, Times, and Timezones**

```markdown
## Dates, Times, and Timezones

### Overview

The DRX API handles all date and time values in a consistent format to ensure reliable data processing across different timezones.

### Date and Time Format

All timestamps in the API use ISO 8601 format in UTC:

YYYY-MM-DDTHH:mm:ssZ

Example:
2025-02-19T08:53:00Z

### Timezone Handling

- All API responses return timestamps in UTC
- Client applications should convert UTC times to local timezone for display
- When sending dates/times to the API, you can either:
  - Send UTC time directly
  - Include timezone offset in ISO 8601 format

### Examples

#### UTC Time
json
{
  "created_at": "2025-02-19T08:53:00Z",
  "updated_at": "2025-02-19T08:53:00Z"
}

#### With Timezone Offset
json
{
  "appointment_time": "2025-02-19T02:53:00-06:00"  // Central Time
}

### Best Practices

1. Always store times in UTC internally
2. Convert to local time only for display purposes
3. Include timezone information when scheduling future events
4. Use ISO 8601 format for all date/time values
5. Consider daylight saving time when working with future dates

### Date-Only Fields

For fields that only require a date (no time component):

json
{
  "birth_date": "2000-01-01",
  "expiration_date": "2025-12-31"
}

### Time Ranges

When specifying time ranges:

json
{
  "start_time": "2025-02-19T08:00:00Z",
  "end_time": "2025-02-19T17:00:00Z"
}

### Common Issues

- Mixing timezone-aware and naive timestamps
- Not accounting for daylight saving time transitions
- Assuming all days have 24 hours
- Not considering leap years/seconds
- Using ambiguous date formats (e.g., MM/DD/YY vs DD/MM/YY)
```

---

# **Changes to the API (Additional Details)**

```markdown
## Changes to the API

The DRX API is constantly evolving to provide better functionality and improved user experience. This section outlines important changes and updates to the API that may affect your integration.

### API Version Updates

The API version is indicated in the URL path. For example:
https://api.drx.com/v2/endpoint

When breaking changes are introduced, a new version number will be released. We maintain backward compatibility within the same major version number.

### Breaking Changes

- Removal of deprecated endpoints
- Changes to request/response structures
- Authentication method updates

### Deprecation Notices

When features are scheduled for removal or major changes, we provide:
- Advance notice through the changelog
- Migration guides
- Timeline for deprecation
- Alternative endpoints or methods

### Changelog Access

You can access the full changelog at:
- API Dashboard
- Release Notes section
- Email notifications (for registered developers)

### Best Practices

- Always specify API version in requests
- Monitor changelog regularly
- Test integrations in staging environment
- Subscribe to developer notifications
- Review deprecation notices
```

---

# **Addresses**

```markdown
## Addresses

### Look Up an Address

Retrieve details for a specific address using its unique identifier.

#### Endpoint

GET /api/v2/addresses/{address_id}

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| address_id | string | Unique identifier of the address to retrieve |

#### Response

##### Success Response (200 OK)

json
{
  "id": "addr_12345",
  "street_1": "123 Main St",
  "street_2": "Suite 100",
  "city": "Austin",
  "state": "TX",
  "postal_code": "78701",
  "country": "US",
  "type": "billing",
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}

##### Error Responses

- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Address ID does not exist

#### Notes

- All address fields are included in the response
- Historical address data is preserved and accessible
- Use this endpoint when you need complete details for a specific address
- The address ID must be a valid identifier previously returned by the API
- Response includes both the created_at and updated_at timestamps
- Deleted addresses will return a 404 Not Found response

### Get a List of Addresses

Retrieve a list of all addresses in the system. This endpoint supports pagination and filtering to manage large sets of address records.

#### Endpoint

GET /api/v2/addresses

#### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| page | integer | Page number for pagination (default: 1) |
| per_page | integer | Number of items per page (default: 20, max: 100) |
| type | string | Filter by address type (e.g., "billing", "shipping") |
| city | string | Filter by city name |
| state | string | Filter by state/province code |
| country | string | Filter by country code |

#### Response

##### Success Response (200 OK)

json
{
  "data": [
    {
      "id": "addr_12345",
      "street_1": "123 Main St",
      "street_2": "Suite 100",
      "city": "Austin",
      "state": "TX",
      "postal_code": "78701",
      "country": "US",
      "type": "billing",
      "created_at": "2025-02-19T08:50:00Z",
      "updated_at": "2025-02-19T08:50:00Z"
    },
    {
      "id": "addr_12346",
      "street_1": "456 Oak Ave",
      "street_2": "Unit 200",
      "city": "Austin",
      "state": "TX",
      "postal_code": "78702",
      "country": "US",
      "type": "shipping",
      "created_at": "2025-02-19T08:51:00Z",
      "updated_at": "2025-02-19T08:51:00Z"
    }
  ],
  "pagination": {
    "total_items": 50,
    "total_pages": 3,
    "current_page": 1,
    "per_page": 20,
    "next_page": 2,
    "prev_page": null
  }
}

##### Error Responses

- 401 Unauthorized: Invalid or missing API key
- 400 Bad Request: Invalid query parameters

#### Notes

- Results are sorted by creation date in descending order
- Empty or invalid filters are ignored
- All address fields are included in the response
- Pagination metadata is always included
- Maximum of 100 addresses can be retrieved per request
- Use pagination for large datasets

### Edit an Address

Update an existing address in the system. This endpoint allows you to modify the details of a previously created address record.

#### Endpoint

PATCH /api/v2/addresses/{address_id}

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| address_id | string | Unique identifier of the address to update |

#### Request Body

| Field | Type | Description |
|-------|------|-------------|
| street_1 | string | Primary street address |
| street_2 | string | Secondary address info (optional) |
| city | string | City name |
| state | string | State/province code |
| postal_code | string | ZIP/Postal code |
| country | string | Country code (ISO 3166-1 alpha-2) |
| type | string | Address type (e.g., "billing", "shipping") |

#### Example Request

json
{
  "street_1": "456 Oak Ave",
  "street_2": "Unit 200",
  "city": "Austin",
  "state": "TX",
  "postal_code": "78702",
  "country": "US",
  "type": "shipping"
}

#### Response

##### Success Response (200 OK)

json
{
  "id": "addr_12345",
  "street_1": "456 Oak Ave",
  "street_2": "Unit 200",
  "city": "Austin",
  "state": "TX",
  "postal_code": "78702",
  "country": "US",
  "type": "shipping",
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:54:00Z"
}

##### Error Responses

- 400 Bad Request: Invalid address data
- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Address ID does not exist
- 422 Unprocessable Entity: Missing required fields

#### Notes

- All fields except street_2 are required
- Country codes must be valid ISO 3166-1 alpha-2 codes
- State codes must be valid for the specified country
- Postal code format is validated based on country
- Address type must be one of the predefined values
- The created_at timestamp remains unchanged
- The updated_at timestamp is automatically updated
- Historical address data is preserved for audit purposes

### Add an Address

Add a new address to the system. This endpoint allows you to create a new address record with detailed location information.

#### Endpoint

POST /api/v2/addresses

#### Request Body

| Field | Type | Description |
|-------|------|-------------|
| street_1 | string | Primary street address |
| street_2 | string | Secondary address info (optional) |
| city | string | City name |
| state | string | State/province code |
| postal_code | string | ZIP/Postal code |
| country | string | Country code (ISO 3166-1 alpha-2) |
| type | string | Address type (e.g., "billing", "shipping") |

#### Example Request

json
{
  "street_1": "123 Main St",
  "street_2": "Suite 100",
  "city": "Austin",
  "state": "TX",
  "postal_code": "78701",
  "country": "US",
  "type": "billing"
}

#### Response

##### Success Response (200 OK)

json
{
  "id": "addr_12345",
  "street_1": "123 Main St",
  "street_2": "Suite 100",
  "city": "Austin",
  "state": "TX",
  "postal_code": "78701",
  "country": "US",
  "type": "billing",
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}

##### Error Responses

- 400 Bad Request: Invalid address data
- 401 Unauthorized: Invalid or missing API key
- 422 Unprocessable Entity: Missing required fields

#### Notes

- All fields except street_2 are required
- Country codes must be valid ISO 3166-1 alpha-2 codes
- State codes must be valid for the specified country
- Postal code format is validated based on country
- Address type must be one of the predefined values
```

---

# **Allergies**

```markdown
## Allergies

### Look Up an Allergy

Retrieve detailed information about a specific allergy using its unique identifier.

#### Endpoint

GET /api/v2/allergies/{allergy_id}

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| allergy_id | string | Unique identifier of the allergy to retrieve |

#### Response

##### Success Response (200 OK)

json
{
  "id": "alg_12345",
  "name": "Penicillin",
  "category": "medication",
  "description": "Beta-lactam antibiotic",
  "common_reactions": [
    "Rash",
    "Hives",
    "Difficulty breathing"
  ],
  "severity_levels": [
    "mild",
    "moderate",
    "severe"
  ],
  "contraindications": [
    "Previous anaphylactic reaction",
    "Family history of severe reactions"
  ],
  "alternatives": [
    "Erythromycin",
    "Azithromycin"
  ],
  "created_at": "2025-02-19T09:00:00Z",
  "updated_at": "2025-02-19T09:00:00Z"
}

##### Error Responses

- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Allergy ID does not exist

#### Notes

- All allergy details are included in the response
- Common reactions are listed in order of frequency
- Severity levels indicate possible reaction intensities
- Contraindications help identify high-risk situations
- Alternatives suggest substitute medications/substances
- The allergy ID must be a valid identifier previously returned by the API
- Response includes both the created_at and updated_at timestamps

### Get a List of Allergies

Retrieve a list of all allergies in the system. This endpoint supports pagination and filtering options.

#### Endpoint

GET /api/v2/allergies

#### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| page | integer | Page number for pagination (default: 1) |
| per_page | integer | Number of items per page (default: 20, max: 100) |
| category | string | Filter by allergy category (e.g., "medication", "food") |
| severity | string | Filter by severity level |
| search | string | Search term to filter allergies by name or description |

#### Response

##### Success Response (200 OK)

json
{
  "data": [
    {
      "id": "alg_12345",
      "name": "Penicillin",
      "category": "medication",
      "description": "Beta-lactam antibiotic",
      "common_reactions": [
        "Rash",
        "Hives",
        "Difficulty breathing"
      ],
      "severity_levels": [
        "mild",
        "moderate",
        "severe"
      ],
      "created_at": "2025-02-19T09:00:00Z",
      "updated_at": "2025-02-19T09:00:00Z"
    },
    {
      "id": "alg_12346",
      "name": "Peanuts",
      "category": "food",
      "description": "Tree nut allergy",
      "common_reactions": [
        "Anaphylaxis",
        "Swelling",
        "Respiratory distress"
      ],
      "severity_levels": [
        "moderate",
        "severe"
      ],
      "created_at": "2025-02-19T09:01:00Z",
      "updated_at": "2025-02-19T09:01:00Z"
    }
  ],
  "pagination": {
    "total_items": 150,
    "total_pages": 8,
    "current_page": 1,
    "per_page": 20,
    "next_page": 2,
    "prev_page": null
  }
}

##### Error Responses

- 401 Unauthorized: Invalid or missing API key
- 400 Bad Request: Invalid query parameters

#### Notes

- Results are sorted alphabetically by allergy name
- Empty or invalid filters are ignored
- All allergy details are included in the response
- Pagination metadata is always included
- Maximum of 100 allergies can be retrieved per request
- Use the search parameter for partial name matches
- Category must be one of the predefined values
- Severity filter matches allergies that include the specified level

### Add an Allergy to a Patient

Record a new allergy for a specific patient in the system.

#### Endpoint

POST /api/v2/patients/{patient_id}/allergies

#### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| patient_id | string | Unique identifier of the patient |

#### Request Body

| Field | Type | Description |
|-------|------|-------------|
| allergy_id | string | Unique identifier of the allergy |
| severity | string | Severity level of the allergy ("mild", "moderate", "severe") |
| reaction | string | Description of the allergic reaction |
| notes | string | Additional notes about the allergy (optional) |
| onset_date | string | Date when the allergy was first observed (ISO 8601) |

#### Example Request

json
{
  "allergy_id": "alg_12345",
  "severity": "moderate",
  "reaction": "Hives and difficulty breathing",
  "notes": "Requires immediate medical attention if exposed",
  "onset_date": "2025-01-15"
}

#### Response

##### Success Response (201 Created)

json
{
  "id": "pat_alg_67890",
  "patient_id": "pat_12345",
  "allergy_id": "alg_12345",
  "severity": "moderate",
  "reaction": "Hives and difficulty breathing",
  "notes": "Requires immediate medical attention if exposed",
  "onset_date": "2025-01-15",
  "created_at": "2025-02-19T09:00:00Z",
  "updated_at": "2025-02-19T09:00:00Z"
}

##### Error Responses

- 400 Bad Request: Invalid request data
- 401 Unauthorized: Invalid or missing API key
- 404 Not Found: Patient or allergy not found
- 422 Unprocessable Entity: Missing required fields

#### Notes

- All fields except notes are required
- Severity must be one of: "mild", "moderate", "severe"
- Onset date must be in ISO 8601 format (YYYY-MM-DD)
- The allergy_id must reference a valid allergy in the system
- Multiple allergies can be recorded for the same patient
- Historical allergy records are preserved for medical history
```

---

# **Charge Accounts**

```markdown
## Charge Accounts

### Lookup a Charge Account

**Method:** GET

**Parameters:**
- Charge Account Primary Key: Required

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

```

---

# **Claims**

```markdown
## Claims

### Lookup a Claim

Using the Claim's primary key, you can find all the information associated with your claim.

**Method:** GET

**Parameters:**
- Claim Primary Key: Required

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Deliveries**

```markdown
## Deliveries

### Get a List of Deliveries

The default order is to order by route and then by route_order. The pharmacy has the ability to assign the preferred route order. This defaults to the most efficient round trip starting at and ending at the pharmacy address. It is possible that the route order could be null.

**Method:** GET

**Parameters:**
- Route: Filter deliveries by a specific route
- Number of records to return per page
- Page number
- Date: Filter deliveries due on a specific date
- External ID: Find deliveries with your assigned external_id

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get a List of Delivery Routes

This endpoint will always sort routes in alphabetical ascending order.

**Method:** GET

**Parameters:**
- Number of records to return
- Page number to return

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Look Up a Delivery

**Method:** GET

**Parameters:**
- Delivery ID: The specific ID of the delivery (Required)

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Edit a Delivery

**Method:** PATCH

You may choose to edit any of the following fields:

| Field | Definition |
|---|---|
| delivery_on | isoformat date |
| name | delivery name |
| address | address |
| city | city |
| state | state |
| zip_code | zip code |
| refused_at | Isoformat date. This will display in the 'Delivered?' column with the red 'Refused' highlighted. |
| refused_by | String. The person who refused the delivery |
| completed_at | Isoformat date. This will display in the 'Delivered?' column with the green highlighted 'Delivered' sign |
| special_instructions | This is equivalent to the 'Instructions' column in the Delivery Queue |
| recipient_phone | String. This will be 10 digits long without the parenthesis and dashes. |
| external_id | You may add an external_id to a delivery and you may search by this field. |
| label_url | Text field of the label url. This will display on the Delivery Queue |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Doctors**

```markdown
## Doctors

### Look Up a Doctor

You can look up a doctor using the doctor ID.

**Method:** GET

**Parameters:**
- Identifier: Doctor primary key, or Doctor DEA, or Doctor NPI (Required)

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get a List of Doctors

To narrow down this endpoint when getting a list of doctors, you can use the q query parameter to enter search criteria.

**Method:** GET

**Parameters:**
- How many records to return
- Offset of records being returned (used for pagination)
- Search query (used to search for a doctor)

**Search Criteria:**

| Criteria | Example |
|---|---|
| Date of Birth | Format with MMDDYYYY ex. 01201986 |
| Phone Number | 10 digits, no spaces or extra characters ex. 5852984455 |
| Name | Format is last_name,first_name. Optionally you can do last name only. Partial names are allowed. ex. nau, ron; ex. naugle; ex. naugle,ron |
| Fax Number | Doctor Fax number as 10 digits, no spaces or extra characters |
| NPI | Doctor NPI as 10 digits |
| DEA | Doctor DEA |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Search Provider Catalog

You can search the surescripts list of providers through this endpoint.

**Method:** GET

**Parameters:**
- Provider First Name
- Prescriber Last Name
- Prescriber SPI
- Provider DEA
- Provider NPI
- State (as a 2 letter string)

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Add a Doctor

If you wish to add a doctor, you are required to add a few objects to the payload. You must add a "prescriber" object, an "addresses" object, and a "phone_numbers" object.

**Method:** POST

#### Prescriber Object

Required Fields:
| Field | Definition |
|---|---|
| first_name | Prescriber first name |
| last_name | Prescriber last name |
| npi | String. National Provider Identifier |

Optional Fields:
| Field | Definition |
|---|---|
| prescriber_type | String. M.D., N.P., ARNP, D.V.M., P.A., F.P.N |
| supervising_physician_id | Foreign key to Supervising Physician |
| dea | String. Prescriber dea |
| spi | SureScripts Prescriber ID |
| renewal_method | Must be one of: 'E-Script', 'Fax', 'Phone' |
| fax_number | 10 digit fax number |
| email | Doctor email |
| website | Doctor website |
| state_license | Doctor's state license |
| practice_location | Doctor's practice location |
| comments | Comments |

#### Addresses Object

The "addresses" must be a list of objects.

Required Fields for each address:
| Field | Definition |
|---|---|
| street | Prescriber address street |
| city | Prescriber address city |
| state | Prescriber address state |
| zip | Prescriber address zip code |
| type_ | Must be one of: 'default', 'delivery', 'shipping', or 'billing' |

Optional Fields:
| Field | Definition |
|---|---|
| line_two | Doctor address line two |

#### Phone Numbers Object

The "phone_numbers" must be a list of objects.

Required Fields for each phone number:
| Field | Definition |
|---|---|
| number | Patient phone number |
| phone_type | Must be one of: 'cell', 'home', 'other' |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Eligibility**

```markdown
## Eligibility

### Real Time Eligibility Check

**Important Notice:** This will send an E1 Eligibility Search Transaction out and therefore there is a cost associated with this request that will get billed to your store.

**Method:** GET

In order to use this endpoint, you have to provide a patient_id in the path params. We will check if the patient has a default address. If the patient doesn't have a default address, please use our Add an Address endpoint to add a default address to this patient.

**Parameters:**
- Patient Primary Key: Required

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Inventory**

```markdown
## Inventory

### Get All Inventory

**Method:** GET

**Note:** This endpoint does not use paging as an exception to the normal procedure. You can expect to receive every item with either a positive or negative balance on hand. As a result, this endpoint can sometimes take several seconds to respond for stores with large amounts of inventory.

This report uses today's date as the default end date from which to calculate the item's current balance on hand. You may pass in another date to see the inventory history over time.

**Parameters:**
- As of Date (optional): Date to see inventory history

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get Item Inventory History

This endpoint allows you to see the detailed inventory history during a specified date range for a specific item ID.

**Method:** GET

**Notes:**
- The default start and end date are the last 14 days if not specified in the request
- The response includes two arrays:
  1. Starting balances
  2. Individual inventory entries for each item
- If the query parameter includeEquivalents is set to true, you may get more than one item ID in the inventories array. Those IDs will have to be matched up to the starting balances array to accurately reflect the "running balance" total.

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Images**

```markdown
## Images

### Get an Image

To look up an image, you must first select a type and then supply an ID for that type. The ID is the primary key used in the database to look up the image associated with that particular model.

**Method:** GET

**Notes:**
- For prescription hard copy images: Use prescription type with prescription number as ID
- For point of sale signatures: Use pos_event type with Sale ID
- For patient-related images (scanned forms, med lists, etc.): Use patient type with Patient ID
- Some records will have multiple images associated with them. Expect an array result containing all images for that particular record.

**Parameters:**
- Type: The type of image being retrieved
- ID: The unique ID for the type provided

**Valid Types:**
| Type | Description |
|---|---|
| pos_event | Any images associated with the sale ID supplied |
| prescription | Any images associated with a particular prescription |
| patient | Any images associated with a particular patient |
| delivery | Any images associated with a delivery |

**Status Codes:**
- 200: Success
- 400: Bad Request

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Add an Image

To save an Image to DRX, save base64 encoded data to the image_data field. Next, you want to assign it to one of: Patient, User, Item, POS Event, Compound Batch, or a Delivery.

**Method:** POST

**Fields:**
| Field | Description |
|---|---|
| image_data | Base64 Image Data |
| name | Name of the image |
| patient_id | Link to Patient |
| user_id | Link to User |
| item_id | Link to Item |
| pos_event_id | Link to POS Event Id |
| compound_batch_id | Link to Compound Batch |
| delivery_id | Link to Delivery |
| created_on | Time Image was created (DateTime) |

**Status Codes:**
- 200: Success
- 400: Bad Request

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Item**

```markdown
## Item

### Look Up an Item

**Method:** GET

**Important Note for Central Site Stores:**
If you are accessing this API against a store that is in a group of central site stores (shared database), the primary key for the same NDC will be different for each store.

Example:
Omeprazole 40 MG
Store A: NDC = 99988222211, Primary Key=61
Store B: NDC = 99988222211, Primary Key=7817

- If looking up an item by NDC, DRX will pull the correct item based on the store slug that you use in the hostname portion of the API endpoint (https://<store_slug>.drxapp.com)
- If using a primary key to look up the item and that item doesn't belong to the store whose endpoint you used, you will get nothing back.
  Example: Looking up item_id=7817 using Store A's URL will return nothing.

**Parameters:**
- Identifier: NDC, UPC, or the Primary Key

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get a List of Items

The default ordering is by item name in ascending order.

**Method:** GET

**Parameters:**
- Number of records to return
- NDC (optional): Filter by National Drug Code. Supports partial matches (e.g., ?ndc=111 will match any NDC beginning with 111)
- GCN (optional): Filter by GCN Code (representing equivalent items). Does not allow partial matches
- Item Type (optional): Filter by specified item type

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Import From FDB Catalog

Sometimes, an item you need may not be in your database. If this is the case, you have the option to import it from the FDB Catalog. All that is required is to have the item's UPC or NDC. Additionally, you may provide the supplier id as a parameter if you wish to delineate by your suppliers.

**Method:** GET

**Parameters:**
- Identifier: Either the Item UPC or NDC (Required)
- Supplier ID: Optional parameter to specify Supplier Primary Key

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Update Reorder Points

DRX has three different ordering "groupings". These groupings determine the balance on hand to use for the purpose of reordering.

**Method:** POST

**Grouping Types:**
1. Plain Item: Balance on hand takes into account only this particular item's inventory and no other items. Used when a store wants to keep a BOH of a specific item without regard to other equivalents in stock.
2. Equivalents for Reordering: Takes into account all equivalent items when calculating BOH. Example: Three different manufacturers of Atorvastatin 40MG will be evaluated together.
3. Equivalents with Stock Size: Uses equivalents but respects stock size. Example: Atorvastatin 40MG PKG 1000 is not equivalent to Atorvastatin 40MG PKG 100.

DRX will automatically detect which grouping the drug belongs to and update the MIN/MAX for that group. You can determine which group an item belongs to using the Look up an Item API endpoint:
json
"use_equivalents_for_ordering": true,
"respect_package_size": false

- Both false: Grouping 1
- Equivalents true, stock size false: Grouping 2
- Both true: Grouping 3

**Parameters:**
- Item Identifier: NDC, UPC, or ID of item to update
- Maximum: Maximum to keep on hand. DRX will try to order to achieve a BOH above the min without going over this max
- Minimum: Minimum to keep on hand. DRX will try to order enough to get just above the min without going over the max

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get a List of Claims

**Method:** GET

**Parameters:**
- How many records to return
- Offset of records to be returned (useful for pagination)
- Find claims before this date time
- Find claims after this date time

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Update Equivalents for Reordering

This endpoint allows you to update the ordering groupings for items.

**Method:** POST

**Grouping Types:**
1. Plain Item: Balance on hand takes into account only this particular item's inventory and no other items.
2. Equivalents for Reordering: Takes into account all equivalent items when calculating BOH.
3. Equivalents with Stock Size: Uses equivalents and respects stock size for determining equivalents.

**Important Note on Invalid Configuration:**
There is never a valid situation where:
json
"use_equivalents_for_ordering": false,
"respect_package_size": true

DRX will set both to false if use_equivalents_for_ordering is set to false.

**Parameters:**
- Item Identifier: NDC, UPC, or ID of item to update
- Configuration:
  
json
  {
    "use_equivalents_for_ordering": true,
    "respect_package_size": false
  }

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Update Balance On Hand

**Method:** POST

**Parameters:**
- Item Identifier: NDC, UPC, or ID of item to update
- New BOH: New Balance On Hand value
- Reason: Description for the BOH change

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Packing List**

```markdown
## Packing List

### Get a List of Packing Lists

**Method:** GET

**Parameters:**
- Limit: Maximum number of records to return (max: 100)
- Offset: For pagination

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get All Prescription Fills on Packing List

**Method:** GET

**Parameters:**
- Primary Key: Required

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Partners**

```markdown
## Partners

### Commands

The partners API is to generate specific responses tailored to a particular vendor. This endpoint may be used by anyone with the appropriate API key, but it was designed for specific integrations and the outputs are frozen and cannot be modified.

**Method:** GET

**Note:** The endpoint requires a partner name in the path, but it can be any name used to help identify the source of the request.

**Commands:**
| Command | Description |
|---|---|
| command=startFeed | Start the daily Datarithm export. IMPORTANT: This command will not take effect until the next server restart (occurs once per week or sooner). If data is needed prior to this taking effect, use the export command. |
| command=endFeed | End the daily Datarithm export. IMPORTANT: This command will also not take effect until the next server restart. |
| command=checkTaskStatus&taskId=<task_id> | Check on the progress of a recently started export task. |
| command=export | Start a new export of data. By default returns the last two days. Add &startDate=yyyy-mm-dd parameter for an earlier start date. Returns a task ID to watch job progress. |
| command=dataDump | Issue a signed download link for database dump tables relevant to a full data conversion to another vendor. The link will be sent to the email address on file. IMPORTANT: Contact DRX support ahead of time to get the destination email address added to the store's system. |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Data Dump Example

If you are intending to use the data dump feature, please follow these guidelines:

#### Step 1: Contact DRX Support
Contact DRX support (support@drxpharmacytech.com) with your intention to use the data dump command. DRX support will send you a data export form that must be filled out and put on file for the customer.

#### Step 2: Email Setup
You must indicate to DRX which email address you'd like the export link to be sent to, or this endpoint will produce no output. DRX support will activate the email address provided and validate the data export form.

#### Step 3: API Request
Attempt to pull the data using the following API request:

bash
curl --request GET \
     --url 'https://slug.drxapp.com/external_api/v1/partners/infowerks?command=dataDump' \
     --header 'X-DRX-Key: DRX7XXXXXXXXXXXXXXXXXXXXXX' \
     --header 'accept: application/json'

Response:
json
{
    "success": true,
    "message": "Data export started, this can take up to 1 hour to complete.",
    "task_id": "82919a9b-825e-46c1-938a-a5a4e69f1675"
}

Check task status:
bash
curl --request GET \
     --url 'https://slug.drxapp.com/external_api/v1/partners/infowerks?command=checkTaskStatus&taskId=82919a9b-825e-46c1-938a-a5a4e69f1675' \
     --header 'X-DRX-Key: DRX75e1XXXXXXXXXXXXXXXXXXXXXXXXXXXX' \
     --header 'accept: application/json'

Response:
json
{
    "success": true,
    "response": {
        "state": "PENDING"
    }
}

**Important Notes:**
- Use your own API key and ensure the slug matches the store you are pulling from
- Data export can take up to an hour for busy stores
- Do not start a second pull until the previous one completes
- Partners that overrun server resources may have API keys suspended
- Recommended to perform dumps after hours if possible

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Patient**

```markdown
## Patient

### Look Up a Patient

You can look up a patient using the patient ID.

**Method:** GET

**Parameters:**
- Patient Primary Key: Required

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| 3h ago | 200 | Try It! |

### Get a List of Patients

To narrow down this endpoint when getting a list of patients, you can use the q query parameter to enter search criteria.

**Method:** GET

**Parameters:**
- Limit: How many records to return
- Offset: Offset of records being returned (used for pagination)
- Search Query: Used to search for a patient
- Before Date: Receive patients who've filled before your date (doesn't include the date)
- After Date: Receive patients who've filled after your date (doesn't include the date)
- Facility ID: Filter Patients linked to this Facility

**Search Criteria:**
| Criteria | Example |
|---|---|
| Date of Birth | Format with MMDDYYYY ex. 01201986 |
| Phone Number | 10 digits, no spaces or extra characters ex. 5852984455 |
| Name | Format is last_name,first_name. Optionally you can do last name only. Partial names are allowed. ex. saf, dan; ex. safee; ex. safee,dani |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| 19h ago | 200 | Try It! |
| 19h ago | 200 | Try It! |
| 22h ago | 200 | Try It! |

### Add a Patient

To add a patient, there are several required fields and optional fields available.

**Method:** POST

**Required Patient Fields:**
| Field | Definition |
|---|---|
| first_name | Patient First Name |
| last_name | Patient Last Name |
| date_of_birth | Patient date of birth as an ISO formatted string |
| gender | Patient Gender as a one character string. Must be 'M' or 'F' |

**Optional Patient Fields:**
| Field | Definition |
|---|---|
| email | String |
| middle_initial | Middle initial of the patient |
| dont_notify_again_until | Pause notifications until specified date |
| delivery_method | 'Ship', 'Pickup', or 'Delivery' which specifies how a patient normally receives their medication |
| drivers_license | Patient's driver license as an Integer |
| social_security_number | Gov't issued social in the form of: 123-45-6789 |
| alternate_id | External ID used for various purposes |
| auto_refill | Boolean to define whether or not patient will be on auto fill |
| height_in_centimeters | Height in centimeters |
| weight_in_grams | Weight in grams |
| automatically_charge_rx_to_account | Boolean that dictates whether prescriptions auto charge to patient's A/R account when hitting Waiting Bin status |
| facility_room_id | Primary key to Facilities (currently not supported in the API) |
| facility_wing_id | Primary key to Facility Wings (currently not supported in the API) |
| blister_pack | Flag if the patient is using a blister pack |
| notify_method | 1 - Email, 2 - Phone, 3 - Do not notify, 0 - Text |
| easy_open | Boolean that designates whether patient may receive easy off caps (Non Safety Caps) |
| cycle_fill_date | Next fill date for patient's sync list meds |
| cycle_interval | Number of days to increment cycle_fill_date when completing sync workflow |
| race | Patient's race: 'Human', 'Dog', 'Cat', 'Bird', 'Reptile', 'Rodent', 'Horse', 'Other' |
| primary_language | 'English' or 'Spanish' |

**Required Address Fields:**
Must append an "addresses" object (list of objects) to the payload.
| Field | Definition |
|---|---|
| street | Patient address street |
| city | Patient address city |
| state | Patient address state |
| zip | Patient address zip code |
| type_ | Must be one of: 'default', 'delivery', 'shipping', or 'billing' |

**Optional Address Fields:**
| Field | Definition |
|---|---|
| line_two | Patient address line two |

**Required Phone Number Fields:**
Must append a "phone_numbers" object (list of objects) to the payload.
| Field | Definition |
|---|---|
| number | Must be a 10 digit long String |
| phone_type | Must be one of: 'cell', 'home', 'other' |

**Optional Allergies:**
May append an "allergies" object (list of objects) to link allergies to a patient.
| Field | Description |
|---|---|
| concept_id_type | Concept id type: Integer |
| dam_concept_id | Integer |

Note: For allergy IDs, check the ALLERGIES endpoint documentation.

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Edit a Patient

If you wish to edit a patient, you may do so using this endpoint. You must provide a patient_id in the URL. Add to the payload object any fields you wish to edit. Omitted fields will be ignored.

**Method:** PATCH

**Parameters:**
- Patient Primary Key: Required

**Editable Fields:**
| Field | Definition |
|---|---|
| first_name | Patient First Name |
| last_name | Patient Last Name |
| date_of_birth | Patient date of birth as an ISO formatted string |
| gender | Patient Gender as a one character string. Must be 'M' or 'F' |
| email | String |
| middle_initial | Middle initial of the patient |
| dont_notify_again_until | Pause notifications until specified date |
| delivery_method | 'Ship', 'Pickup', or 'Delivery' which specifies how a patient normally receives their medication |
| drivers_license | Patient's driver license |
| social_security_number | Gov't issued social |
| alternate_id | External ID used for various purposes |
| auto_refill | Boolean to define whether or not patient will be on auto fill |
| height_in_centimeters | Height in centimeters |
| weight_in_grams | Weight in grams |
| automatically_charge_rx_to_account | Boolean that dictates whether prescriptions auto charge to patient's A/R account when hitting Waiting Bin status |
| facility_room_id | Primary key to Facilities (currently not supported in the API) |
| facility_wing_id | Primary key to Facility Wings (currently not supported in the API) |
| blister_pack | Flag if the patient is using a blister pack |
| notify_method | 1 - Email, 2 - Phone, 3 - Do not notify, 0 - Text |
| easy_open | Boolean that designates whether patient may receive easy off caps (Non Safety Caps) |
| cycle_fill_date | Next fill date for patient's sync list meds |
| cycle_interval | Number of days to increment cycle_fill_date when completing sync workflow |
| race | Patient's race: 'Human', 'Dog', 'Cat', 'Bird', 'Reptile', 'Rodent', 'Horse', 'Other' |
| primary_language | 'English' or 'Spanish' |
| active | Boolean. A deactivated patient will not appear in search results |
| deceased | Boolean. Deceased patients will have a deceased icon appear their profile |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get a List of Charge Accounts

**Method:** GET

**Parameters:**
- Patient linked to Charge Account
- Limit of records returned
- Offset of records returned (useful for paging)

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Look Up a Patient Profile

**Method:** GET

**Parameters:**
- Patient ID: Primary key for patient record (Required)

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Patient Match**

```markdown
## Patient Match

### Find a Match

**Method:** POST

**Requirements:**
- DRX requires that the Rx number, first name, and last name fields be populated to produce a match
- If there is not one and only match, no patient data will be displayed
- The date of birth field must be an ISO 8601 formatted string

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Phone Numbers**

```markdown
## Phone Number

### Look Up a Phone Number

You can look up a phone number using its ID.

**Method:** GET

**Parameters:**
- Phone Number Primary Key: Required

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get a List of Phone Numbers

To narrow down this endpoint when getting a list of phone numbers, you can use the q query parameter to enter search criteria.

**Method:** GET

**Parameters:**
- Limit: How many records to return
- Offset: Offset of records being returned (used for pagination)
- Search Query: Used to search for a phone number

**Search Criteria:**
| Criteria | Example |
|---|---|
| Phone Number | 10 digits, no spaces or extra characters ex. 5852984455. You may search for any part of the number |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Add a Phone Number

**Method:** POST

**Note:** You must provide either a patient_id to add a phone number to a patient, or a doctor_id to add a phone number to a doctor.

**Patient Link Fields:**
| Field | Definition |
|---|---|
| patient_id | Patient id that the phone number will be linked to |

**Doctor Link Fields:**
| Field | Definition |
|---|---|
| doctor_id | Doctor id that the phone number will be linked to |

**Required Fields:**
| Field | Definition |
|---|---|
| number | Patient phone number |
| phone_type | Must be one of: 'cell', 'home', 'other' |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Edit a Phone Number

To edit a phone number, there are 2 fields available to edit. Omitting a field will result in no change for that specific field.

**Method:** PATCH

**Parameters:**
- Phone Number Primary Key: Required

**Editable Fields:**
| Field | Definition |
|---|---|
| number | Phone number |
| phone_type | Must be one of: 'home', 'cell', 'other' |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Point of Sale**

```markdown
## Point of Sale

### Get a List of Sale Events

**Method:** GET

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Lookup a Sale Event

**Method:** GET

**Status Codes:**
- 200: Success
- 400: Bad Request

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Lookup a Barcode

DRX allows usage of the external API to send and receive data related to the point of sale.

**Method:** GET

**Barcode Format Details:**
- Every prescription label gets a 1D barcode that encodes data about the prescription
- Format: <bottle_or_label_flag:len(1)><prescription_fill_id:len(varies)><delimiter:(:)><label_version:len(varies)>
  Example: 'b209827:a5g'
- Components:
  * Bottle or label flag: Designates whether the scanned barcode is a prescription bottle or paper label
  * Prescription fill ID: Primary key used to locate a specific fill of a prescription
  * Delimiter: Always a colon
  * Label version: Alphanumeric string (typically 3 characters)

**Integration Notes:**
- For third party POS integrations:
  1. Before Sale: Scan barcode and parse prescription_fill_id to retrieve sale details
  2. After Sale: Send POST request to indicate sale results
  3. All refund and void transactions must be reported to maintain accurate prescription status

**Parameters:**
- Primary Key: Fill ID encoded in the label barcode

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Send a Sale Event to DRX

**Method:** POST

**Important Notes:**
- DRX processes these asynchronously and events are added to a queue for consumption
- All data validation occurs outside of the HTTP POST request
- All requests yield a 200 HTTP response code, even if errors are detected afterwards
- This design allows DRX to:
  * Monitor input from third parties
  * Potentially replay and reject inputs if issues are detected
  * Allow for variations of input created by different third party vendors

**Requirements:**
- Dates must be submitted in ISO 8601 format

**Status Codes:**
- 200: Success (Note: This is returned for all requests due to async processing)
- 400: Bad Request

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Edit a Point of Sale Event

**Method:** PATCH

**Parameters:**
- Primary Key: Point of Sale Event ID

**Editable Fields:**
| Field | Description |
|---|---|
| sub_total | Subtotal amount |
| tax | Tax amount |
| total | Total amount |
| discounts | Discount amounts |
| credit_card_fee | Credit card processing fee |
| remaining | Remaining balance |
| remaining_text | Text description of remaining balance |
| sale_comment | Comments about the sale |
| _receipt_items | Receipt item details |
| _payments | Payment details |
| cash_tendered | Cash payment amount |
| check_tendered | Check payment amount |
| credit_on_file_tendered | Credit on file payment amount |
| type_of_event | Type of sale event |
| event_status | Status of the event |
| declined_counseling | Whether counseling was declined |
| tax_exempt_sale | Whether sale is tax exempt |
| prescription_fills | Associated prescription fills |

**Status Codes:**
- 200: Success
- 400: Bad Request

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Click 2 Pay

**Method:** GET

**Parameters:**
- Point of Sale Event Primary Key: Required

**Status Codes:**
- 200: Success
- 400: Bad Request

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Prescription**

```markdown
## Prescription

### Get a List of Prescriptions

**Method:** GET

**Notes:**
- Sort order defaults to prescription written date in descending order (not configurable)
- Date filters apply to child Prescription Fills, not Prescriptions themselves
- Dates must be in ISO8601 format

**Parameters:**
- Patient ID: Filter prescription list to a specific patient
- Status: Filter by status (Options: 'Hold', 'Waiting Bin', 'Sold', 'Print', 'Rejected', 'Verify', 'Scan', 'Adjudicating', 'OOS')
- Facility ID: Filter Prescriptions by the Patient's Facility
- EHR Message ID: ehrMessageId saved from the SureScript
- EHR Order Number: ehrOrderNumber saved from the SureScript
- Expiration Date: Filter which prescriptions will expire by this date
- Before Date: Get prescriptions filled before this date
- After Date: Get prescriptions filled after this date

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| 20h ago | 200 | Try It! |
| 20h ago | 200 | Try It! |

### Look Up a Prescription

**Method:** GET

**Parameters:**
- Primary Key: Required (Prescription ID)

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| 3h ago | 200 | Try It! |
| 20h ago | 200 | Try It! |
| 20h ago | 200 | Try It! |

### Send Hard Copy Image to Intake for Processing

This endpoint allows you to send an image to the intake queue for processing by a user of the DRX system. The equivalent pharmacy workflow is if a patient drops off hard copies to scan into the intake queue for processing later.

**Method:** POST

**Required Fields:**
| Field | Definition |
|---|---|
| base64_image_data | Your image data in base64 format |
| drug_name | Name of the prescription drug |

**Optional Fields:**
| Field | Definition |
|---|---|
| sig | Medication instructions |
| comment | String comments |

**Patient Object (Required):**
Either provide:
- Patient ID:
  | Field | Definition |
  |---|---|
  | id | Patient primary key |

OR
- Patient Details:
  | Field | Definition |
  |---|---|
  | first_name | Patient first name |
  | last_name | Patient last name |
  | dob | Patient Date of Birth as an isoformat string |
  | gender | String. Either 'M' or 'F' |

**Doctor Object (Required):**
Either provide:
- Doctor ID:
  | Field | Definition |
  |---|---|
  | id | Doctor primary key |

OR
- Doctor Details:
  | Field | Definition |
  |---|---|
  | first_name | Doctor first name |
  | last_name | Doctor last name |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Generate an E-Script (Prescription Order) (Deprecated)

```markdown
**DEPRECATED:** Please use the 'Generate Surescript' endpoint found under QUEUE section instead.
```

```markdown
This endpoint generates a new prescription order without assigning an Rx number. It will appear as a new Intake item requiring user verification before prescription generation.

**Method:** POST

**Required Fields:**
| Field | Definition |
|---|---|
| doctor_id | Doctor Id (Integer Primary Key, DEA, or NPI). DRX will find and save the Doctor Primary Key if DEA or NPI is given |
| substitutions_allowed | Integer number of substitutions allowed. May not be 0 |

**Required Item Identification (One of these):**
| Field | Definition |
|---|---|
| item_id | Prescribed Item primary key |
| item_ndc | String. Prescribed Item NDC |
| item_name | Name of the prescribed item |

**Optional Field:**
| Field | Definition |
|---|---|
| notes | Notes can be any string or text |

**Medication Object (Required):**
Required Fields:
| Field | Definition |
|---|---|
| unit | Choose 1 (EA), 2 (ML), or 3 (GM) |
| quantity | Integer quantity of the medication |
| directions | Directions on how to take the medication |

Optional Fields:
| Field | Definition |
|---|---|
| prn | Boolean value. If the medication is "as needed" |
| refills | Integer quantity of refills |

**Patient Object (Required):**
Required Fields:
| Field | Definition |
|---|---|
| first_name | Patient first name |
| last_name | Patient last name |
| gender | Must be 'M' or 'F' |
| dob | Patient Date of Birth in isoformat |
| phone_number | Patient Phone Number |

Optional Fields:
| Field | Definition |
|---|---|
| species | 'Human', 'Dog', 'Cat', 'Bird', 'Reptile', 'Rodent', 'Horse', 'Other' (defaults to 'Human') |
| weight | Patient weight |
| weight_units | Units of the patient weight (required if weight provided) |
| email | Will update current patient email |
| delivery_notes | Added to Patient's comments tagged as 'Delivery' |

**Owner Object (Optional, append to patient):**
| Field | Definition |
|---|---|
| first_name | Owner first name |
| last_name | Owner last name |

**Address Object (Required, append to patient):**
Required Fields:
| Field | Definition |
|---|---|
| street | Patient street |
| city | Patient city |
| state | Patient state |
| zip | Patient zip code |
| type_ | Must be: 'default', 'delivery', 'shipping', or 'billing' |

Optional Field:
| Field | Definition |
|---|---|
| line_two | Address line two |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.
```

### Generate a Prescription

```markdown
## Generate a Prescription

This endpoint will generate a new prescription and assign it a prescription id number. The Rx will be automatically put in 'Hold' status.

**Method:** POST

**Required Fields:**
| Field | Definition |
|---|---|
| patient_id | Patient Primary Key |
| doctor_id | Doctor Primary Key |
| prescribed_quantity | Decimal value quantity prescribed |
| dispensed_quantity | Decimal value quantity dispensed |
| item_id | Item Primary Key |
| days_supply | Integer days supply |

**Optional Fields:**
| Field | Definition |
|---|---|
| pharmacist_id | Primary Key of the pharmacist User |
| date_written | Valid Isoformat date |
| date_expires | Isoformat date. If omitted, default expiration date calculated based on Location Settings |
| daw | String: 0 - 9 (defaults to 0) |
| origin_code | 'Walk-in', 'Phone-in', 'Fax', 'Electronic', 'Transfer-in', 'Other-pharmacy' |
| refills | Integer # of refills (defaults to 0) |
| fill_date | Isoformat date |
| serial_number | String serial number |
| pickup_time | Isoformat date to assign the Prescription to be picked up |
| primary_third_party_id | Primary Key of Primary Third Party |
| secondary_third_party_id | Primary key of Secondary Third Party |
| tertiary_third_party_id | Primary Key of Tertiary Third Party |
| primary_third_party_bin | Bin Number of the Primary Third Party |
| secondary_third_party_bin | Bin Number of the Secondary Third Party |
| tertiary_third_party_bin | Bin Number of the Tertiary Third Party |
| sig | Directions of how to take the medication |
| fill_tags | Array of strings. Each string will be the tag assigned |
| base64_image_data | Your image data in base64 format |
| status | 'Hold', 'Waiting Bin', 'Sold', 'Print', 'Rejected', 'Verify', 'Scan', 'Adjudicating', 'OOS' (defaults to 'Hold') |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.
```

### Inactivate Prescription

```markdown
## Inactivate Prescription

Inactivating a prescription will halt its future adjudications and scheduled fill dates. There will be an indicator in the UI that the prescription has been inactivated.

**Method:** POST

**Parameters:**
| Field | Description |
|---|---|
| prescription_id | Prescription Primary Key (Required) |
| reason | Optional. Reason for inactivating the prescription |

**Status Codes:**
- 200: Success
- 400: Bad Request

Note: URL requests expire after 30 days.
```

### Reactivate Prescription

```markdown
## Reactivate Prescription

You may reactivate a previously inactivated prescription.

**Method:** POST

**Parameters:**
| Field | Description |
|---|---|
| prescription_id | Prescription Primary Key (Required) |

**Status Codes:**
- 200: Success
- 400: Bad Request

Note: URL requests expire after 30 days.
```

---

# **Prescription Fills**

```markdown
## Prescription Fills

### Get a List of Prescription Fills

Get a list of prescription fills with various filtering options.

**Method:** GET

**Query Parameters:**
- **Date Filtering** (ISO8601 format):
  - before_date: Get fills sold before this date (exclusive)
  - after_date: Get fills sold after this date (exclusive)

- **Status Filtering:**
  - fills_in_progress: Set to true to limit results to fills in active workflow state (in progress at pharmacy or waiting for pickup)
  - status: Filter by specific fill status

- **Patient Filtering:**
  - patient_id: Limit results to a specific patient

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Look Up a Prescription Fill

Retrieve details for a specific prescription fill by its ID.

**Method:** GET

**Parameters:**
- Primary Key of the prescription fill

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Send Fill to Vial Dispensing Robot

Send a prescription fill to a connected vial dispensing robot in the pharmacy. If multiple robots are connected, the fill will be sent to any available robot (most pharmacies only have one robot).

**Method:** GET

**URL Parameter:**
- Prescription Fill primary key
- Include 'send_to_vial_dispensing_robot' in the URL

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Reverse Paid Claims

This endpoint attempts to reverse any paid claims on a prescription fill. If successful, all claims will be reversed and the fill will be put on Hold status. If there are any errors during reversal, they will be compiled into a list.

**Method:** POST

**URL Parameter:**
- Primary key of the Prescription Fill

**Request Body:**
- Empty JSON object ({})

**Response:**
- Success message if all claims reversed successfully
- List of errors if any claims failed to reverse

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Set Fill Status

Manually change the status of a prescription fill. Note that changing status may have side effects, which are expected behaviors rather than bugs.

**Method:** POST

**URL Parameter:**
- Unique ID of the fill to change status for

**Request Body:**
json
{
  "status": "string"  // Must be one of the allowed status values (case sensitive)
}

**Status Codes:**
- 200: Success
- 400: Bad Request

**Side Effects:**
Status changes may trigger automated workflows or state changes in related systems. These are normal behaviors and should not be considered bugs.

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Fill Tags**

```markdown
## Fill Tags

### Look Up a Fill Tag

Look up details for a specific prescription fill tag.

**Method:** GET

**URL Parameter:**
- Prescription Fill Tag Primary Key

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get a List of Fill Tags

Get a list of prescription fill tags with filtering and pagination options.

**Method:** GET

**Query Parameters:**
| Parameter | Description |
|---|---|
| offset | Offset of records to return (for pagination) |
| limit | Maximum number of records to return |
| name | Filter tags by name (supports partial matches) |
| fill_id | Filter tags assigned to a specific fill ID |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Add Bin Location

Add a bin location to a prescription fill.

**Method:** POST

**URL Parameter:**
- Prescription Fill Primary Key

**Request Body:**
json
{
  "bin_location_name": "string"
}

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Add Tags to a Fill

Add one or more tags to a prescription fill.

**Method:** POST

**Request Body:**
Array of objects, each containing:
| Field | Definition |
|---|---|
| prescription_fill_id | Prescription Fill Primary Key |
| tag_names | Array of strings, each string will be a tag associated with the Fill |

Example:
json
[
  {
    "prescription_fill_id": 123,
    "tag_names": ["urgent", "delivery"]
  }
]

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Remove Tags from Fills

Remove one or more tags from prescription fills.

**Method:** DELETE

**Request Body:**
Array of objects, each containing:
| Field | Definition |
|---|---|
| prescription_fill_id | Prescription Fill Primary Key |
| tag_names | Array of strings, each matching string tag will be removed |

Example:
json
[
  {
    "prescription_fill_id": 123,
    "tag_names": ["urgent", "delivery"]
  }
]

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **SureScripts**

```markdown
## SureScripts

### Look Up a SureScript

Retrieve details for a specific SureScript record.

**Method:** GET

**URL Parameter:**
- SureScript Primary Key

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| 18h ago | 200 | Try It! |

### Get a List of SureScripts (Intake Queue)

Get a list of all scripts currently in the Intake Queue, or retrieve processed scripts by setting showOldItems to true.

**Method:** GET

**Query Parameters:**
| Parameter | Description |
|---|---|
| limit | How many records to return |
| offset | Offset of records for pagination |
| showOldItems | Set to true to display processed scripts |
| external_id | Search by external_id saved to a SureScript |
| search | Search by Patient First Name, Last Name, or Drug Name |
| ehrMessageId | Filter by ehrMessageId provided after surescript is filled |
| ehrOrderNumber | Filter by ehrOrderNumber provided after SureScript is filled |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Generate SureScript

Generate a surescript that will populate into the DRX intake queue.

**Method:** POST

**Required Objects:**
1. **Patient Object:**
   - Option 1: Provide ID
     | Field | Definition |
     |---|---|
     | id | Patient Primary Key |

   - Option 2: Provide Details
     | Field | Definition |
     |---|---|
     | first_name | Patient First Name |
     | last_name | Patient Last Name |
     | gender | 'M' or 'F' |
     | dob | Patient Date of Birth as an isoformat string |

   Optional Fields:
   | Field | Definition |
   |---|---|
   | email | Updates current patient email |
   | delivery_notes | Added to Patient's comments tagged as 'Delivery' |
   | phone_number | Patient Phone Number |

   Optional Address Object:
   | Field | Definition |
   |---|---|
   | street | Address street |
   | city | Address city |
   | state | Address state |
   | zip_code | Address zip code |

2. **Doctor Object:**
   - Option 1: Provide Identifier
     | Field | Definition |
     |---|---|
     | id | Doctor Primary Key |
     | dea | Doctor DEA |
     | npi | Doctor NPI |

   - Option 2: Provide Details
     | Field | Definition |
     |---|---|
     | first_name | Doctor First Name |
     | last_name | Doctor Last Name |

   Optional Fields:
   | Field | Definition |
   |---|---|
   | phone_number | Doctor Phone Number |
   | fax_number | Doctor Fax Number |

   Optional Address Object: Same structure as patient address

3. **Medication Object:**
   - Option 1: Provide Identifier
     | Field | Definition |
     |---|---|
     | id | Drug's Primary Key |
     | ndc | String Drug's NDC |

   - Option 2: Provide Details
     | Field | Definition |
     |---|---|
     | name | Name of the Medication |

   Optional Fields:
   | Field | Definition |
   |---|---|
   | sig | Directions for taking medication |
   | refills | # of refills authorized |
   | quantity | Integer quantity |
   | medication_comment | Comment attached to medication |
   | substitutions_allowed | Daw. Integer 0-9 |

**Optional Payload Fields:**
| Field | Definition |
|---|---|
| comment | Any notes you wish to add |
| external_id | Value to search for later |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Cancel Message

Cancel a prescription message.

**Method:** POST

**Required Components:**

1. **Item Identification (One of):**
   | Field | Definition |
   |---|---|
   | item_id | Item Primary Key |
   | item_ndc | String. Item NDC |

   Or Item Object:
   | Field | Definition |
   |---|---|
   | name | Item name |
   | ndc | Item ndc |

2. **Patient Identification (One of):**
   | Field | Definition |
   |---|---|
   | patient_id | Patient Primary Key |

   Or Patient Object:
   | Field | Definition |
   |---|---|
   | first_name | Patient first name |
   | last_name | Patient last name |
   | gender | 'M' or 'F' |
   | dob | Patient Isoformat date of birth |
   | phone_number | String Phone Number |

   Required Address Object (if patient_id omitted):
   | Field | Definition |
   |---|---|
   | street | Address street |
   | city | Address city |
   | state | Address state |
   | zip_code | Integer zip code |

3. **Doctor Identification (One of):**
   | Field | Definition |
   |---|---|
   | doctor_id | Doctor Primary Key, DEA, or NPI |

   Or Doctor Object:
   | Field | Definition |
   |---|---|
   | first_name | Doctor first name |
   | last_name | Doctor last name |
   | dea | Doctor DEA |
   | fax_number | Doctor fax number |

   Optional Doctor Fields:
   | Field | Definition |
   |---|---|
   | npi | Doctor NPI |
   | state_license | Doctor State License |
   | practice_location | Doctor Practice Location |

4. **Cancel Order Object (Required):**
   Required Fields:
   | Field | Definition |
   |---|---|
   | unit | 'EA', 'ML', or 'GM' |
   | refills | Integer number of refills |
   | quantity | Float quantity of drug |
   | directions | Direction for taking drug |

   Optional Field:
   | Field | Definition |
   |---|---|
   | substitutions_allowed | Integer (defaults to 0) |

**Optional Payload Field:**
| Field | Definition |
|---|---|
| external_id | Value to search for Cancel Message |

**Notes:**
- If patient_id provided, patient must have default address
- If doctor_id provided, doctor must have default address

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Look Up a Patient Profile

Retrieve a patient's profile information.

**Method:** GET

**URL Parameter:**
- Primary key for patient record

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Delete a SureScript from the Intake Queue

Delete a SureScript from the Intake queue. The script will be permanently deleted and cannot be recovered.

**Method:** DELETE

**Query Parameter:**
- SureScript primary key (Use 'Get a List of SureScripts' endpoint to find the ID)

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Edit Intake Item

Edit items in your Intake queue. This endpoint is particularly useful for marking SureScripts as 'consumed', which removes them from the Intake queue (but they remain retrievable with 'showOldItems=true').

**Method:** PATCH

**URL Parameter:**
- SureScript Primary Key

**Editable Fields:**
| Field | Definition |
|---|---|
| consumed | Boolean. Consumed items will not appear in the Intake queue |
| patient_id | Patient Primary key |
| patient_first_name | Patient First Name |
| patient_last_name | Patient Last Name |
| doctor_first_name | Doctor First Name |
| doctor_last_name | Doctor Last Name |
| drug_name | Name of Drug |
| note | Text Note linked to the SureScript |
| external_id | ID used to search for a SureScript |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Refills and Renewals**

```markdown
## Refills and Renewals

### Send a Refill Request

Send a request to refill prescriptions for a patient.

**Method:** POST

**Requirements:**
- Must submit at least patient date of birth OR patient ID (both will be validated if provided)
- Can only submit refill requests for one patient at a time

**Response:**
Success response example:
json
{
    "success": true,
    "errors": [],
    "processed": [
        {
            "success": true,
            "message": "Sent to queue for adjudication: Task ID c3ba0298-b145-4f62-abc3-c0988ebccbdd",
            "estimated_pickup_time": "2022-03-18T08:51:20.880789",
            "item_name": "CITALOPRAM HBR 20 MG TABLET",
            "rx_id": 714130
        }
    ]
}

**Possible Error Responses:**
1. Expired Prescription:
json
{
    "success": true,
    "errors": [
        {
            "success": false,
            "message": "Rx is expired",
            "item_name": "RISPERIDONE 0.25 MG TABLET",
            "rx_id": 676112
        }
    ],
    "processed": []
}

2. Fill in Progress:
json
{
    "success": true,
    "errors": [
        {
            "success": false,
            "message": "Most recent fill still in progress",
            "rx_id": 712899
        }
    ],
    "processed": []
}

3. Patient ID Mismatch:
json
{
    "success": true,
    "errors": [
        {
            "success": false,
            "message": "Patient ID Mismatch",
            "rx_id": 712899
        }
    ],
    "processed": []
}

4. Missing Patient Information:
json
{
    "success": true,
    "errors": [
        {
            "success": false,
            "message": "Patient ID or Date of Birth must be submitted with the request",
            "rx_id": 712899
        }
    ],
    "processed": []
}

5. Insufficient Quantity:
json
{
    "success": true,
    "errors": [
        {
            "success": false,
            "message": "Insufficient qty remaining",
            "remaining": 0,
            "item_name": "CITALOPRAM HBR 20 MG TABLET",
            "rx_id": 714130
        }
    ],
    "processed": []
}

6. Date of Birth Mismatch:
json
{
    "success": true,
    "errors": [
        {
            "success": false,
            "message": "Patient Date of Birth Mismatch",
            "rx_id": 714130
        }
    ],
    "processed": []
}

**Note:**
- Estimated pickup time is set by the store in their location settings
- Pickup time should be presented to patients as an estimate only

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Send in a Renewal

Send a prescription renewal request to the prescriber.

**Method:** POST

**Required Parameters:**
- Rx number

**Optional Parameters:**
- renewal_message: Message sent to prescriber electronically (e.g., "Patient is requesting 90 days supply")

**Demo Environment Note:**
- Electronic renewals are prevented in demo environment
- Only success or "renewal recently sent" failure responses will be returned
- Production environment may return additional failure messages in the same format

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Store Management**

```markdown
## Store Management

### Get Store Settings

Retrieve store settings including operating hours and delivery methods.

**Method:** GET

**Store Hours:**
- Hours are in store's local timezone
- Times expressed as 24-hour integer values
- Days of week represented as:
  | Integer Value | Day of Week |
  |---|---|
  | 0 | Monday |
  | 1 | Tuesday |
  | 2 | Wednesday |
  | 3 | Thursday |
  | 4 | Friday |
  | 5 | Saturday |
  | 6 | Sunday |

**Delivery Methods:**
| Method | Explanation |
|---|---|
| Delivery | Prescription delivered by pharmacy |
| Ship | Prescription shipped via UPS/USPS (integrated with DRX) |
| Pickup | Prescription held in waiting bin for customer pickup |

Response includes which delivery methods are enabled for the store.

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get a List of Stores

Retrieve a list of all stores.

**Method:** GET

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Shipping**

```markdown
## Shipping

### Get a List of Past Shipments

Retrieve a list of past shipments, sorted by creation date in descending order (not configurable).

**Method:** GET

**Query Parameters:**
- patient_id (optional): Filter shipments to a specific patient

**Sort Order:**
- Default: Shipment creation date (descending)
- Not configurable

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get Shipping Rates

Get available shipping rates and options for a package.

**Method:** POST

**Query Parameters:**
| Parameter | Description |
|---|---|
| patient_id | (Optional) Patient Primary Key |
| address_id | (Optional) Address Primary Key (must be associated with the patient) |

**Request Body:**
1. If address_id not provided, include address object:
   Required Fields:
   | Field | Definition |
   |---|---|
   | street | Street |
   | city | City |
   | state | State |
   | zip_code | Integer Zip Code |

   Optional Field:
   | Field | Definition |
   |---|---|
   | line_two | Address line two (defaults to empty string) |

2. If patient_id not provided:
   | Field | Definition |
   |---|---|
   | name | String. Name |

3. Package Information:
   Required (at least one):
   | Field | Definition |
   |---|---|
   | package_weight_pounds | Package weight in pounds |
   | package_weight_ounces | Package weight in ounces |

   Optional:
   | Field | Definition |
   |---|---|
   | signature_required | Boolean. Whether to require package signature |
   | carrier | String: 'fedex', 'ups', or 'usps' (if omitted, no carrier filter applied) |

**Response:**
Returns list of shipping options including:
- Service
- Expected delivery date
- Price
- Possible tracking number
- rate_id (use this in Generate Label endpoint)

**Notes:**
- If both addressId and patientId provided, address will be verified against patient
- Use returned rate_id with Generate Label endpoint to get downloadable label

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Generate Label

Generate a shipping label using a selected shipping rate.

**Method:** POST

**Query Parameters:**
- patient_id (optional): Link shipment with patient in database

**Required Fields:**
| Field | Definition |
|---|---|
| rate_id | Provided in the response of 'Get Shipping Rates' endpoint |

**Optional Fields:**
| Field | Definition |
|---|---|
| signature_required | Boolean. Whether to require signature |
| pos_event_id | Foreign key to link to a Point of Sale event |
| packing_list_id | Foreign key to link to a packing list |

**Notes:**
- Optional fields are useful for maintaining foreign key relationships in your database
- Use rate_id from the Get Shipping Rates endpoint response

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **SMS**

```markdown
## SMS

### Send SMS

Send an SMS message to any phone number.

**Method:** POST

**Required Fields:**
| Field | Definition |
|---|---|
| to | Phone Number as a String |
| body | Message to relay |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Tasks**

```markdown
## Tasks

### Get Task Status Updates

Get the status and details of a specific task.

**Method:** GET

**URL Parameter:**
- Unique task ID

**Response Details:**
- Completed files are uploaded to the pharmacy's object storage
- Files are guaranteed to be stored for 30 days (may persist longer)
- Complete file URL can be found in meta -> details -> path

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Start a New Task

Start a background task for bulk data exports to avoid paging limitations.

**Method:** POST

**Required Fields:**
| Field | Definition |
|---|---|
| task_name | Name of task to start (see available tasks) |
| start_date | Start date (if required by task) |
| end_date | End date (if required by task) |

**Optional Fields:**
| Field | Definition |
|---|---|
| fields | Desired fields in output |
| format | 'json' or 'csv' (defaults to JSON) |
| delimiter | Delimiter for CSV output |
| sold_after | Fills sold after this date |
| sold_before | Fills sold before this date |

**Available Tasks:**
| Task | Description | Required Parameters | Optional Parameters |
|---|---|---|---|
| fill_export | Bulk prescription fill data export. Returns same data as Look up a Prescription Fill endpoint by default. | start_date, end_date (for fill dates) | fields, format, delimiter, sold_after, sold_before |

**Available Fields for fill_export:**
[Extensive list of available fields including prescription details, patient information, doctor information, fill details, third party information, and store information - see full documentation for complete list]

**Response:**
- Success response includes task ID for status queries

**Status Codes:**
- 200: Success
- 400: Bad Request

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Third Party**

```markdown
## Third Party

### Add a Third Party

Add a third party insurance plan to a patient.

**Method:** POST

**URL Parameter:**
- Patient Primary Key

**Required Fields:**
| Field | Explanation |
|---|---|
| name | Plan Name |
| bin_number | Third Party Bin Number |

**Optional Fields:**
| Field | Explanation |
|---|---|
| pcn | Third Party PCN |
| group | Third Party Group |
| treat_as_cash | Boolean (defaults to false) |
| dir_fee_formula_id | Foreign key to a Dir Fee Formula |
| help_desk_number | Phone number format: "(123) 456-7890" |
| cardholder_id | Integer cardholder id |
| start_date | Valid isoformat date |
| end_date | Valid isoformat date |
| billing_order | "primary" or "false" |
| comments | String notes |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Transfers**

```markdown
## Transfers

### Look Up a Competing Pharmacy

Look up information about a competing pharmacy that you can send transfers to.

**Method:** GET

**URL Parameter:**
- Competing Pharmacy ID/NPI/DEA

**Description:**
Retrieves all information associated with a competing pharmacy when you have their ID saved in your database.

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get a List of Competing Pharmacies

Get a list of pharmacies that you can transfer prescriptions to.

**Method:** GET

**Query Parameters:**
| Parameter | Description |
|---|---|
| limit | Number of search results to return |
| offset | Offset for pagination |
| search | Filter by name, NPI, DEA, NCPDP, address, phone, or fax |

**Description:**
Use this endpoint to find the ID of a target pharmacy when you need to send a transfer.

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Add a Competing Pharmacy

Add a new pharmacy to your database for future transfers.

**Method:** POST

**Required Fields:**
| Field Name | Description |
|---|---|
| name | Name of the Competing Pharmacy |
| fax_number | String Fax Number in format: +11234567890 |

**Optional Fields:**
| Field Name | Description |
|---|---|
| npi | Pharmacy NPI |
| dea | Pharmacy DEA |
| ncpdp | Pharmacy NCPDP |
| phone | String Phone Number in format: +11234567890 |
| address | Pharmacy Address |
| city | Pharmacy City |
| state | Pharmacy State |
| zip_code | Pharmacy zip code |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Send a Transfer Out

Send a prescription transfer to another pharmacy.

**Method:** POST

**Pharmacy Identification (One Required):**
| Field Name | Description |
|---|---|
| id | Competing Pharmacy Primary Key |
| dea | Competing Pharmacy DEA |
| npi | Competing Pharmacy NPI |

**Transfer Object (Required - List of Objects):**
Each object must contain:
| Field Name | Description |
|---|---|
| prescription_id | Prescription Primary Key |
| qty | Quantity of the Prescription being transferred |

**Required Fields:**
| Field Name | Description |
|---|---|
| receiving_rph | Name of the Pharmacist receiving the transfer |
| transferring_rph | Name of the Pharmacist sending the transfer |

**Optional Fields:**
| Field Name | Description |
|---|---|
| fax_transfer | Boolean. If true, requires target pharmacy to have fax number |
| fax_number | String format: +11234567890 (will be saved to pharmacy if provided) |

**Create Pharmacy On-the-Fly:**
If pharmacy doesn't exist, you can create it by providing:
1. Required (One of):
   | Field Name | Description |
   |---|---|
   | dea | Competing Pharmacy DEA |
   | npi | Competing Pharmacy NPI |

2. Required:
   | Field Name | Description |
   |---|---|
   | name | Name of the Competing Pharmacy |

3. Optional:
   | Field Name | Description |
   |---|---|
   | fax_number | String format: +11234567890 |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

# **Webhooks**

```markdown
## Webhooks

### Look Up a Webhook

Look up a single webhook by its ID.

**Method:** GET

**URL Parameter:**
- Primary Key of the Webhook

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Get a List of Webhooks

Get a paginated list of your webhooks.

**Method:** GET

**Query Parameters:**
| Parameter | Description |
|---|---|
| limit | Number of records to return per page |
| offset | Offset of records for pagination |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Add a Webhook

Subscribe to a new webhook.

**Method:** POST

**Required Fields:**
| Field | Description |
|---|---|
| url | URL that we will send a POST request to |
| header_key | Key for authentication |
| header_value | Value for authentication |
| event | Event to subscribe to (create multiple webhooks for multiple events) |

**Available Events:**

1. **Prescription Fill Status Changes:**
| Event | Payload |
|---|---|
| Hold | Prescription Fill Object |
| Print | Prescription Fill Object |
| Scan | Prescription Fill Object |
| Rejected | Prescription Fill Object |
| Verify | Prescription Fill Object |
| OOS | Prescription Fill Object |
| Waiting Bin | Prescription Fill Object |
| Sold | Prescription Fill Object |
| Pre-Check | Prescription Fill Object |

2. **Prescription Events:**
| Event | Payload |
|---|---|
| Prescription Created | Prescription Object |

3. **Delivery Events:**
| Event | Payload |
|---|---|
| Delivery | Delivery Object |

4. **Miscellaneous Events:**
| Event | Description | Payload |
|---|---|---|
| Update Bin Location | Fires when Bin Location is chosen or updated | Prescription Fill Object |
| Confirm Pickup | Patient Prescriptions confirmed for pickup | Array of Selected Fill Objects |
| Return to Stock | Fires when Return to Stock button clicked in Waiting Bin | Array of Selected Prescription Objects |

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |

### Delete a Webhook

Delete an existing webhook.

**Method:** DELETE

**URL Parameter:**
- Webhook Primary Key to delete

**Status Codes:**
- 200: Success

Note: URL requests expire after 30 days.

| time | status | user agent |
|---|---|---|
| Make a request to see history. |
```

---

**End of Merged & Reformatted Document**