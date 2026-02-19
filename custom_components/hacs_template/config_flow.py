"""Config flow for HACS Template integration."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_HOST, CONF_PORT

from .const import DEFAULT_PORT, DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
        vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
    }
)


class TemplateConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for HACS Template."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            # TODO: Validate connection to the service
            # try:
            #     await validate_connection(user_input)
            # except CannotConnect:
            #     errors["base"] = "cannot_connect"
            # except InvalidAuth:
            #     errors["base"] = "invalid_auth"
            # except Exception:
            #     _LOGGER.exception("Unexpected exception")
            #     errors["base"] = "unknown"

            if not errors:
                return self.async_create_entry(
                    title=user_input[CONF_HOST],
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )
