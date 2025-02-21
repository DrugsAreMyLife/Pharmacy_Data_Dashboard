# Phase 5 – DRX Integration (Deep Dive)

Total Estimated Hours: ≈ 40

Focuses on configuring DRX API access, implementing near real-time data sync, error handling, and final testing with a sandbox environment.

---

## Task Checklist

- [ ] **Configuring DRX API access and secure credential management** (≈8 hours)
- [ ] **Implement incremental, near real-time data sync and data mapping** (≈8 hours)
- [ ] **Process prescriber/prescription data with error handling and retries** (≈12 hours)
- [ ] **Testing using a sandbox environment & documenting** (≈8 hours)
- [ ] **Adding real-time update features** (≈4 hours)

---

### 1. Configuring DRX API Access & Secure Credential Management (≈8 hours)

1. [ ] **Obtain DRX Credentials**  
   - Each pharmacy on DRX must provide an API key (or Bearer token).  
   - Store these in your DB table `pharmacy_integrations` or similar.

2. [ ] **Register with DRX**  
   - If needed, register your application with DRX to get a client ID/secret.  
   - Follow DRX documentation for any OAuth flows.

3. [ ] **Store in Secret Manager**  
   - For each pharmacy, create a secret named `DRX_API_KEY_{pharmacyId}`.  
   - Or store them in the DB encrypted.  
   - Document in `/docs/integrations/drx_credentials.md`.

4. [ ] **Integration Config**  
   - In the Python integration service, ensure a function `get_drx_api_key(pharmacy_id)` that fetches from Secret Manager or DB.  
   - We want to keep these out of logs.

5. [ ] **Validate Connectivity**  
   - Test a sample request to DRX’s heartbeat endpoint:
     ```
     GET /heartbeat 
     Authorization: Bearer <API_KEY>
     ```
   - Log the response to confirm connectivity.

6. [ ] **Set up DRX base URL**  
   - Possibly `DRX_BASE_URL=https://api.drxdomain.com` as an env var in Cloud Run.  
   - This allows environment-specific overrides (sandbox vs prod).

---

### 2. Implement Incremental, Near Real-Time Data Sync (≈8 hours)

1. [ ] **DRX Endpoints**  
   - Consult DRX docs for:
     - `GET /doctor`: to fetch prescriber data.  
     - `GET /prescriptions`: or equivalent to fetch new scripts.  
   - Confirm availability or see if we must use `GET /patients` plus a sub-endpoint.

2. [ ] **Incremental Approach**  
   - Store a `last_synced_at` timestamp for each pharmacy.  
   - When calling DRX, pass `?updatedSince=<last_synced_at>` if DRX supports it.  
   - If not, pull all and filter.  
   - Only insert new or changed records.

3. [ ] **Polling Frequency**  
   - Consider scheduling the sync every 15-30 minutes in Cloud Scheduler.  
   - Or add an optional manual trigger from the Node API if user wants “Sync Now”.

4. [ ] **Mapping Data**  
   - DRX’s `doctor` endpoint likely returns `NPI`, `name`, `address`, `specialty`.  
   - Map to `prescribers` table. Use `ON CONFLICT (npi) DO UPDATE` to handle updates.  
   - For prescriptions, store them in a `prescriptions` table or increment counters in `prescriber_metrics`.

5. [ ] **Sync Function**  
   - In `drx_connector.py`:
     ```py
     def sync_drx(pharmacy_id):
         api_key = get_drx_api_key(pharmacy_id)
         # fetch new doctors
         # fetch new prescriptions
         # update DB
         # update last_synced_at
     ```
   - Return a summary, e.g., “10 new prescribers added, 50 new Rxs processed.”

6. [ ] **Testing on Small Data**  
   - Use a sandbox environment from DRX if available.  
   - Insert mock doctors/prescriptions, confirm they appear in our DB.

---

### 3. Process Prescriber/Prescription Data with Error Handling & Retries (≈12 hours)

1. [ ] **Network Faults**  
   - Wrap API calls in try/except. On `requests.exceptions.RequestException`, log error.  
   - Possibly retry up to 3 times with a small backoff (use `time.sleep` or the `tenacity` library).

2. [ ] **Validation**  
   - Ensure DRX data has `npi` and `name` fields. If missing, skip or store partial.  
   - If a record is invalid, log it.

3. [ ] **Database Transactions**  
   - Use transactions so partial updates can be rolled back on failure.  
   - For example, in psycopg2:
     ```py
     with conn:
       with conn.cursor() as cur:
         # do inserts
     ```
   - If an error occurs, the transaction is rolled back automatically.

4. [ ] **Partial Success**  
   - If prescribers fetch succeeds but prescriptions fetch fails, we still keep prescribers.  
   - Then mark partial success in the DB so we know we can retry the prescriptions fetch next run.

5. [ ] **Log Detailed Results**  
   - e.g., “Successfully updated 45 prescribers, inserted 102 prescription records, 2 errors.”  
   - Insert logs into a `integration_logs` table or GCP logging for analytics.

6. [ ] **Performance Considerations**  
   - Batch inserts if we have hundreds of records.  
   - Possibly parse JSON line by line if DRX returns large chunks.

7. [ ] **Security**  
   - Hide API key from logs. Only log masked data if needed.

---

### 4. Testing with Sandbox & Documenting Integration (≈8 hours)

1. [ ] **Sandbox Testing**  
   - Acquire DRX sandbox credentials or create a test pharmacy.  
   - Insert test doctors/prescriptions in DRX.  
   - Run `sync_drx(test_pharmacy_id)` manually.  
   - Verify DB updates.  
   - Simulate error conditions (invalid key, timeouts).

2. [ ] **Automated Tests**  
   - Add Pytest cases that mock DRX API responses.  
   - Ensure the connector code handles them correctly.

3. [ ] **Integration Docs**  
   - In `/docs/integrations/drx_integration.md`, detail:  
     - How to set DRX API key for a pharmacy,  
     - How often it syncs,  
     - Potential errors and solutions.  
     - Step-by-step for re-syncing if needed.

4. [ ] **Sign-Off**  
   - Have a final review of the DRX integration by QA or lead dev.  
   - Ensure it meets the near-real-time goal (e.g., tested at 15-min intervals).

---

### 5. Adding Real-Time Update Features (≈4 hours)

1. [ ] **WebSocket or SSE**  
   - In the Node API, implement a WebSocket or SSE endpoint: `/api/live-updates`.  
   - On each successful DRX sync, broadcast a message: “Pharmacy X updated. Dr. Smith has 2 new Rxs.”

2. [ ] **React Integration**  
   - In the front-end, open the SSE/WebSocket connection on login.  
   - Show a small notification or refresh the prescriber list when a “sync complete” event arrives.

3. [ ] **Testing**  
   - Manually trigger sync, watch front-end for real-time updates.  
   - Confirm minimal latency.

4. [ ] **Documentation**  
   - Update the front-end docs to mention real-time functionality.  
   - Outline how to subscribe/unsubscribe.

---

## Conclusion

By completing Phase 5, you will have a robust DRX integration that synchronizes prescriber and prescription data in near-real time, handles errors gracefully, and updates front-end users in real time.

**At this point, the Superior Pharmacy CRM should be feature-complete** for DRX-based pharmacies. Future expansions for other PMS integrations will follow a similar pattern, thanks to this modular architecture.

