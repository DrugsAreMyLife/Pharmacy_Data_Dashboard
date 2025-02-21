# Third Party

This section covers the endpoints related to managing third-party insurance plans in the DRX API.

## Add a Third Party

Add a third-party insurance plan to a patient.

### Endpoint

`POST /api/v2/patients/{patient_id}/third-parties`

### Required Fields

| Field | Explanation |
|-------|-------------|
| name | Plan Name |
| bin_number | Third Party BIN Number |

### Optional Fields

| Field | Explanation |
|-------|-------------|
| pcn | Processor Control Number |
| group | Group Number |
| treat_as_cash | Boolean (defaults to false) |
| dir_fee_formula_id | Foreign key to Dir Fee Formula |
| help_desk_number | Phone format: "(123) 456-7890" |
| cardholder_id | Cardholder ID number |
| start_date | Valid ISO format date |
| end_date | Valid ISO format date |
| billing_order | "primary" or "false" |
| comments | Additional notes |

### Example Request

```json
{
  "name": "Example Health Insurance",
  "bin_number": "123456",
  "pcn": "ABCD",
  "group": "GROUP123",
  "cardholder_id": "ID12345",
  "billing_order": "primary",
  "start_date": "2025-01-01",
  "help_desk_number": "(555) 123-4567"
}
```

### Response

#### Success Response (201 Created)

```json
{
  "id": "tp_12345",
  "name": "Example Health Insurance",
  "bin_number": "123456",
  "pcn": "ABCD",
  "group": "GROUP123",
  "cardholder_id": "ID12345",
  "billing_order": "primary",
  "status": "active",
  "start_date": "2025-01-01",
  "end_date": null,
  "help_desk_number": "(555) 123-4567",
  "created_at": "2025-02-19T08:50:00Z",
  "updated_at": "2025-02-19T08:50:00Z"
}
```

### Insurance Types

1. Primary Insurance
   - Main coverage
   - Processed first
   - Required for claims
   - Coverage verification needed

2. Secondary Insurance
   - Additional coverage
   - Processed after primary
   - Optional coverage
   - Coordination of benefits

3. Tertiary Insurance
   - Third level coverage
   - Final processing
   - Rare usage
   - Special handling

### Best Practices

1. Plan Management
   - Verify plan information
   - Check effective dates
   - Monitor coverage status
   - Update as needed

2. Claims Processing
   - Follow billing order
   - Check coverage rules
   - Handle rejections
   - Track payments

3. Data Quality
   - Validate BIN numbers
   - Verify PCN format
   - Check group numbers
   - Confirm IDs

4. Patient Communication
   - Explain coverage
   - Document changes
   - Notify of issues
   - Update preferences

### Common Issues

1. Invalid Information
   - Wrong BIN number
   - Incorrect PCN
   - Invalid group
   - Wrong cardholder ID

2. Coverage Problems
   - Expired coverage
   - Wrong effective dates
   - Terminated plans
   - Coverage gaps

3. Processing Errors
   - Wrong billing order
   - Missing information
   - Rejection handling
   - Coordination issues

4. System Integration
   - Data synchronization
   - Real-time verification
   - Claims processing
   - Payment posting

### Additional Information

- URL requests expire after 30 days
- All changes logged
- Audit trail maintained
- Historical data preserved
- Real-time updates supported
- Integration with:
  * Claims system
  * Patient portal
  * Billing system
  * Verification services