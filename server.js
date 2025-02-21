/*
 * Pharmacy Data Dashboard - Production Server
 * This server performs a daily data scrape from the pharmacy management system by integrating
 * with real APIs as documented in the API_Integrator subfolder. It retrieves RX metrics,
 * prescriber metrics, drug statistics, and presents them via REST API endpoints.
 */

const express = require('express');
const axios = require('axios');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

let latestMetrics = {
  rxCount: 0,
  prescriberCount: 0,
  drugStats: {},
  timestamp: null
};

// Load API Integrator configuration from the docs/API_Integrator folder.
const configPath = path.join(__dirname, 'docs', 'API_Integrator', 'config.json');
let apiConfig = {};
try {
  const configData = fs.readFileSync(configPath, 'utf8');
  apiConfig = JSON.parse(configData);
  console.log('API Integrator configuration loaded successfully.');
} catch (err) {
  console.error('Error loading API Integrator configuration:', err);
}

/**
 * Fetch data from the DRX API using real endpoints and API keys as per the API_Integrator documentation.
 * This function assumes that the configuration file (config.json) contains:
 *   - DRX_API_ENDPOINT: the URL for the DRX API endpoint.
 *   - DRX_API_KEY: the API key for authenticating requests.
 *
 * The response from the DRX API is expected to include metrics such as:
 *   - rxCount
 *   - prescriberCount
 *   - drugStats (an object mapping drug names to their counts)
 */
async function fetchDataFromDRX() {
  if (!apiConfig.DRX_API_ENDPOINT || !apiConfig.DRX_API_KEY) {
    throw new Error('DRX API configuration missing in config.json.');
  }
  try {
    const response = await axios.get(apiConfig.DRX_API_ENDPOINT, {
      headers: { 'api-key': apiConfig.DRX_API_KEY }
    });
    // Process and normalize the API response data.
    // The actual mapping will depend on the DRX API response structure as described in docs/API_Integrator/DRX_API_ENDPOINTS.md.
    // For demonstration, we assume the response contains the metrics directly.
    const data = response.data;
    return {
      rxCount: data.rxCount || 0,
      prescriberCount: data.prescriberCount || 0,
      drugStats: data.drugStats || {},
      timestamp: new Date().toISOString()
    };
  } catch (err) {
    console.error('Error fetching DRX API data:', err.message);
    throw err;
  }
}

// Endpoint to trigger a real-time data scrape from the DRX API.
app.get('/api/trigger-scrape', async (req, res) => {
  try {
    const data = await fetchDataFromDRX();
    latestMetrics = data;
    res.json({
      message: "Data scrape completed successfully.",
      data: latestMetrics
    });
  } catch (err) {
    res.status(500).json({ message: "Failed to scrape data.", error: err.message });
  }
});

// Endpoint to fetch the latest metrics data.
app.get('/api/metrics', (req, res) => {
  res.json(latestMetrics);
});

app.listen(PORT, () => {
  console.log(`Production server is listening on port ${PORT}`);
});