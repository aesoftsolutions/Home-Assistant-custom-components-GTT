import logging
import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, CONF_STOP_ID, SCAN_INTERVAL
from .api import GTTClient, GTTStopData

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the integration from a ConfigEntry"""

    # Create an aiohttp client for HTTP requests
    session = aiohttp.ClientSession()
    client = GTTClient(entry.data[CONF_STOP_ID], session)

    #Initialize the DataUpdateCoordinator
    async def async_update_data():
        """Function to retrieve data from the GTTTools API"""
        dataInfo = await client.get_stop_data()
        if dataInfo is None:
            _LOGGER.error("Unable to retrieve GTTTools data or parsing error.")
            raise UpdateFailed("Unable to retrieve GTTTools data or parsing error.")

        """Function to retrieve data from the GTT API"""
        dataArrivals = await client.get_next_arrivals()
        if dataArrivals is None:
            _LOGGER.error("Unable to retrieve GTT data or parsing error.")
            raise UpdateFailed("Unable to retrieve GTT data or parsing error.")

        return GTTStopData(info=dataInfo, arrivals=dataArrivals)

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=DOMAIN,
        update_method=async_update_data,
        update_interval=SCAN_INTERVAL,
    )

    # Performs the first update
    await coordinator.async_config_entry_first_refresh()

    # Forward the configuration to the sensor platform
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Download the integration"""
    # Download the platforms
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    # Remove the coordinator
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok