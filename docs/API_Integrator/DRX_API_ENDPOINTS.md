# DRX API ENDPOINTS - IMMUTABLE REFERENCE

⚠️ **PROTECTED SECTION - DO NOT MODIFY** ⚠️
===============================================

## Demo Environment Configuration
```
Base URL: https://demo.drxapp.com
API Path: /external_api/v1
Authentication: X-DRX-Key header
Store Slug: demo
```

## ✅ VERIFIED WORKING ENDPOINTS

### System
1. **Heartbeat**
   - Method: GET
   - Endpoint: `/heartbeat`
   - Status: 200 ✓
   - Parameters: None
   - Response: Health status object

### Inventory Management
1. **Get All Inventory**
   - Method: GET
   - Endpoint: `/inventory`
   - Status: 200 ✓
   - Parameters:
     * as_of_date (optional): ISO 8601 date
   - Response: Array of inventory items with quantities

2. **List Items**
   - Method: GET
   - Endpoint: `/items`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * ndc (string, optional): Filter by NDC code
     * gcn (string, optional): Filter by GCN
     * item_type (string, optional): Filter by type (e.g., "MEDICATION")
   - Response: Paginated list of items

### Store Management
1. **Get Store Settings**
   - Method: GET
   - Endpoint: `/settings`
   - Status: 200 ✓
   - Parameters: None
   - Response: Store configuration object

2. **List Stores**
   - Method: GET
   - Endpoint: `/stores`
   - Status: 200 ✓
   - Parameters: None
   - Response: Array of store objects

### Address Management
1. **List Addresses**
   - Method: GET
   - Endpoint: `/addresses`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * type (string, optional): "billing" or "shipping"
     * city (string, optional)
     * state (string, optional)
     * country (string, optional)
   - Response: Paginated list of addresses

### Medical Records
1. **List Allergies**
   - Method: GET
   - Endpoint: `/allergies`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * category (string, optional): "medication" or "food"
     * severity (string, optional): "mild", "moderate", or "severe"
     * search (string, optional): Search allergy descriptions
   - Response: Paginated list of allergies

2. **List Claims**
   - Method: GET
   - Endpoint: `/claims`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * before_date (string, optional): ISO 8601 datetime
     * after_date (string, optional): ISO 8601 datetime
   - Response: Paginated list of claims

### Delivery System
1. **List Deliveries**
   - Method: GET
   - Endpoint: `/deliveries`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * route (string, optional): Filter by route code
     * date (string, optional): ISO 8601 date
     * external_id (string, optional): External reference ID
   - Response: Paginated list of deliveries

2. **List Delivery Routes**
   - Method: GET
   - Endpoint: `/deliveries/routes`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
   - Response: Paginated list of delivery routes

### Healthcare Providers
1. **Get Transfer Pharmacies**
   - Method: GET
   - Endpoint: `/transfer`
   - Status: 200 ✓
   - Description: Find pharmacies for prescription transfers
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * q (string, optional): Search by name/NPI/DEA/NCPDP/address/phone/fax
   - Response:
     * success (boolean): Operation status
     * message (string): Response message
     * competing_pharmacies (array): List of pharmacy objects containing:
       - id (integer)
       - created_at (string, ISO 8601)
       - updated_at (string, ISO 8601)
       - name (string)
       - npi (string)
       - ncpdp (string)
       - phone (string)
       - fax (string)
       - address (string)
       - city (string)
       - state (string)
       - zip_code (string)
       - dea (string)
       - surescripts_spi (string)

2. **List Doctors**
   - Method: GET
   - Endpoint: `/doctors`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * q (string, optional): Search by name/DOB/phone/NPI/DEA
   - Response: Paginated list of doctors

3. **Search Provider Catalog**
   - Method: GET
   - Endpoint: `/doctors/search`
   - Status: 200 ✓
   - Parameters:
     * first_name (string, optional)
     * last_name (string, optional)
     * npi (string, optional): NPI number
     * dea (string, optional): DEA number
     * state (string, optional): State code
   - Response: List of matching providers

### Patient Management
1. **List Patients**
   - Method: GET
   - Endpoint: `/patients`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * search (string, optional): General search term
     * q (string, optional): Quick search by name/DOB/phone
     * before_date (string, optional): ISO 8601 datetime
     * after_date (string, optional): ISO 8601 datetime
     * facility_id (int32, optional)
   - Response: Paginated list of patients

