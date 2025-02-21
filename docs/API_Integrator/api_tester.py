#!/usr/bin/env python
"""
API Tester for DRX API

Comprehensive testing of all v1 endpoints with various parameter combinations.
"""

import requests
import json
import os
import datetime
import time
from typing import Dict, List, Optional, Set, Any, Deque, NamedTuple, TypedDict, DefaultDict
from collections import deque, defaultdict
from urllib.parse import urljoin, urlencode

class TestResult(TypedDict):
    """Type definition for test results."""
    endpoint: str
    method: str
    params: Optional[Dict[str, Any]]
    status: Optional[int]
    response: str

class CategoryResults(DefaultDict[str, List[TestResult]]):
    """Type for categorized test results."""
    pass

# Fixed configuration - IMMUTABLE DEMO ENVIRONMENT
STORE_SLUG = "demo"  # This is immutable for the demo environment
BASE_URL = f"https://{STORE_SLUG}.drxapp.com/external_api/v1"
API_KEY = os.getenv("DRX_API_KEY", "DRX1754cdd3b922426998649af0b0fee50b")

# Rate limiting configuration
HOURLY_LIMIT = 1000
MINUTE_LIMIT = 100
request_history: Deque[float] = deque(maxlen=HOURLY_LIMIT)
minute_history: Deque[float] = deque(maxlen=MINUTE_LIMIT)

class Endpoint(NamedTuple):
    """Represents an API endpoint to test."""
    name: str
    path: str
    method: str
    params: Optional[Dict[str, Any]] = None
    data: Optional[Dict[str, Any]] = None

# Define common parameter variations
PAGINATION_VARIATIONS = [
    {"limit": "10", "offset": "0"},
    {"limit": "1", "offset": "0"},  # Minimum case
    {"limit": "100", "offset": "0"},  # Maximum case
    {"limit": "10", "offset": "10"},  # With offset
]

DATE_VARIATIONS = [
    {"before_date": "2025-02-19T00:00:00Z"},
    {"after_date": "2025-02-19T00:00:00Z"},
    {"before_date": "2025-02-19T00:00:00Z", "after_date": "2025-02-18T00:00:00Z"},
]

STATUS_VARIATIONS = [
    {"status": "Hold"},
    {"status": "Waiting Bin"},
    {"status": "Sold"},
    {"status": "Print"},
    {"status": "Rejected"},
    {"status": "Verify"},
    {"status": "Scan"},
    {"status": "Adjudicating"},
    {"status": "OOS"},
]

SEARCH_VARIATIONS = [
    {"search": "test"},  # Basic search
    {"search": ""},  # Empty search
    {"search": "a"},  # Single character
    {"search": "test test"},  # Multiple words
]

