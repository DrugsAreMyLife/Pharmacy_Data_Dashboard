# API Test Results

Test Run: 2025-02-19 16:41:45

## Summary

- Total Tests: 200
- Successful: 127
- Failed: 73

## Detailed Results

### Get

| Endpoint | Method | Parameters | Status | Result |
|----------|---------|------------|---------|----------|
| Get All Inventory | GET | None | 200 ✅ | Success |
| Get All Inventory with Date | GET | {"as_of_date": "2025-02-19"}... | 200 ✅ | Success |
| Get Item Inventory History | GET | {"item_id": "12345"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| Get Item Inventory History | GET | {"item_id": "12345", "start_date": "2025-02-18", "... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| Get Item Inventory History | GET | {"item_id": "12345", "includeEquivalents": "true"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| Get Store Settings | GET | None | 200 ✅ | Success |

### Heartbeat

| Endpoint | Method | Parameters | Status | Result |
|----------|---------|------------|---------|----------|
| Heartbeat | GET | None | 200 ✅ | Success |

### List

| Endpoint | Method | Parameters | Status | Result |
|----------|---------|------------|---------|----------|
| List Addresses | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Addresses | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Addresses | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Addresses | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Addresses | GET | {"type": "billing"}... | 200 ✅ | Success |
| List Addresses | GET | {"type": "shipping"}... | 200 ✅ | Success |
| List Addresses | GET | {"city": "Austin"}... | 200 ✅ | Success |
| List Addresses | GET | {"state": "TX"}... | 200 ✅ | Success |
| List Addresses | GET | {"country": "US"}... | 200 ✅ | Success |
| List Addresses | GET | {"limit": "10", "offset": "0", "type": "billing", ... | 200 ✅ | Success |
| List Allergies | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Allergies | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Allergies | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Allergies | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Allergies | GET | {"category": "medication"}... | 200 ✅ | Success |
| List Allergies | GET | {"category": "food"}... | 200 ✅ | Success |
| List Allergies | GET | {"severity": "mild"}... | 200 ✅ | Success |
| List Allergies | GET | {"severity": "moderate"}... | 200 ✅ | Success |
| List Allergies | GET | {"severity": "severe"}... | 200 ✅ | Success |
| List Allergies | GET | {"search": "test"}... | 200 ✅ | Success |
| List Allergies | GET | {"search": ""}... | 200 ✅ | Success |
| List Allergies | GET | {"search": "a"}... | 200 ✅ | Success |
| List Allergies | GET | {"search": "test test"}... | 200 ✅ | Success |
| List Charge Accounts | GET | {"limit": "10", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Charge Accounts | GET | {"limit": "1", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Charge Accounts | GET | {"limit": "100", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Charge Accounts | GET | {"limit": "10", "offset": "10"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Claims | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Claims | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Claims | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Claims | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Claims | GET | {"before_date": "2025-02-19T00:00:00Z"}... | 200 ✅ | Success |
| List Claims | GET | {"after_date": "2025-02-19T00:00:00Z"}... | 200 ✅ | Success |
| List Claims | GET | {"before_date": "2025-02-19T00:00:00Z", "after_dat... | 200 ✅ | Success |
| List Competing Pharmacies | GET | {"limit": "10", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"limit": "1", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"limit": "100", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"limit": "10", "offset": "10"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"search": "test"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"search": ""}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"search": "a"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"search": "test test"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"search": "CVS"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"search": "1234567890"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"search": "AB1234567"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Competing Pharmacies | GET | {"search": "NCPDP123"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Deliveries | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Deliveries | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Deliveries | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Deliveries | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Deliveries | GET | {"route": "ROUTE1"}... | 200 ✅ | Success |
| List Deliveries | GET | {"date": "2025-02-19"}... | 200 ✅ | Success |
| List Deliveries | GET | {"external_id": "TEST-ID"}... | 200 ✅ | Success |
| List Deliveries | GET | {"limit": "10", "offset": "0", "route": "ROUTE1", ... | 200 ✅ | Success |
| List Delivery Routes | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Delivery Routes | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Delivery Routes | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Delivery Routes | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Doctors | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Doctors | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Doctors | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Doctors | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Doctors | GET | {"q": "01201986"}... | 200 ✅ | Success |
| List Doctors | GET | {"q": "5852984455"}... | 200 ✅ | Success |
| List Doctors | GET | {"q": "nau,ron"}... | 200 ✅ | Success |
| List Doctors | GET | {"q": "naugle"}... | 200 ✅ | Success |
| List Doctors | GET | {"q": "5852984455"}... | 200 ✅ | Success |
| List Doctors | GET | {"q": "1234567890"}... | 200 ✅ | Success |
| List Doctors | GET | {"q": "AB1234567"}... | 200 ✅ | Success |
| List Fill Tags | GET | {"limit": "10", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Fill Tags | GET | {"limit": "1", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Fill Tags | GET | {"limit": "100", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Fill Tags | GET | {"limit": "10", "offset": "10"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Fill Tags | GET | {"name": "urgent"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Fill Tags | GET | {"fill_id": "12345"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Fill Tags | GET | {"limit": "10", "offset": "0", "name": "urgent"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Items | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Items | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Items | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Items | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Items | GET | {"ndc": "111"}... | 200 ✅ | Success |
| List Items | GET | {"gcn": "12345"}... | 200 ✅ | Success |
| List Items | GET | {"item_type": "MEDICATION"}... | 200 ✅ | Success |
| List Items | GET | {"limit": "10", "offset": "0", "ndc": "111", "item... | 200 ✅ | Success |
| List Packing Lists | GET | {"limit": "10", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Packing Lists | GET | {"limit": "1", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Packing Lists | GET | {"limit": "100", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Packing Lists | GET | {"limit": "10", "offset": "10"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Past Shipments | GET | {"limit": "10", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Past Shipments | GET | {"limit": "1", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Past Shipments | GET | {"limit": "100", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Past Shipments | GET | {"limit": "10", "offset": "10"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Past Shipments | GET | {"patient_id": "12345"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Patients | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Patients | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Patients | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Patients | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Patients | GET | {"search": "test"}... | 200 ✅ | Success |
| List Patients | GET | {"search": ""}... | 200 ✅ | Success |
| List Patients | GET | {"search": "a"}... | 200 ✅ | Success |
| List Patients | GET | {"search": "test test"}... | 200 ✅ | Success |
| List Patients | GET | {"before_date": "2025-02-19T00:00:00Z"}... | 200 ✅ | Success |
| List Patients | GET | {"after_date": "2025-02-19T00:00:00Z"}... | 200 ✅ | Success |
| List Patients | GET | {"before_date": "2025-02-19T00:00:00Z", "after_dat... | 200 ✅ | Success |
| List Patients | GET | {"facility_id": "12345"}... | 200 ✅ | Success |
| List Patients | GET | {"q": "01201986"}... | 200 ✅ | Success |
| List Patients | GET | {"q": "5852984455"}... | 200 ✅ | Success |
| List Patients | GET | {"q": "smith,john"}... | 200 ✅ | Success |
| List Patients | GET | {"q": "smith"}... | 200 ✅ | Success |
| List Phone Numbers | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Phone Numbers | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Phone Numbers | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Phone Numbers | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Phone Numbers | GET | {"search": "test"}... | 200 ✅ | Success |
| List Phone Numbers | GET | {"search": ""}... | 200 ✅ | Success |
| List Phone Numbers | GET | {"search": "a"}... | 200 ✅ | Success |
| List Phone Numbers | GET | {"search": "test test"}... | 200 ✅ | Success |
| List Phone Numbers | GET | {"q": "5852984455"}... | 200 ✅ | Success |
| List Phone Numbers | GET | {"q": "585"}... | 200 ✅ | Success |
| List Prescription Fills | GET | {"limit": "10", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"limit": "1", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"limit": "100", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"limit": "10", "offset": "10"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"before_date": "2025-02-19T00:00:00Z"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"after_date": "2025-02-19T00:00:00Z"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"before_date": "2025-02-19T00:00:00Z", "after_dat... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"fills_in_progress": "true"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"status": "Hold"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"status": "Waiting Bin"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"status": "Sold"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"status": "Print"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"status": "Rejected"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"status": "Verify"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"status": "Scan"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"status": "Adjudicating"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"status": "OOS"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"patient_id": "12345"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescription Fills | GET | {"limit": "10", "offset": "0", "patient_id": "1234... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Prescriptions | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"patient_id": "12345"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"status": "Hold"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"status": "Waiting Bin"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"status": "Sold"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"status": "Print"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"status": "Rejected"}... | 500 ❌ | {"message": "Internal Server Error"} |
| List Prescriptions | GET | {"status": "Verify"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"status": "Scan"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"status": "Adjudicating"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"status": "OOS"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"facility_id": "12345"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"ehr_message_id": "MSG123"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"ehr_order_number": "ORD123"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"expiration_date": "2025-02-19"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"before_date": "2025-02-19T00:00:00Z"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"after_date": "2025-02-19T00:00:00Z"}... | 200 ✅ | Success |
| List Prescriptions | GET | {"before_date": "2025-02-19T00:00:00Z", "after_dat... | 200 ✅ | Success |
| List Prescriptions | GET | {"limit": "10", "offset": "0", "patient_id": "1234... | 200 ✅ | Success |
| List Sale Events | GET | {"limit": "10", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Sale Events | GET | {"limit": "1", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Sale Events | GET | {"limit": "100", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Sale Events | GET | {"limit": "10", "offset": "10"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Stores | GET | None | 200 ✅ | Success |
| List SureScripts | GET | {"limit": "10", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"limit": "1", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"limit": "100", "offset": "0"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"limit": "10", "offset": "10"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"showOldItems": "true"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"showOldItems": "false"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"external_id": "EXT123"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"search": "test"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"search": ""}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"search": "a"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"search": "test test"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"ehrMessageId": "MSG123"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"ehrOrderNumber": "ORD123"}... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List SureScripts | GET | {"limit": "10", "offset": "0", "showOldItems": "tr... | 404 ❌ | {"message": "The requested URL was not found on the server. If you entered the URL manually please c... |
| List Tasks | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Tasks | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Tasks | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Tasks | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |
| List Webhooks | GET | {"limit": "10", "offset": "0"}... | 200 ✅ | Success |
| List Webhooks | GET | {"limit": "1", "offset": "0"}... | 200 ✅ | Success |
| List Webhooks | GET | {"limit": "100", "offset": "0"}... | 200 ✅ | Success |
| List Webhooks | GET | {"limit": "10", "offset": "10"}... | 200 ✅ | Success |

### Search

| Endpoint | Method | Parameters | Status | Result |
|----------|---------|------------|---------|----------|
| Search Provider Catalog | GET | {"first_name": "John"}... | 200 ✅ | Success |
| Search Provider Catalog | GET | {"last_name": "Smith"}... | 200 ✅ | Success |
| Search Provider Catalog | GET | {"npi": "1234567890"}... | 200 ✅ | Success |
| Search Provider Catalog | GET | {"dea": "AB1234567"}... | 200 ✅ | Success |
| Search Provider Catalog | GET | {"state": "TX"}... | 200 ✅ | Success |
| Search Provider Catalog | GET | {"limit": "10", "offset": "0", "first_name": "John... | 200 ✅ | Success |

