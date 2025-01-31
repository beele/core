"""Test evil genius labs diagnostics."""
import pytest

from tests.components.diagnostics import get_diagnostics_for_config_entry


@pytest.mark.parametrize("platforms", [[]])
async def test_entry_diagnostics(
    hass, hass_client, setup_evil_genius_labs, config_entry, data_fixture, info_fixture
):
    """Test config entry diagnostics."""
    assert await get_diagnostics_for_config_entry(hass, hass_client, config_entry) == {
        "info": {
            **info_fixture,
            "wiFiSsidDefault": "REDACTED",
            "wiFiSSID": "REDACTED",
        },
        "data": data_fixture,
    }
