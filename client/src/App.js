import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

// Register chart components
ChartJS.register(
  BarElement,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend
);

function App() {
  const [metrics, setMetrics] = useState({
    rxCount: 0,
    prescriberCount: 0,
    drugStats: {},
    timestamp: ''
  });
  const [loading, setLoading] = useState(false);

  // Fetch current metrics from the API
  const fetchMetrics = async () => {
    try {
      setLoading(true);
      const response = await axios.get('/api/metrics');
      setMetrics(response.data);
      setLoading(false);
    } catch (error) {
      console.error("Error fetching metrics:", error);
      setLoading(false);
    }
  };

  // Trigger a live data scrape from the API
  const triggerScrape = async () => {
    try {
      setLoading(true);
      const response = await axios.get('/api/trigger-scrape');
      setMetrics(response.data.data);
      setLoading(false);
    } catch (error) {
      console.error("Error triggering data scrape:", error);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchMetrics();
  }, []);

  const drugLabels = Object.keys(metrics.drugStats || {});
  const drugData = Object.values(metrics.drugStats || {});

  const chartData = {
    labels: drugLabels,
    datasets: [
      {
        label: 'Drug Counts',
        data: drugData,
        backgroundColor: 'rgba(75,192,192,0.6)',
      }
    ]
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Drug Statistics' }
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Pharmacy Data Dashboard</h1>
      <p>Last updated: {metrics.timestamp || "N/A"}</p>
      <div style={{ marginBottom: '1rem' }}>
        <button onClick={triggerScrape} disabled={loading}>
          {loading ? 'Loading...' : 'Trigger Data Scrape'}
        </button>
      </div>
      <div>
        <h2>RX Metrics</h2>
        <p>Total Prescriptions: {metrics.rxCount}</p>
        <p>Total Prescribers: {metrics.prescriberCount}</p>
      </div>
      <div style={{ marginTop: '2rem' }}>
        <h2>Drug Statistics</h2>
        <Bar data={chartData} options={chartOptions} />
      </div>
    </div>
  );
}

export default App;