### Contact Information
1. **List Phone Numbers**
   - Method: GET
   - Endpoint: `/phone_numbers`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * search (string, optional): General search term
     * q (string, optional): Quick search by number/area code
   - Response: Paginated list of phone numbers

### Prescription Management
1. **List Prescription Fills**
   - Method: GET
   - Endpoint: `/prescription-fills`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * patient_id (int32, optional): Filter by patient
     * before_date (string, optional): ISO 8601 datetime
     * after_date (string, optional): ISO 8601 datetime
     * status (string, optional): Filter by status
     * fills_in_progress (boolean, optional): Show only in-progress fills
   - Response:
     * success (boolean): Operation status
     * message (string): Response message
     * total (integer): Total number of fills
     * fills (array): List of fill objects containing:
       - patient: Patient information (id, first_name, last_name, easy_open, date_of_birth)
       - id (integer)
       - prescription_id (integer)
       - fill_date (string, ISO 8601)
       - status (string)
       - quantity (integer)
       - days_supply (integer)
       - refills_remaining (integer)
       - last_filled_date (string, ISO 8601)
       - next_fill_date (string, ISO 8601)
       - notes (string, optional)
       - created_at (string, ISO 8601)
       - updated_at (string, ISO 8601)

2. **List Prescriptions**
   - Method: GET
   - Endpoint: `/prescriptions`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * patient_id (int32, optional)
     * status (string, optional): Filter by status
       - Valid statuses: "Hold", "Waiting Bin", "Sold", "Print", "Verify", "Scan", "Adjudicating", "OOS"
       - Note: "Rejected" status returns 500 error
     * facility_id (int32, optional)
     * ehr_message_id (string, optional)
     * ehr_order_number (string, optional)
     * expiration_date (string, optional): ISO 8601 date
     * before_date (string, optional): ISO 8601 datetime
     * after_date (string, optional): ISO 8601 datetime
   - Response: Paginated list of prescriptions

3. **List Rejected Prescriptions**
   - Method: GET
   - Endpoint: `/prescriptions`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
     * status: "Rejected" (string, required)
     * patient_id (int32, optional)
     * before_date (string, optional): ISO 8601 datetime
     * after_date (string, optional): ISO 8601 datetime
     * facility_id (int32, optional)
     * ehr_message_id (string, optional)
     * ehr_order_number (string, optional)
   - Response:
     * success (boolean): Operation status
     * total (integer): Total number of prescriptions
     * prescriptions (array): List of rejected prescriptions containing:
       - id (integer)
       - patient_id (integer)
       - prescriber_id (integer)
       - medication: Drug details (name, ndc, strength, form)
       - sig (string): Instructions
       - quantity (integer)
       - days_supply (integer)
       - refills (integer)
       - written_date (string, ISO 8601)
       - rejection_date (string, ISO 8601)
       - rejection_reason (string)
       - rejection_code (string)
       - rejection_notes (string)
       - rejected_by (string)
       - facility_id (integer)
       - ehr_message_id (string)
       - ehr_order_number (string)
       - created_at (string, ISO 8601)
       - updated_at (string, ISO 8601)

### Fill Management
1. **List Fill Tags**
   - Method: GET
   - Endpoint: `/fill-tags`
   - Status: 200 ✓
   - Description: Get list of tags associated with prescription fills
   - Parameters:
     * limit (int32, optional, defaults to 10)
     * offset (int32, optional, defaults to 10)
     * tag_name (string, optional): Filter tags by name (partial matches allowed)
     * prescription_fill_id (int32, optional): Filter by specific fill ID
   - Response:
     * success (boolean): Operation status
     * message (string): Response message
     * total (integer): Total number of tags
     * fill_tags (array): List of tag objects containing:
       - id (integer)
       - name (string)
       - prescription_fills (array): Associated fills containing:
         * prescription_fill_id (integer)

### Task Management
1. **List Tasks**
   - Method: GET
   - Endpoint: `/tasks`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
   - Response: Paginated list of tasks

### Webhook Management
1. **List Webhooks**
   - Method: GET
   - Endpoint: `/webhooks`
   - Status: 200 ✓
   - Parameters:
     * limit (int32, optional, default: 10)
     * offset (int32, optional, default: 0)
   - Response: Paginated list of webhook configurations

⚠️ **END PROTECTED SECTION** ⚠️
===============================

Note: This document serves as an immutable reference for verified working endpoints in the demo environment. Any modifications to this section must go through proper change management procedures.