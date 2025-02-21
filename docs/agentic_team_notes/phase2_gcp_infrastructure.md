# Phase 2 – GCP Infrastructure Configuration

Total Estimated Hours: ≈ 44

This section covers creating a GCP project, configuring services, setting up Cloud SQL, networking/security, and validating everything. 

---

## Task Checklist

- [ ] **GCP project creation and billing configuration** (≈8 hours)
- [ ] **Enable key APIs and service setup** (≈4 hours)
- [ ] **Cloud SQL instance creation and initial schema design** (≈16 hours)
- [ ] **Secret Manager configuration and network/security settings** (≈12 hours)
- [ ] **Testing and validation** (≈4 hours)

---

### 1. GCP Project Creation and Billing Configuration (≈8 hours)

1. [ ] **Login to GCP Console**  
   - Go to [console.cloud.google.com](https://console.cloud.google.com).  
   - Confirm correct Google account with permissions to create projects.

2. [ ] **Create New Project**  
   - Click **Select a project** → **New Project**.  
   - Name it `superior-pharmacy-crm-prod`.  
   - Choose an organization if applicable or “No organization.”  
   - Note the **Project ID**.

3. [ ] **Link Billing**  
   - Go to **Billing** in the left menu.  
   - Ensure the newly created project is selected.  
   - Link to your billing account or create one if needed.

4. [ ] **Set Project Quotas** (optional)  
   - If you anticipate heavy usage, you might request increases for Cloud SQL connections or Cloud Run concurrency.  
   - Go to **IAM & Admin** → **Quotas** to check limits.

5. [ ] **Create Additional Projects** (optional)  
   - For dev/test/staging, replicate steps above to create `superior-pharmacy-crm-dev`, etc.  
   - Link them to billing.  
   - Document environment usage in `/docs/environments.md`.

---

### 2. Enable Key APIs and Service Setup (≈4 hours)

1. [ ] **Go to APIs & Services**  
   - In the left nav, click **APIs & Services** → **Dashboard**.  
   - Click **+ Enable APIs and Services**.

2. [ ] **Enable Required APIs**  
   - **Cloud Run**  
   - **Cloud Build**  
   - **Artifact Registry** (or Container Registry)  
   - **Cloud SQL Admin API**  
   - **Secret Manager**  
   - **Cloud Scheduler**  
   - **Pub/Sub** (if using for messaging)  
   - **Compute Engine** (implied, for underlying resources)  
   - Click **Enable** for each.

3. [ ] **Service Accounts**  
   - (Optional) Create specialized service accounts for deployment or to run Cloud Scheduler.  
   - Example: “cloud-run-deployer-sa”, “scheduler-trigger-sa”.  
   - Save JSON keys if needed, but recommended practice is to use IAM roles without exporting keys.

---

### 3. Cloud SQL Instance Creation and Initial Schema Design (≈16 hours)

1. [ ] **Navigate to Cloud SQL**  
   - In the left nav, choose **SQL** under Databases.  
   - Click **Create Instance** → **Choose PostgreSQL**.

2. [ ] **Configure PostgreSQL**  
   - **Instance ID**: `pharmacy-crm-postgres`.  
   - **Region**: choose a region near your pharmacy clients (e.g., `us-central1`).  
   - **Zone availability**: Single zone or multi-zone for high availability.  
   - **Machine Type**: Start with 2vCPU, 8GB memory for dev.  
   - **Storage**: 50GB SSD, auto-increase on.  
   - **Set root password** or use **IAM database authentication** (optional).

3. [ ] **Network Settings**  
   - If planning to connect from Cloud Run via private IP, select **Private IP**.  
   - Otherwise, use public IP but restrict with authorized networks or use the Cloud SQL Auth proxy.

4. [ ] **Create Database**  
   - After instance creation, go to **Databases** tab → **Create Database**.  
   - Name it `pharmacy_crm`.  
   - Alternatively, do it via a psql client: `CREATE DATABASE pharmacy_crm;`.

5. [ ] **Create DB User**  
   - In the **Users** tab, create a new user, e.g. `crm_admin`.  
   - Assign a strong password.

6. [ ] **Initial Schema**  
   - Use **Cloud Shell** or a local psql to connect:  
     ```bash
     gcloud sql connect pharmacy-crm-postgres --user=crm_admin
     ```
   - Execute SQL to create tables (or partial schema). For example:
     ```sql
     CREATE TABLE pharmacies (
       id SERIAL PRIMARY KEY,
       name VARCHAR(255),
       created_at TIMESTAMP DEFAULT NOW()
     );
     CREATE TABLE prescribers (
       id SERIAL PRIMARY KEY,
       npi VARCHAR(10) UNIQUE NOT NULL,
       full_name VARCHAR(255),
       specialty VARCHAR(255),
       created_at TIMESTAMP DEFAULT NOW()
     );
     -- Additional tables as per design
     ```

7. [ ] **Document Schema**  
   - Export as an SQL file (`schema_v1.sql`) in `/docs/db/`.  
   - Keep versioning so you can track schema changes.

8. [ ] **Test Connection**  
   - Optionally create a local test script or use Python’s `psycopg2` or Node’s `pg` library to connect.  
   - Verify you can do basic CRUD operations.

---

### 4. Secret Manager Configuration and Network/Security Settings (≈12 hours)

1. [ ] **Access Secret Manager**  
   - In the GCP Console, go to **Security** → **Secret Manager**.  
   - Click **Create Secret** → Name: `DB_PASSWORD`, value: the `crm_admin` password.  
   - Repeat for other secrets (like `DRX_API_KEY`, etc.).

2. [ ] **Grant Access to Service Accounts**  
   - For the Cloud Run service account, grant the `Secret Manager Secret Accessor` role for these secrets.  
   - You can do this in **IAM & Admin** → **IAM**, find the service account, click **Edit**, **Add Role**.

3. [ ] **Verify Access**  
   - Attempt to access a secret via the Cloud Shell with `gcloud secrets versions access latest --secret=DB_PASSWORD`.  
   - If authorized, you’ll see the secret. If not, fix IAM.

4. [ ] **VPC Connector (Optional)**  
   - If using private IP to connect to Cloud SQL, create a **VPC Connector** in **VPC Network** → **Serverless VPC Access**.  
   - Name it `connector-us-central1`.  
   - Assign a CIDR range (e.g., 10.8.0.0/28).  
   - This allows Cloud Run to talk to Cloud SQL on the private network.

5. [ ] **Firewall Rules**  
   - If using public IP, create firewall rules to allow only Cloud Run egress or your dev IP to connect to the SQL instance.  
   - Alternatively, keep it private IP only, eliminating the need for a public firewall rule.

6. [ ] **SSL/TLS**  
   - Optionally enforce SSL connections to the DB.  
   - Download client certs from Cloud SQL instance page if needed.  
   - Configure your application to use them.

---

### 5. Testing and Validation (≈4 hours)

1. [ ] **Smoke Test**  
   - Confirm you can connect to the database from a local environment or via the Cloud Shell.  
   - Attempt to read/write sample data.

2. [ ] **Check Logs**  
   - Go to **Logs Explorer**, filter by Cloud SQL.  
   - Ensure no errors about instance creation or blocked connections.

3. [ ] **Review Security**  
   - Confirm only authorized networks or private connections are enabled.  
   - No public IP if not needed.

4. [ ] **Close Phase 2**  
   - Mark tasks complete.  
   - Proceed to [Phase 3 – Core Application Development](./phase3_core_development.md).

