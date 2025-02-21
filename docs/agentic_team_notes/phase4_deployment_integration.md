# Phase 4 – Deployment & Integration

Total Estimated Hours: ≈ 44

Covers packaging the Node.js and Python services in Docker, deploying to Cloud Run, setting up Cloud Scheduler, domain mapping, and final system tests.

---

## Task Checklist

- [ ] **Dockerizing Node.js and Python services, pushing images** (≈16 hours)
- [ ] **Deploying services to Cloud Run with scaling, networking, secrets** (≈16 hours)
- [ ] **Configuring Cloud Scheduler, domain mapping, CDN** (≈8 hours)
- [ ] **End-to-end testing and validation** (≈4 hours)

---

### 1. Dockerizing Node.js and Python Services (≈16 hours)

1. [ ] **Dockerfile for Node**  
   - In `backend-node/`, create `Dockerfile`:
     ```dockerfile
     FROM node:18-alpine as build
     WORKDIR /app
     COPY package*.json ./
     RUN npm ci
     COPY . .
     RUN npm run build  # if using TS or bundling

     FROM node:18-alpine
     WORKDIR /app
     COPY --from=build /app ./
     EXPOSE 8080
     CMD ["node", "dist/index.js"]  # or whichever start command
     ```
   - Test by running `docker build -t node-backend .` then `docker run -p 8080:8080 node-backend`.

2. [ ] **Dockerfile for Python**  
   - In `integrations-python/`, create `Dockerfile`:
     ```dockerfile
     FROM python:3.11-slim
     WORKDIR /app
     COPY requirements.txt ./
     RUN pip install --no-cache-dir -r requirements.txt
     COPY . .
     EXPOSE 8000
     CMD ["python", "app.py"]
     ```
   - Test similarly with `docker build` and `docker run`.

3. [ ] **Tag & Push to Artifact Registry**  
   - In GCP, create an Artifact Registry repo:
     ```bash
     gcloud artifacts repositories create pharmacy-repo --repository-format=docker --location=us-central1
     ```
   - Configure Docker to use `gcloud` as a credential helper.
   - Tag images: `docker tag node-backend us-central1-docker.pkg.dev/PROJECT_ID/pharmacy-repo/node-backend:latest`
   - Push: `docker push us-central1-docker.pkg.dev/PROJECT_ID/pharmacy-repo/node-backend:latest`
   - Repeat for Python integration image.

4. [ ] **Automate with Cloud Build** (optional)  
   - Create a `cloudbuild.yaml` to build and push images on each commit.  
   - Example snippet:
     ```yaml
     steps:
       - name: 'gcr.io/cloud-builders/docker'
         args: ['build', '-t', 'us-central1-docker.pkg.dev/$PROJECT_ID/pharmacy-repo/node-backend:$COMMIT_SHA', '.']
       - name: 'gcr.io/cloud-builders/docker'
         args: ['push', 'us-central1-docker.pkg.dev/$PROJECT_ID/pharmacy-repo/node-backend:$COMMIT_SHA']
     images:
       - 'us-central1-docker.pkg.dev/$PROJECT_ID/pharmacy-repo/node-backend:$COMMIT_SHA'
     ```
   - Configure triggers in Cloud Build settings.

---

### 2. Deploying Services to Cloud Run (≈16 hours)

1. [ ] **Node Backend Deployment**  
   - In GCP Console, go to **Cloud Run** → **Create Service**.  
   - Select the image `us-central1-docker.pkg.dev/PROJECT_ID/pharmacy-repo/node-backend:latest`.  
   - Set service name `pharmacy-node-api`.  
   - Choose `us-central1` region.  
   - Under **Advanced Settings** → **Connections**, add the Cloud SQL instance if needed.  
   - Under **Environment Variables**, set `DB_CONNECTION_STRING`, etc. or use Secrets.  
   - Allow unauthenticated access if you want public API (or require IAM if you prefer).  
   - Click **Deploy**.

2. [ ] **Integration Service Deployment**  
   - Similarly, create service `pharmacy-integrations`.  
   - Possibly **disable** unauthenticated access so only internal calls or Cloud Scheduler can invoke.  
   - Provide environment variables for DB connection, etc.  
   - Deploy.

3. [ ] **Test**  
   - Access the Node service URL from the console output.  
   - e.g., `https://pharmacy-node-api-xxx-uc.a.run.app/api/health`.  
   - Should return “OK” if the route is working.  
   - For the integrations service, try `GET /health` if publicly accessible or from an authorized request.

4. [ ] **Scaling and Concurrency**  
   - In **Cloud Run** → **pharmacy-node-api** → **Edit & Deploy** → set concurrency to 80.  
   - Set min instances = 0 (to save cost) or 1 if you need always warm.  
   - Do the same for the Python service as needed.

5. [ ] **Secret Access**  
   - If using Secret Manager references, go to **Variables & Secrets** tab in Cloud Run.  
   - Add a secret reference for `DB_PASSWORD` or others.  
   - In your code, ensure you read them from the correct env var.

---

### 3. Configuring Cloud Scheduler, Domain Mapping, and CDN (≈8 hours)

1. [ ] **Cloud Scheduler**  
   - Go to **Cloud Scheduler** → **Create job**.  
   - Name: `nightly-integration-sync`, schedule: `0 2 * * *`.  
   - Target: HTTP, URL = `https://pharmacy-integrations-xxx-uc.a.run.app/sync-all` (assuming you created a `/sync-all` route).  
   - Select **Service Account** with `Cloud Run Invoker` role if the service is protected.  
   - Save, test run.

2. [ ] **Domain Mapping**  
   - If you own a custom domain, go to **Cloud Run** → **Manage Custom Domains**.  
   - Map domain `api.mypharmacycrm.com` to the Node service.  
   - Add DNS records as instructed.  
   - Wait for propagation, then test `https://api.mypharmacycrm.com/health`.

3. [ ] **CDN for Front-End**  
   - If hosting the React build in Cloud Storage, enable **Static Website** on the bucket.  
   - Enable **Cloud CDN** in the **Load Balancing** section, point to that bucket.  
   - Or use **Firebase Hosting**: `firebase init hosting` in `frontend-react`, then `firebase deploy`.  
   - Confirm the front-end calls the correct API domain via `.env.production`.

---

### 4. End-to-End Testing and Validation (≈4 hours)

1. [ ] **Run E2E Tests**  
   - From local or staging environment, create a new user, login, check prescribers.  
   - Confirm integrations can fetch data from PMS (simulate with test credentials).

2. [ ] **Check Logs**  
   - In **Cloud Logging**, filter by `pharmacy-node-api`.  
   - Confirm no critical errors.  
   - Check integration logs too.

3. [ ] **Validate Security**  
   - Attempt unauthorized call to protected integration endpoint. Should fail.  
   - Confirm JWT endpoints require correct tokens.

4. [ ] **Sign Off**  
   - Mark tasks complete, proceed to [Phase 5 – DRX Integration (Deep Dive)](./phase5_drx_integration.md).

