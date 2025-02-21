# Phase 3 – Core Application Development

Total Estimated Hours: ≈ 160

This phase covers building the Node.js API (≈60 hours), the Python/Flask integration services (≈40 hours), and the React front-end (≈60 hours).

---

## Task Checklist

- [ ] **Back-end API (Node.js) implementation** (≈60 hours)
- [ ] **Integration Services (Python/Flask) development** (≈40 hours)
- [ ] **Front-end (React) application development** (≈60 hours)

Below are the sub-steps in ultra detail:

---

### 1. Back-End API (Node.js) Implementation (≈60 hours)

1. [ ] **Initialize Node Project**  
   - Create a directory `backend-node/`.  
   - `cd backend-node && npm init -y`.  
   - Install base deps: `npm install express cors dotenv pg`.

2. [ ] **Configure TypeScript (Optional)**  
   - `npm install typescript ts-node @types/node @types/express --save-dev`.  
   - Run `npx tsc --init`.  
   - Update `tsconfig.json` for target ES2020, etc.

3. [ ] **Set Up Project Structure**  
   - Folders: `src/controllers`, `src/routes`, `src/models`, `src/config`.  
   - In `src/index.ts` (or `.js`), create the Express server instance.

4. [ ] **Database Connection**  
   - `npm install pg pg-hstore`.  
   - Create `src/config/db.ts`: 
     ```ts
     import { Pool } from 'pg';
     export const pool = new Pool({
       connectionString: process.env.DB_CONNECTION_STRING
     });
     // or use socket path for Cloud SQL, etc.
     ```
   - Verify connectivity in a small test route.

5. [ ] **Env Variables & Secrets**  
   - In dev, use `.env` with `DB_CONNECTION_STRING=...`.  
   - For production, plan to load from GCP Secret Manager.  
   - Document usage in `README.md`.

6. [ ] **Basic Routes**  
   - In `src/routes/index.ts`:
     ```ts
     import { Router } from 'express';
     const router = Router();
     router.get('/health', (req, res) => res.send('OK'));
     export default router;
     ```
   - In `src/index.ts`, import `router`:
     ```ts
     import express from 'express';
     import router from './routes';
     const app = express();
     app.use(express.json());
     app.use('/api', router);
     app.listen(process.env.PORT || 8080, () => { ... });
     ```

7. [ ] **User Authentication**  
   - Decide on JWT or session-based.  
   - If JWT, install `npm install jsonwebtoken bcrypt`.  
   - Create `src/controllers/authController.ts` with routes for `POST /login`, `POST /register`.  
   - Hash passwords with bcrypt, store in DB. Return JWT on login.  
   - Add middleware to validate JWT for protected routes.

8. [ ] **Prescriber Routes**  
   - `GET /api/prescribers`: query DB for prescribers.  
   - `GET /api/prescribers/:id`: details.  
   - `POST /api/prescribers`: add new (if needed).  
   - `PATCH /api/prescribers/:id`: update existing.  
   - Implement using a dedicated controller or route file.

9. [ ] **Integration Status Routes**  
   - `GET /api/integrations/status`: returns last sync time for each pharmacy.  
   - `POST /api/integrations/run`: triggers manual sync (we will call the Python service or Pub/Sub).

10. [ ] **Error Handling & Logging**  
    - Implement a global error handler middleware.  
    - Use a logging library (winston or pino) to log requests and errors.

11. [ ] **Testing (Unit & Integration)**  
    - `npm install jest supertest --save-dev`.  
    - Write test cases for each route.  
    - Example: `test/prescribers.test.ts` using supertest to call `GET /api/prescribers` and check response.

12. [ ] **Code Review and Refactoring**  
    - Ensure consistent style (ESLint or Prettier).  
    - Setup pre-commit hooks if desired.

13. [ ] **Performance Considerations**  
    - Evaluate if we need caching for prescriber queries.  
    - Possibly store frequently accessed data in memory or Redis.  
    - For now, keep it simple unless we see performance issues.

14. [ ] **Finalize**  
    - Confirm all endpoints and features match acceptance criteria from Phase 1.  
    - Document usage in `backend-node/README.md`.

---

### 2. Integration Services (Python/Flask) Development (≈40 hours)

1. [ ] **Initialize Python Project**  
   - Create `integrations-python/`.  
   - Create a virtual environment: `python3 -m venv venv`.  
   - Activate: `source venv/bin/activate`.  
   - Install deps: `pip install flask requests psycopg2`.

2. [ ] **Flask App Setup**  
   - In `app.py`, create a basic Flask instance:
     ```py
     from flask import Flask
     app = Flask(__name__)

     @app.route('/health')
     def health():
         return 'Integration Service OK', 200
     if __name__ == '__main__':
         app.run(host='0.0.0.0', port=8000)
     ```
   - Test locally with `python app.py`.

3. [ ] **Configuration & DB Connection**  
   - Use environment variables to get DB credentials.  
   - Create `db.py`:
     ```py
     import os
     import psycopg2
     conn = psycopg2.connect(os.environ['DB_CONNECTION_STRING'])
     ```
   - Potentially create a function `get_db_cursor()` returning `conn.cursor()` or use a connection pool.

4. [ ] **Integration Connectors**  
   - Create `connectors/` folder.  
   - For each system (DRX, BestRx, etc.), create a file: e.g. `drx_connector.py`, `bestrx_connector.py`.  
   - Each file has a function `fetch_data(pharmacy_id, api_key)` that calls external API and returns the data.