# Define all v1 endpoints to test with variations
ENDPOINTS = [
    # Heartbeat
    Endpoint("Heartbeat", "heartbeat", "GET"),
    
    # Addresses
    *[Endpoint("List Addresses", "addresses", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          {"type": "billing"},
          {"type": "shipping"},
          {"city": "Austin"},
          {"state": "TX"},
          {"country": "US"},
          {**PAGINATION_VARIATIONS[0], "type": "billing", "city": "Austin"},
      ]],
    
    # Allergies
    *[Endpoint("List Allergies", "allergies", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          {"category": "medication"},
          {"category": "food"},
          {"severity": "mild"},
          {"severity": "moderate"},
          {"severity": "severe"},
          *SEARCH_VARIATIONS,
      ]],
    
    # Charge Accounts
    *[Endpoint("List Charge Accounts", "charge_accounts", "GET", params)
      for params in PAGINATION_VARIATIONS],
    
    # Claims
    *[Endpoint("List Claims", "claims", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          *DATE_VARIATIONS,
      ]],
    
    # Deliveries
    *[Endpoint("List Deliveries", "deliveries", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          {"route": "ROUTE1"},
          {"date": "2025-02-19"},
          {"external_id": "TEST-ID"},
          {**PAGINATION_VARIATIONS[0], "route": "ROUTE1", "date": "2025-02-19"},
      ]],
    
    # Delivery Routes
    *[Endpoint("List Delivery Routes", "deliveries/routes", "GET", params)
      for params in PAGINATION_VARIATIONS],
    
    # Doctors
    *[Endpoint("List Doctors", "doctors", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          {"q": "01201986"},  # Date of Birth
          {"q": "5852984455"},  # Phone Number
          {"q": "nau,ron"},  # Full name
          {"q": "naugle"},  # Last name only
          {"q": "5852984455"},  # Fax Number
          {"q": "1234567890"},  # NPI
          {"q": "AB1234567"},  # DEA
      ]],
    
    # Provider Catalog
    *[Endpoint("Search Provider Catalog", "doctors/search", "GET", params)
      for params in [
          {"first_name": "John"},
          {"last_name": "Smith"},
          {"npi": "1234567890"},
          {"dea": "AB1234567"},
          {"state": "TX"},
          {**PAGINATION_VARIATIONS[0], "first_name": "John", "last_name": "Smith"},
      ]],
    
    # Inventory
    Endpoint("Get All Inventory", "inventory", "GET"),
    Endpoint("Get All Inventory with Date", "inventory", "GET", {"as_of_date": "2025-02-19"}),
    
    # Item Inventory History
    *[Endpoint("Get Item Inventory History", "inventory/history", "GET", params)
      for params in [
          {"item_id": "12345"},
          {"item_id": "12345", "start_date": "2025-02-18", "end_date": "2025-02-19"},
          {"item_id": "12345", "includeEquivalents": "true"},
      ]],
    
    # Items
    *[Endpoint("List Items", "items", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          {"ndc": "111"},  # Partial NDC match
          {"gcn": "12345"},  # Exact GCN match
          {"item_type": "MEDICATION"},
          {**PAGINATION_VARIATIONS[0], "ndc": "111", "item_type": "MEDICATION"},
      ]],
    
    # Packing Lists
    *[Endpoint("List Packing Lists", "packing_lists", "GET", params)
      for params in PAGINATION_VARIATIONS],
    
    # Patients
    *[Endpoint("List Patients", "patients", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          *SEARCH_VARIATIONS,
          *DATE_VARIATIONS,
          {"facility_id": "12345"},
          {"q": "01201986"},  # Date of Birth
          {"q": "5852984455"},  # Phone Number
          {"q": "smith,john"},  # Full name
          {"q": "smith"},  # Last name only
      ]],
    
    # Phone Numbers
    *[Endpoint("List Phone Numbers", "phone_numbers", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          *SEARCH_VARIATIONS,
          {"q": "5852984455"},  # Full number
          {"q": "585"},  # Partial number
      ]],
    
    # Point of Sale
    *[Endpoint("List Sale Events", "pos/events", "GET", params)
      for params in PAGINATION_VARIATIONS],
    
    # Prescriptions
    *[Endpoint("List Prescriptions", "prescriptions", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          {"patient_id": "12345"},
          *STATUS_VARIATIONS,
          {"facility_id": "12345"},
          {"ehr_message_id": "MSG123"},
          {"ehr_order_number": "ORD123"},
          {"expiration_date": "2025-02-19"},
          *DATE_VARIATIONS,
          {**PAGINATION_VARIATIONS[0], "patient_id": "12345", "status": "Hold"},
      ]],
    
    # Prescription Fills
    *[Endpoint("List Prescription Fills", "prescription_fills", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          *DATE_VARIATIONS,
          {"fills_in_progress": "true"},
          *STATUS_VARIATIONS,
          {"patient_id": "12345"},
          {**PAGINATION_VARIATIONS[0], "patient_id": "12345", "status": "Hold"},
      ]],
    
    # Fill Tags
    *[Endpoint("List Fill Tags", "fill_tags", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          {"name": "urgent"},
          {"fill_id": "12345"},
          {**PAGINATION_VARIATIONS[0], "name": "urgent"},
      ]],
    
    # SureScripts
    *[Endpoint("List SureScripts", "surescripts", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          {"showOldItems": "true"},
          {"showOldItems": "false"},
          {"external_id": "EXT123"},
          *SEARCH_VARIATIONS,
          {"ehrMessageId": "MSG123"},
          {"ehrOrderNumber": "ORD123"},
          {**PAGINATION_VARIATIONS[0], "showOldItems": "true", "search": "test"},
      ]],
    
    # Store Settings
    Endpoint("Get Store Settings", "settings", "GET"),
    
    # Stores
    Endpoint("List Stores", "stores", "GET"),
    
    # Shipping
    *[Endpoint("List Past Shipments", "shipments", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          {"patient_id": "12345"},
      ]],
    
    # Tasks
    *[Endpoint("List Tasks", "tasks", "GET", params)
      for params in PAGINATION_VARIATIONS],
    
    # Competing Pharmacies
    *[Endpoint("List Competing Pharmacies", "competing_pharmacies", "GET", params)
      for params in [
          *PAGINATION_VARIATIONS,
          *SEARCH_VARIATIONS,
          {"search": "CVS"},
          {"search": "1234567890"},  # NPI
          {"search": "AB1234567"},  # DEA
          {"search": "NCPDP123"},  # NCPDP
      ]],
    
    # Webhooks
    *[Endpoint("List Webhooks", "webhooks", "GET", params)
      for params in PAGINATION_VARIATIONS],
]

def check_rate_limit() -> bool:
    """Check if we're within rate limits."""
    current_time = time.time()
    hour_ago = current_time - 3600
    minute_ago = current_time - 60
    
    # Clean up old requests
    while request_history and request_history[0] < hour_ago:
        request_history.popleft()
    while minute_history and minute_history[0] < minute_ago:
        minute_history.popleft()
    
    # Check limits
    return len(request_history) < HOURLY_LIMIT and len(minute_history) < MINUTE_LIMIT

def track_request() -> None:
    """Track a new request for rate limiting."""
    current_time = time.time()
    request_history.append(current_time)
    minute_history.append(current_time)

