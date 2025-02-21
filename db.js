/**
 * db.js
 * 
 * This module sets up a connection pool to the persistent storage (Cloud SQL/PostgreSQL)
 * using the 'pg' package. Ensure that the DATABASE_URL environment variable is set in production.
 */

const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  // In production, you might adjust SSL settings as needed.
  ssl: process.env.DATABASE_URL.includes("postgres") ? { rejectUnauthorized: false } : false
});

module.exports = {
  query: (text, params, callback) => {
    return pool.query(text, params, callback);
  }
};