5. [ ] **Common Sync Logic**  
   - Write a function `sync_pharmacy(pharmacy_id, system_name)` that:  
     - Retrieves the pharmacy’s integration info from DB.  
     - Calls the relevant connector.  
     - Processes results (inserts/updates prescribers, prescriptions).
   - Store last sync time in DB.

6. [ ] **Routes vs CLI**  
   - If you want an HTTP endpoint to trigger sync:
     ```py
     @app.route('/sync/<pharmacy_id>', methods=['POST'])
     def sync_now(pharmacy_id):
         # call sync_pharmacy
         return 'Sync triggered', 200
     ```
   - For batch or scheduled tasks, consider a separate script or Cloud Run job that calls these functions directly.

7. [ ] **DRX Connector (Skeleton)**  
   - In `drx_connector.py`:
     ```py
     import requests
     def fetch_data(api_key):
         headers = {'Authorization': f'Bearer {api_key}'}
         # Example: r = requests.get('https://drx-api/doctor/GetAll', headers=headers)
         # parse r.json(), return structured data
         return []
     ```
   - Return a list of prescribers, each with {npi, name, specialty…}.

8. [ ] **Data Ingestion**  
   - Once data is fetched, transform to DB schema.  
   - Use `INSERT ... ON CONFLICT (npi) DO UPDATE` for prescriber records.  
   - Maintain metrics (like `rx_count`) in separate tables as needed.

9. [ ] **Error Handling & Retries**  
   - If the API call fails, log an error, set a status for that sync attempt.  
   - Possibly implement exponential backoff or schedule a retry.

10. [ ] **Testing**  
    - Use Pytest.  
    - Mock external API calls with `responses` library or `unittest.mock`.  
    - Ensure data is inserted properly into a test DB.

11. [ ] **Documentation**  
    - In `integrations-python/README.md`, list how to run the server, environment variables, etc.  
    - Example: `DB_CONNECTION_STRING`, `DRX_API_KEY_...` etc.

12. [ ] **Refine Performance**  
    - Evaluate batch size for API calls, ensure we’re not loading too much into memory.  
    - Possibly process data in chunks.

13. [ ] **Finalize**  
    - Confirm that each connector is tested.  
    - Integration service is stable, logging is enabled.

---

### 3. Front-End (React) Application Development (≈60 hours)

1. [ ] **Initialize React Project**  
   - `npx create-react-app frontend-react --template typescript` (if using TS).  
   - Or `npx create-react-app frontend-react` (JS).

2. [ ] **Project Structure**  
   - In `src/`, create subfolders: `components/`, `pages/`, `services/`, `store/`.  
   - Clear out sample code, keep `App.js` or `App.tsx` as root.

3. [ ] **Routing Setup**  
   - `npm install react-router-dom`.  
   - Wrap `<App>` with `<BrowserRouter>`.  
   - Create routes: `/login`, `/prescribers`, `/prescribers/:id`, `/analytics`.

4. [ ] **Authentication Flow**  
   - Create a `LoginPage.tsx` that calls the Node API’s `/api/login`.  
   - Store JWT in localStorage or in memory.  
   - Use a higher-order component or custom hook to protect routes.

5. [ ] **Prescribers List**  
   - `PrescribersPage.tsx`: fetch from `GET /api/prescribers`.  
   - Display in a table using a component library (e.g., Material-UI):
     ```bash
     npm install @mui/material @emotion/react @emotion/styled
     ```
   - Handle loading states, errors.

6. [ ] **Prescriber Detail**  
   - `PrescriberDetailPage.tsx`: fetch `/api/prescribers/:id`.  
   - Show name, specialty, total Rx count, etc.  
   - Possibly a chart for script trends (use `recharts` or `chart.js`).

7. [ ] **Analytics**  
   - `AnalyticsPage.tsx`: call `/api/analytics/overview`.  
   - Display charts for top prescribers, top drugs, etc.

8. [ ] **Global State Management**  
   - Optionally install Redux: `npm install redux react-redux @reduxjs/toolkit`.  
   - Create slices for `authSlice`, `prescribersSlice`, etc.  
   - Or use React Context if simpler.

9. [ ] **UI Components**  
   - Create reusable components in `/components/`:
     - `PrescriberCard.tsx`, `LoadingSpinner.tsx`, `Navbar.tsx`.
   - Style with Material-UI themes or a custom CSS approach.

10. [ ] **API Service**  
    - In `/services/api.ts`, centralize fetch logic:
      ```ts
      import axios from 'axios';
      const api = axios.create({
        baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8080/api'
      });
      export default api;
      ```
    - Expose methods: `login`, `getPrescribers`, etc.

11. [ ] **Testing**  
    - `npm install --save-dev jest @testing-library/react`.  
    - Write component tests (render, simulate clicks).  
    - Possibly add integration tests with a mock server.

12. [ ] **Performance**  
    - Consider code splitting for routes if the app is large.  
    - Use React’s Suspense if beneficial.

13. [ ] **Build for Production**  
    - `npm run build` produces `/build` folder.  
    - This will be deployed (Phase 4).

14. [ ] **Finalize**  
    - Ensure all front-end acceptance criteria are met.  
    - Document in `frontend-react/README.md`.

---

After completing these subtasks, the core application (back-end, front-end, integration services) should be fully functional and tested. Proceed to [Phase 4 – Deployment & Integration](./phase4_deployment_integration.md).

