"""The HACS Template integration."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN, FRONTEND_SCRIPT_URL
from .coordinator import TemplateCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]


@dataclass
class HacsTemplateData:
    """Data for the HACS Template integration."""

    coordinator: TemplateCoordinator


type HacsTemplateConfigEntry = ConfigEntry[HacsTemplateData]


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the HACS Template integration."""
    frontend_path = Path(__file__).parent / "frontend"
    try:
        await hass.http.async_register_static_paths(
            [
                StaticPathConfig(
                    FRONTEND_SCRIPT_URL,
                    str(frontend_path / f"{DOMAIN}-card.js"),
                    cache_headers=True,
                )
            ]
        )
    except RuntimeError:
        # Path already registered — happens on reload
        pass
    return True


async def async_setup_entry(hass: HomeAssistant, entry: HacsTemplateConfigEntry) -> bool:
    """Set up HACS Template from a config entry."""
    coordinator = TemplateCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = HacsTemplateData(coordinator=coordinator)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: HacsTemplateConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
