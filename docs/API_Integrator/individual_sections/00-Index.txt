# DRX API Documentation Index

This index provides quick access to all sections of the DRX API documentation.

## Core Documentation

1. [Introduction](01-DRX_API_Documentation_Introduction.md)
2. [Getting Started](02-Getting_Started.md)
3. [Changes to the API](03-Changes_to_the_API.md)
4. [Example Data](04-Example_Data.md)
5. [Dates, Times, and Timezones](05-Dates_Times_and_Timezones.md)

## API Endpoints

### Patient Management
6. [Addresses](06-Addresses.md)
7. [Allergies](07-Allergies.md)
8. [Charge Accounts](08-Charge_Accounts.md)
9. [Claims](09-Claims.md)
10. [Patients](18-Patients.md)
11. [Patient Match](19-Patient_Match.md)
12. [Phone Numbers](20-Phone_Numbers.md)

### Prescription Management
13. [Prescriptions](22-Prescriptions.md)
14. [Prescription Fills](23-Prescription_Fills.md)
15. [Fill Tags](24-Fill_Tags.md)
16. [SureScripts](25-SureScripts.md)
17. [Refills and Renewals](26-Refills_and_Renewals.md)

### Inventory and Items
18. [Inventory](13-Inventory.md)
19. [Items](15-Items.md)
20. [Images](14-Images.md)

### Delivery and Shipping
21. [Deliveries](10-Deliveries.md)
22. [Packing Lists](16-Packing_Lists.md)
23. [Shipping](28-Shipping.md)

### Healthcare Providers
24. [Doctors](11-Doctors.md)
25. [Eligibility](12-Eligibility.md)
26. [Third Party](31-Third_Party.md)
27. [Transfers](32-Transfers.md)

### Sales and Transactions
28. [Point of Sale](21-Point_of_Sale.md)
29. [Partners](17-Partners.md)

### Store Management
30. [Store Management](27-Store_Management.md)
31. [Tasks](30-Tasks.md)

### Communication
32. [SMS](29-SMS.md)
33. [Webhooks](33-Webhooks.md)

## Additional Resources

- Each section includes:
  * Endpoint descriptions
  * Request/response examples
  * Required/optional parameters
  * Best practices
  * Error handling
  * Integration notes

- Common features across sections:
  * Authentication requirements
  * Rate limiting
  * Pagination
  * Error responses
  * Webhook notifications

## Best Practices

1. Always check the [Changes to the API](03-Changes_to_the_API.md) section for updates
2. Review authentication requirements in [Getting Started](02-Getting_Started.md)
3. Understand date/time handling from [Dates, Times, and Timezones](05-Dates_Times_and_Timezones.md)
4. Reference [Example Data](04-Example_Data.md) for data structure patterns
5. Implement proper error handling as described in each section

## Notes

- All API endpoints require authentication
- URLs expire after 30 days
- Responses are in JSON format
- UTC timestamps are used throughout
- Rate limiting applies to all endpoints