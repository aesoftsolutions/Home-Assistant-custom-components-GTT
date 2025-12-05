import logging
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.helpers.typing import StateType
from homeassistant.const import UnitOfTime

from .const import DOMAIN, CONF_STOP_ID, CONF_NAME

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set the GTT sensor from the configuration entry"""

    # Retrieves the coordinator created in __init__.py
    coordinator: DataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([
        GTTSensor(coordinator, entry.data[CONF_STOP_ID], entry.data[CONF_NAME], entry)
    ], True)


class GTTSensor(SensorEntity):
    """Sensor showing GTT arrival times"""

    _attr_icon = "mdi:bus-clock"
    # Set the unit to 'min' if we can calculate the arrival in minutes
    # For now, use the generic attribute until we calculate the time

    def __init__(self, coordinator: DataUpdateCoordinator, stop_id: str, name: str, entry: ConfigEntry) -> None:
        """Initialize the sensor"""
        self.coordinator = coordinator
        self._attr_name = name
        self._attr_unique_id = f"{DOMAIN}_{stop_id}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, stop_id)},
            "name": name,
            "manufacturer": "GTT Torino",
            "model": "Arrivi in fermata",
            # "suggested_area": "Home",
        }
        self._stop_id = stop_id

    @property
    def native_value(self) -> StateType:
        """Returns the main value (first arrival in real time)"""
        data = self.coordinator.data.arrivals
        if data and isinstance(data, list) and len(data) > 0:
            # We find the first arrival among all the lines
            first_arrival_time = None
            first_arrival_line = None

            # Let's assume we use the first arrival of the first line as the main state
            first_line_data = data[0]
            return first_line_data.get("primo_arrivo", "N/A")

        return "N/A"

    @property
    def extra_state_attributes(self):
        """Returns extra attributes (full arrival list)"""
        attributes = {
            "stop_id": self._stop_id,
            "stop_name": self.coordinator.data.info[0].get("name"),
            "stop_desc": self.coordinator.data.info[0].get("description"),
            "stop_city": self.coordinator.data.info[0].get("city"),
            "line_arrivals": self.coordinator.data.arrivals or [],
        }

        # Let's add an attribute for the next bus/tram ever
        if self.coordinator.data:
            # Find the closest arrival point among all lines
            # For simplicity, let's consider the first arrival of the first line in the JSON
            first_line_data = self.coordinator.data.arrivals[0]
            attributes["incoming_line"] = first_line_data.get("linea")
            attributes["direction_next"] = first_line_data.get("direzione")

        return attributes

    @property
    def available(self) -> bool:
        """Returns True if the data was loaded successfully."""
        return self.coordinator.last_update_success

    # Required to use the DataUpdateCoordinator
    async def async_added_to_hass(self) -> None:
        """Register coordinator listeners when the entity is added"""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    @property
    def should_poll(self) -> bool:
        """Indicates that the entity uses the coordinator and should not poll directly"""
        return False