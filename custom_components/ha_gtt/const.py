"""Constants for GTT"""

from datetime import timedelta

# Configuration keys
NAME = "GTT"
DOMAIN = "ha_gtt"

CONF_STOP_ID = "stop_id"
CONF_NAME = "name"
DEFAULT_TITLE = "GTT arrivi in fermata"

# Update interval (60 seconds)
SCAN_INTERVAL = timedelta(seconds=60)

# URL API GTT
# {stop_id} is the placeholder for stop ID
GTT_API_URL = "https://www.gtt.to.it/cms/index.php?option=com_gtt&task=palina.getTransitiOld&realtime=true&get_param=value&palina={stop_id}"
GTTTOOLS_API_URL = "https://tools.gtt.cx/api/search-stop/{stop_id}"