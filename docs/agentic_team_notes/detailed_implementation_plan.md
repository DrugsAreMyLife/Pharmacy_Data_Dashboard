# Detailed Implementation Plan for Pharmacy Data Dashboard

This document combines and updates the ultra granular task breakdown from Phases 1–5 (as detailed in the respective phase files) and incorporates production-ready API integration details from the API_Integrator subfolder. It provides an atomic step-by-step roadmap for a fully functional product that performs a daily ingestion of new data from the pharmacy management system and presents that data via elegant graphs, charts, and metrics. All tasks are accompanied by checkboxes and estimated times to guide the agentic programming team.

---

## Phase 1: Project Setup and Requirements  
**Estimated Total: ~13 hours**

### 1.1 Repository & Documentation Setup
- [ ] **Create Remote Repository** (2h)
  - Set up a new repository (e.g., on GitHub) and configure branch protection rules.
- [ ] **Clone Repository & Initial Setup** (1h)
  - Clone the repository, initialize local environment, create a proper .gitignore.
- [ ] **Establish Core Documentation** (1h)
  - Create README, PROJECT_IMPLEMENTATION_PLAN.md, and design docs.
  - Merge contents from *docs/agentic_team_notes/README.md*.
  
### 1.2 Requirements & Feature Analysis  
- [ ] **Define & Document Features** (2h)
  - List required modules:
    - Prescriber CRM with search, filtering, and notes.
    - Dashboard for RX, prescriber, and drug metrics (beautiful graphs/charts).
    - Daily data ingestion from the pharmacy management system.
    - Integration interfaces per API_Integrator guidelines.
- [ ] **Set Acceptance Criteria & User Stories** (2h)
  - Example: “Data from PMS appears in CRM within 1 hour; charts update daily.”
- [ ] **Finalize Requirements Documentation** (2h)
  - Consolidate requirements with input from API_Integrator (review API documentation, configuration, and endpoint details).

---

## Phase 2: Google Cloud Infrastructure Setup  
**Estimated Total: ~13.5 hours**

### 2.1 GCP Project & API Enablement
- [ ] **Create and Configure GCP Project ("pharmacy-crm-prod")** (1h)
  - Set up the project, enable billing, and assign IAM roles.
- [ ] **Enable Required GCP APIs** (1h)
  - APIs: Cloud Run, Cloud Build, Artifact Registry, Cloud SQL Admin, Secret Manager, Cloud Monitoring, Cloud Pub/Sub.
- [ ] **Verify Service Activation** (0.5h)

### 2.2 Cloud SQL Instance & Schema Deployment
- [ ] **Provision Cloud SQL (PostgreSQL)** (2h)
  - Choose configuration (e.g., 2 vCPU, 8GB RAM) and set auto-storage increase.
- [ ] **Design & Document Database Schema** (2h)
  - Tables: pharmacy, prescriber, prescriber_pharmacy_data, user, prescription.
- [ ] **Deploy SQL Scripts via Cloud Shell** (2h)

### 2.3 Secret Management and Networking  
- [ ] **Configure Secret Manager** (1h)
  - Create secrets for sensitive keys: DB_PASSWORD, DRX_API_KEY, BESTRX_API_KEY, etc.
- [ ] **Set Up Networking & VPC Connector (if required)** (2h)
  - Secure Cloud SQL access with authorized networks, set up VPC connectors for Cloud Run.

---

## Phase 3: Core Application Development  
**Estimated Total: ~48.5 hours**

### 3.1 Back-End API (Node.js)
- [ ] **Bootstrap Node.js Project and Install Dependencies** (2h)
  - Use Express, pg, dotenv, cors, bcrypt, jsonwebtoken, etc.
- [ ] **Implement Basic Express Server & Health Endpoint** (1h)
- [ ] **Develop Core API Endpoints** (8h)
  - Endpoints:
    - GET /api/prescribers
    - GET /api/prescribers/:id 
    - POST /api/prescribers/:id/note 
    - GET /api/analytics/overview 
    - GET /api/trigger-scrape (integrates with production API calls)
- [ ] **Integrate Persistent Storage (Cloud SQL)** (4h)
  - Establish connection pooling and write parameterized SQL queries.
- [ ] **Authentication & Authorization Module** (4h)
  - JWT-based authentication; secure password handling via bcrypt.
- [ ] **Unit & Integration Testing (Jest)** (3h)

### 3.2 Integration Services (Python/Flask)
- [ ] **Bootstrap Python/Flask Project** (1h)
  - Create project, set up virtual environment.
- [ ] **Install Flask, requests, SQLAlchemy, etc.** (1h)
- [ ] **Implement a Production-Ready Data Ingestion Function** (8h)
  - Remove simulation; integrate real API calls using endpoints and guidelines in *docs/API_Integrator/DRX_API_ENDPOINTS.md*.
  - Process and normalize data to update metrics (rxCount, prescriberCount, drugStats).
- [ ] **Develop Integration Manager & Connector Classes** (4h)
  - Create a base class and vendor-specific implementations (e.g., DRX, BestRx).
- [ ] **Unit and Functional Testing for Integration Logic** (3h)

