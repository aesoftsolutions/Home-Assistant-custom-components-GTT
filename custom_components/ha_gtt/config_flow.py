import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError

from .const import DOMAIN, CONF_STOP_ID, CONF_NAME, DEFAULT_TITLE

# Schema for input validation
DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_STOP_ID): str,
    vol.Optional(CONF_NAME, default=DEFAULT_TITLE): str,
})

class GTTTorinoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """GTT configuration flow"""
    
    VERSION = 1
                    
    async def async_step_user(self, user_input=None):
        """Handles the initial step called by the user"""
        errors = {}

        if user_input is not None:
            # Check to ensure there are no duplicate integrations with the same stop_id
            await self.async_set_unique_id(user_input[CONF_STOP_ID])
            self._abort_if_unique_id_configured()
                                                                                                
            # Here you could add a stop ID validation by calling the API
            # But in this first version, we proceed directly with the creation of the entry.
                                                                                                                                    
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )

        # Show form data
        return self.async_show_form(
            step_id="user", 
            data_schema=DATA_SCHEMA, 
            errors=errors,
        )                                                                                                                                                                                                                                                 
