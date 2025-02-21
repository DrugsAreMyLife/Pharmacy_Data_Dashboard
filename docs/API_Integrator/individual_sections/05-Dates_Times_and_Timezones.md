# Dates, Times, and Timezones

## Overview

The DRX API handles all date and time values in a consistent format to ensure reliable data processing across different timezones. This document outlines the standards and best practices for working with temporal data in the API.

## Date and Time Format

All timestamps in the API use ISO 8601 format in UTC:

```
YYYY-MM-DDTHH:mm:ssZ
```

Example:
```
2025-02-19T08:53:00Z
```

## Timezone Handling

- All API responses return timestamps in UTC
- Client applications should convert UTC times to local timezone for display
- When sending dates/times to the API, you can either:
  - Send UTC time directly
  - Include timezone offset in ISO 8601 format

## Examples

### UTC Time
```json
{
  "created_at": "2025-02-19T08:53:00Z",
  "updated_at": "2025-02-19T08:53:00Z"
}
```

### With Timezone Offset
```json
{
  "appointment_time": "2025-02-19T02:53:00-06:00"  // Central Time
}
```

## Best Practices

1. Always store times in UTC internally
2. Convert to local time only for display purposes
3. Include timezone information when scheduling future events
4. Use ISO 8601 format for all date/time values
5. Consider daylight saving time when working with future dates

## Date-Only Fields

For fields that only require a date (no time component):

```json
{
  "birth_date": "2000-01-01",
  "expiration_date": "2025-12-31"
}
```

## Time Ranges

When specifying time ranges:

```json
{
  "start_time": "2025-02-19T08:00:00Z",
  "end_time": "2025-02-19T17:00:00Z"
}
```

## Common Issues

1. Mixing timezone-aware and naive timestamps
   - Always be explicit about timezone information
   - Don't assume local timezone for incoming data

2. Daylight saving time transitions
   - Be aware of DST changes when scheduling future events
   - Test date/time handling around DST transitions

3. Day length assumptions
   - Not all days have 24 hours (DST transitions)
   - Some locations may have different day lengths

4. Leap years and seconds
   - Account for leap years in date calculations
   - Be prepared to handle leap seconds if high precision is required

5. Ambiguous date formats
   - Avoid ambiguous formats like MM/DD/YY vs DD/MM/YY
   - Stick to ISO 8601 format for consistency

## Implementation Tips

1. Use appropriate date/time libraries
   - Moment.js
   - date-fns
   - Luxon
   - Python's datetime with pytz

2. Validation checks
   - Validate date format before processing
   - Check for reasonable date ranges
   - Verify timezone offsets

3. Error handling
   - Provide clear error messages for invalid dates
   - Handle edge cases gracefully
   - Log timezone-related issues for debugging

4. Testing considerations
   - Test with different timezones
   - Include DST transition dates in test cases
   - Verify date/time calculations across date boundaries

## Additional Resources

1. ISO 8601 Standard Reference
2. UTC Time Explanation
3. Timezone Database Updates
4. Date/Time Library Documentation