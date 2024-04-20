"""Matterbridge Message platform for notify component."""
from __future__ import annotations

from typing import Any

import voluptuous as vol
import requests
import logging


from homeassistant.components.notify import (
    ATTR_DATA,
    PLATFORM_SCHEMA,
    BaseNotificationService,
)
from homeassistant.const import CONTENT_TYPE_JSON
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

CONF_URL = "url"
CONF_KEY = "key"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_URL): cv.string,
        vol.Required(CONF_KEY): cv.string,
    }
)

def get_service(hass, config, discovery_info=None):
    """Get the Matterbridge Message notification service."""
    return HaxkoNotificationService(
        config[CONF_URL], config[CONF_KEY]
    )

class HaxkoNotificationService(BaseNotificationService):
    """Implementation of a notification service for the Matterbridge Message service."""

    def __init__(self, url, key):
        """Initialize the service."""
        self.url = url
        self.key = key

    def send_message(self, message="", **kwargs):
        """Send a message."""
        message = message.strip()

        headers = {
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/text"
        }

        response = requests.post(self.url, headers=headers, data=message)

        if response.status_code == 200:
            _LOGGER.info(f"Posted message '{message}' to matterbridge")
            pass
        else:
            _LOGGER.error(f"Failed to send message '{message}' to the API. Status code: {response.status_code}")
            pass
        