def save_markdown_results(results: List[TestResult]) -> None:
    """Save test results to a markdown file."""
    output_file = "API-Tester/api_test_results.md"
    
    # Calculate summary statistics
    total_tests = len(results)
    successful_tests = sum(1 for r in results if r["status"] in [200, 201, 204])
    
    with open(output_file, "w", encoding="utf-8") as f:
        # Write header and summary
        f.write("# API Test Results\n\n")
        f.write(f"Test Run: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## Summary\n\n")
        f.write(f"- Total Tests: {total_tests}\n")
        f.write(f"- Successful: {successful_tests}\n")
        f.write(f"- Failed: {total_tests - successful_tests}\n\n")
        
        # Group results by endpoint category
        categories: CategoryResults = defaultdict(list)
        for result in results:
            category = result["endpoint"].split()[0]  # First word of endpoint name
            categories[category].append(result)
        
        # Write detailed results by category
        f.write("## Detailed Results\n\n")
        for category, category_results in sorted(categories.items()):
            f.write(f"### {category}\n\n")
            f.write("| Endpoint | Method | Parameters | Status | Result |\n")
            f.write("|----------|---------|------------|---------|----------|\n")
            
            for result in sorted(category_results, key=lambda x: x["endpoint"]):
                status = result["status"]
                indicator = "✅" if status in [200, 201, 204] else "❌"
                
                try:
                    response = json.loads(result["response"]) if result["response"] else None
                    response_text = "Success" if status in [200, 201, 204] else json.dumps(response)
                except:
                    response_text = str(result["response"])
                
                # Truncate long responses
                response_text = response_text[:100] + "..." if len(response_text) > 100 else response_text
                response_text = response_text.replace("|", "│")
                
                params_text = json.dumps(result.get("params", {}))[:50] + "..." if result.get("params") else "None"
                
                f.write(f"| {result['endpoint']} | {result['method']} | {params_text} | {status or 'ERROR'} {indicator} | {response_text} |\n")
            
            f.write("\n")

def construct_api_url(endpoint: str, path_params: Optional[Dict[str, str]] = None, query_params: Optional[Dict[str, str]] = None) -> str:
    """Construct full API URL."""
    # Replace path parameters in endpoint
    if path_params:
        for param, value in path_params.items():
            endpoint = endpoint.replace(f"{{{param}}}", value)
    
    # Construct the base URL
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    
    # Add query parameters if provided
    if query_params:
        url = f"{url}?{urlencode(query_params)}"
    
    return url

def test_endpoint(url: str, method: str = "GET", headers: Optional[Dict] = None, data: Optional[Dict] = None) -> tuple:
    """Test an API endpoint and return status code and response."""
    try:
        # Check rate limits before making request
        if not check_rate_limit():
            return 429, "Rate limit exceeded. Please wait before making more requests."
        
        # Test connection to URL first
        print(f"Testing connection to URL: {url}")
        response = requests.head(url, headers=headers, timeout=5)
        print(f"URL test response status: {response.status_code}")
        
        # Make the actual API request
        print("Making API request...")
        start_time = time.time()
        response = requests.request(method, url, headers=headers, json=data, timeout=10)
        end_time = time.time()
        
        # Print response details for debugging
        print(f"API Response Time: {end_time - start_time:.2f}s")
        print(f"Response Status: {response.status_code}")
        print(f"Response Headers: {json.dumps(dict(response.headers), indent=2)}")
        print(f"Response Content: {response.text}")
        
        # Track the request for rate limiting
        track_request()
        
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return None, str(e)
    except Exception as e:
        return 500, str(e)

def main() -> None:
    """Main entry point for the API tester."""
    print("Starting comprehensive API tests...")
    print(f"Total endpoints to test: {len(ENDPOINTS)}")
    
    # Prepare headers according to v1 API documentation
    headers = {
        "X-DRX-Key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    results = []
    
    # Test all endpoints
    for i, endpoint in enumerate(ENDPOINTS, 1):
        print(f"\nTesting endpoint {i}/{len(ENDPOINTS)}: {endpoint.name}")
        
        url = construct_api_url(endpoint.path, query_params=endpoint.params)
        print(f"Making {endpoint.method} request to {url}")
        print(f"Headers: {json.dumps(headers, indent=2)}")
        if endpoint.params:
            print(f"Query Parameters: {json.dumps(endpoint.params, indent=2)}")
        if endpoint.data:
            print(f"Request Data: {json.dumps(endpoint.data, indent=2)}")
        
        status, response = test_endpoint(url, method=endpoint.method, headers=headers, data=endpoint.data)
        
        results.append({
            "endpoint": endpoint.name,
            "method": endpoint.method,
            "params": endpoint.params,
            "status": status,
            "response": response
        })
        
        # Respect rate limits
        time.sleep(1)  # Add a small delay between requests
    
    save_markdown_results(results)
    print("\nAPI testing complete. Results saved to api_test_results.md")
    print(f"Total endpoints tested: {len(results)}")
    successful_tests = sum(1 for r in results if r["status"] in [200, 201, 204])
    print(f"Successful tests: {successful_tests}")
    print(f"Failed tests: {len(results) - successful_tests}")

if __name__ == "__main__":
    main()