### 3.3 Front-End (React)
- [ ] **Bootstrap React Project (using Create React App with TypeScript)** (1h)
- [ ] **Set Up Project Structure, Routing, and State Management** (2h)
  - Utilize React Router and Context/Redux.
- [ ] **Develop Key UI Components** (6h)
  - Components: PrescriberTable, PrescriberCard, MetricsChart.
- [ ] **Implement Pages for Dashboard and Detailed Views** (6h)
  - Pages: Login, Prescriber List, Prescriber Detail, Analytics.
- [ ] **Integration with Back-End via API Service Layer** (4h)
  - Manage API calls with proper error handling and auth.
- [ ] **Testing and Linting for React Components** (2h)

### 3.4 Daily Data Ingestion & Reporting
- [ ] **Implement Daily Ingestion Scheduler (using Cloud Scheduler or Cron in production)** (4h)
  - Automatically invoke integration functions to retrieve fresh data each day.
- [ ] **Develop Data Transformation & Reporting Logic** (4h)
  - Compute RX, prescriber, and drug metrics.
  - Build endpoints to serve dashboard-ready data.

---

## Phase 4: Deployment and Integration  
**Estimated Total: ~16.5 hours**

### 4.1 Containerization  
- [ ] **Write and Refine Dockerfile for Node.js API** (2h)
  - Use multi-stage builds for efficiency.
- [ ] **Write Dockerfile for Python Integration Service** (1.5h)
- [ ] **Build, Test, and Push Container Images to Artifact Registry** (3h)

### 4.2 Cloud Run Deployment  
- [ ] **Deploy Node.js API with Cloud Run** (1.5h)
  - Configure environment variables, auto-scaling, and Cloud SQL connection.
- [ ] **Deploy Python Integration Service with Cloud Run** (1.5h)
- [ ] **Set Up Cloud Scheduler to Trigger Daily Ingestion Jobs** (1h)

### 4.3 Front-End Hosting and Integration  
- [ ] **Build Production Bundle for React App** (1h)
- [ ] **Deploy React App via Firebase Hosting or Cloud Storage + CDN** (1.5h)
- [ ] **Configure Domain Mapping and CORS** (1h)

### 4.4 End-to-End Testing and Monitoring  
- [ ] **Conduct Comprehensive End-to-End Testing** (1.5h)
- [ ] **Set Up Cloud Monitoring Dashboards and Logging** (1.5h)

---

## Phase 5: DRX Integration Deep Dive  
**Estimated Total: ~16.5 hours**

### 5.1 DRX API Production Integration  
- [ ] **Review API Documentation and Update Configurations** (1h)
  - Ensure *docs/API_Integrator/DRX_API_DOCUMENTATION_GUIDE_REMASTERED.MD* and *DRX_API_ENDPOINTS.md* are referenced.
- [ ] **Store DRX API Credentials Securely in Secret Manager** (1h)
- [ ] **Set Up DRX Sandbox Environment for Testing** (1h)

### 5.2 Implement DRX Ingestion & Normalization  
- [ ] **Develop Function to Call DRX API Endpoints** (2h)
  - Use axios (in Node.js) or requests (in Python) to fetch live data.
- [ ] **Process and Map DRX Data to Internal Metrics** (2h)
  - Normalize fields and update the central database.
- [ ] **Implement Incremental Sync and Error Handling** (2h)
  - Use timestamps to fetch only new data and robust retry mechanisms.
- [ ] **Write Unit and Integration Tests for DRX Connector** (1.5h)

### 5.3 Real-Time Updates and Reporting Enhancements  
- [ ] **Integrate Real-Time Data Push (WebSocket or SSE)** (2h)
- [ ] **Update Dashboard Components to Reflect Live Updates** (1h)

### 5.4 Performance and Scalability Validation  
- [ ] **Perform Load Testing Specific to DRX Ingestion** (1.5h)
- [ ] **Optimize and Document Scalability Measures** (1.5h)

---

## Overall Timeline Summary  
- **Phase 1:** ~13 hours  
- **Phase 2:** ~13.5 hours  
- **Phase 3:** ~48.5 hours  
- **Phase 4:** ~16.5 hours  
- **Phase 5:** ~16.5 hours  

**Total:** Approx. 108 hours (~14 workdays for a small agile team with parallel workflow capabilities)

---

### Additional Notes:
- **API_Integrator References:**  
  All specific API details, endpoints, and integration nuances are documented in the *docs/API_Integrator* folder. This detailed plan uses these references to implement production-grade integration (e.g., DRX API).
- **Data Ingestion:**  
  The product will perform a daily, automated scrape from the pharmacy management software. Data is processed to compute RX metrics, prescriber metrics, and drug statistics with clear visual reporting (graphs, charts) on the dashboard.
- **Production Readiness:**  
  This plan assumes that the relevant configurations, secrets, and endpoints are fully documented in the API_Integrator subfolder for a seamless transition to a production environment.

This updated detailed implementation plan now fully reflects the contents of Phases 1–5 in the agentic team notes folder and incorporates the production API integration aspects from the API_Integrator references.