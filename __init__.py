"""Matterbridge Message Push Integration."""

from homeassistant import core

async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Matterbridge Message Push component."""
    return True