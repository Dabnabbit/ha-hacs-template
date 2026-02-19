"""DataUpdateCoordinator for HACS Template."""

from __future__ import annotations

import logging
from datetime import timedelta
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DEFAULT_SCAN_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)


class TemplateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Coordinator to manage data fetching from the service."""

    config_entry: ConfigEntry

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self.config_entry = entry
        session = async_get_clientsession(hass)
        # TODO: Initialize your API client here using the managed session
        # self.client = MyApiClient(
        #     host=entry.data[CONF_HOST],
        #     port=entry.data[CONF_PORT],
        #     session=session,
        # )

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from the service."""
        try:
            # TODO: Replace with actual API call
            # data = await self.client.async_get_data()
            data: dict[str, Any] = {}
            return data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}") from err
