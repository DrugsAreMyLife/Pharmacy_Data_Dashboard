# Phase 1 – Project Setup & Requirements

Total Estimated Hours: ≈ 48

This document provides an ultra-granular task list for setting up the project and defining requirements.

---

## Task Checklist

- [ ] **Define requirements and modules** (≈16 hours)
- [ ] **Choose development approach** (≈8 hours)
- [ ] **Set up version control and CI** (≈8 hours)
- [ ] **Create central design document** (≈12 hours)
- [ ] **Finalize acceptance criteria** (≈4 hours)

Below is the detailed breakdown for each.

---

### 1. Define Requirements and Modules (≈16 hours)

1. [ ] **Gather all Stakeholders & Documentation**  
   - Locate or request any existing documentation regarding user needs, pharmacy workflows, data scope.  
   - Schedule meeting with stakeholders (pharmacy owner, developer leads, any key SMEs).
   - Consolidate all gathered data into a single shareable location (e.g., Google Drive or the local `/docs/` folder).

2. [ ] **Create a Master Requirements Document**  
   - In `/docs/requirements/`, start a file named `requirements_master.md`.  
   - Outline user stories or use cases (e.g., “As a pharmacy user, I want to see a real-time list of prescribers…”).  
   - For each user story, define a minimal acceptance scenario.

3. [ ] **Break Down Functional Modules**  
   - Draft a list of functional modules (e.g., **Prescriber CRM**, **Prescription Analytics**, **Data Share/Market Insights**, **User Management**, **Integrations**).  
   - For each module, detail the features (e.g., “Prescriber CRM: add/edit prescriber notes, view total scripts…”).

4. [ ] **Discuss Data Privacy & Compliance**  
   - Note any HIPAA or state regulations that might affect design.  
   - Decide which data elements are personally identifiable and how to handle them.  
   - Document any encryption or data retention requirements.

5. [ ] **Review & Iterate**  
   - Present the modules list to the team, gather feedback.  
   - Incorporate changes, finalize the requirements scope.

6. [ ] **Sign-Off**  
   - Get formal or informal sign-off from stakeholders that these requirements are correct.

---

### 2. Choose Development Approach (≈8 hours)

1. [ ] **Microservices vs Monolith**  
   - Confirm decision to use microservices for integration logic (Python/Flask) + Node.js for main API.  
   - Document rationale in `/docs/design/architecture_overview.md`.

2. [ ] **Front-End Stack**  
   - Confirm use of React (with TypeScript if desired).  
   - Decide on Redux vs Context for state management.  
   - Record final choice in architecture overview.

3. [ ] **Database Approach**  
   - Confirm usage of PostgreSQL on Cloud SQL for relational data.  
   - Potentially BigQuery for large-scale analytics.  
   - Document the chosen approach in architecture overview.

4. [ ] **File Structure & Repo Strategy**  
   - Decide on multi-repo or monorepo structure.  
   - If monorepo, note how directories will be organized.  
   - Document in architecture overview.

5. [ ] **Schedule Team Roles**  
   - Assign lead developer for each major subsystem (React, Node, Python).  
   - Estimate high-level timeline for sprints (e.g., 2-week sprints).

---

### 3. Set Up Version Control and CI (≈8 hours)

1. [ ] **Create Git Repository**  
   - If using GitHub, go to GitHub and create a new repo.  
   - Name it something like `superior-pharmacy-crm`.  
   - Initialize with a README, `.gitignore` for Node, Python, React, etc.

2. [ ] **Branching Strategy**  
   - Decide on GitFlow or trunk-based.  
   - Document branching conventions in `/docs/contributing.md`.

3. [ ] **Set up GitHub Actions (or Cloud Build)**  
   - Create a basic YAML config for CI:
     - **Node.js**: run `npm ci`, `npm test`  
     - **Python**: set up a separate job that installs requirements and runs tests.  
   - Store the config in `.github/workflows/ci.yml` or a similar path.

4. [ ] **Enable Pull Request Checks**  
   - In repo settings, enable branch protection so PR merges require passing CI.  
   - Test with a sample PR.

5. [ ] **Add Code Owners (Optional)**  
   - If certain team members own certain directories, configure `CODEOWNERS` file.

---

### 4. Create Central Design Document (≈12 hours)

1. [ ] **Initiate `/docs/design/architecture_overview.md`**  
   - Summarize overall system: front-end, Node API gateway, Python integration, DB, GCP.  
   - Use diagrams if possible (e.g., draw.io or mermaid in Markdown).

2. [ ] **Detail Data Flow**  
   - For each integration, show how data moves from PMS → Integration → DB → Node → React.  
   - Include any caching, queues, or Pub/Sub usage.

3. [ ] **Define Entities & Schemas**  
   - Create an entity-relationship diagram for DB tables (Pharmacy, Prescriber, Prescription, etc.).  
   - List fields, data types, relationships, and constraints.

4. [ ] **NPI Lookup & Data Enrichment**  
   - Outline how the NPI registry will be used and mention caching strategy.

5. [ ] **Security & Compliance**  
   - Describe approach for HIPAA compliance, mention encryption at rest, user authentication flow.  
   - Define how secrets and credentials are stored (Secret Manager).

6. [ ] **Review & Sign-Off**  
   - Circulate the design doc.  
   - Gather team feedback, finalize.

---

### 5. Finalize Acceptance Criteria (≈4 hours)

1. [ ] **Write Acceptance Criteria**  
   - For each major feature, define pass/fail conditions.  
   - Example: “Prescriber CRM loads data from the DB within 2 seconds with 1000 prescribers.”  
   - Keep them measurable and testable.

2. [ ] **Create a `testing_strategy.md`** in `/docs/`  
   - Outline how unit, integration, and end-to-end tests will be carried out.  
   - Reference acceptance criteria.

3. [ ] **Add to Project Management Tool**  
   - If using Jira/Trello, create tickets for each acceptance criterion.  
   - Link them to the relevant user stories in `requirements_master.md`.

4. [ ] **Close Phase 1**  
   - Confirm all tasks have been checked off and documented.  
   - Proceed to [Phase 2 – GCP Infrastructure Setup](./phase2_gcp_infrastructure.md).

