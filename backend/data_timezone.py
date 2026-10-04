# Multi-timezone Digital Clock
# Displays current time in different time zones relevant to airport operations

TIMEZONES = [
    {"name": "Local (WIB)", "timezone": "Asia/Jakarta", "offset": "UTC+7", "city": "Jakarta", "region": "Terminal Local"},
    {"name": "Singapore (SGT)", "timezone": "Asia/Singapore", "offset": "UTC+8", "city": "Singapore", "region": "Regional Hub"},
    {"name": "Bangkok (ICT)", "timezone": "Asia/Bangkok", "offset": "UTC+7", "city": "Bangkok", "region": "Regional Hub"},
    {"name": "Hong Kong (HKT)", "timezone": "Asia/Hong_Kong", "offset": "UTC+8", "city": "Hong Kong", "region": "Asia Pacific"},
    {"name": "Tokyo (JST)", "timezone": "Asia/Tokyo", "offset": "UTC+9", "city": "Tokyo", "region": "Asia Pacific"},
    {"name": "Sydney (AEST)", "timezone": "Australia/Sydney", "offset": "UTC+10", "city": "Sydney", "region": "Asia Pacific"},
    {"name": "Dubai (GST)", "timezone": "Asia/Dubai", "offset": "UTC+4", "city": "Dubai", "region": "Middle East"},
    {"name": "London (GMT)", "timezone": "Europe/London", "offset": "UTC+0", "city": "London", "region": "Europe"},
    {"name": "Paris (CET)", "timezone": "Europe/Paris", "offset": "UTC+1", "city": "Paris", "region": "Europe"},
    {"name": "New York (EST)", "timezone": "America/New_York", "offset": "UTC-5", "city": "New York", "region": "North America"},
    {"name": "Los Angeles (PST)", "timezone": "America/Los_Angeles", "offset": "UTC-8", "city": "Los Angeles", "region": "North America"},
    {"name": "Sydney Morning", "timezone": "Australia/Sydney", "offset": "UTC+10", "city": "Sydney", "region": "Next Day"},
]

CLOCK_CONFIG = {
    "format": "24h",  # 24h or 12h
    "show_seconds": True,
    "show_date": True,
    "auto_update_interval": 1000,  # milliseconds
    "theme": "dark",  # dark or light
}
