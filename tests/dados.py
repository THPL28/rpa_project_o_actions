"""Synthetic, non-secret data used by UI tests."""

from datetime import datetime, timezone


def registration_data() -> dict[str, str]:
    """Create unique synthetic registration data for the demo application."""
    suffix = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
    password = "DemoTest!2026"
    return {
        "firstname": "Automation",
        "lastname": "Test",
        "address": "100 Test Street",
        "city": "Testville",
        "state": "California",
        "zipcode": "90001",
        "phone": "5550000000",
        "ssn": "000-00-0000",
        "username": f"oa_{suffix}",
        "password": password,
        "confirm": password,
    }
