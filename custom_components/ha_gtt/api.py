import aiohttp
import async_timeout
import logging

from .const import GTT_API_URL, GTTTOOLS_API_URL

_LOGGER = logging.getLogger(__name__)
TIMEOUT = 10

class GTTStopData:
    info: list[dict]
    arrivals: list[dict]

    def __init__(self, info: list[dict], arrivals: list[dict]) -> None:
        self.info = info
        self.arrivals = arrivals

class GTTClient:
    """Client for interaction with GTT API"""
        
    def __init__(self, stop_id: str, session: aiohttp.ClientSession) -> None:
        """Init client API"""
        self._stop_id = stop_id
        self._session = session
        self._urlGtt = GTT_API_URL.format(stop_id=stop_id)
        self._urlGttTools = GTTTOOLS_API_URL.format(stop_id=stop_id)
        
    async def get_next_arrivals(self) -> list[dict] | None:
        """Retrieve and process next arrivals"""
        _LOGGER.debug("Fetching data for stop ID: %s", self._stop_id)
        
        try:
            async with async_timeout.timeout(TIMEOUT):
                response = await self._session.get(self._urlGtt)
                response.raise_for_status() # Exception for HTTP errors (like 4xx or 5xx)
                
                # GTT API return a JSON string with an array
                data = await response.json(content_type=None)
                
                # Analyze the return and create a simple list of arrivals
                arrivals = []
                for line_data in data:
                    # Retrieve the first real-time arrival
                    rt_arrivals = line_data.get("PassaggiRT", [])
                    first_arrival = rt_arrivals[0] if rt_arrivals else "N/A"
                    
                    arrivals.append({
                        "linea": line_data.get("Linea"),
                        "direzione": line_data.get("Direzione"),
                        "prossimi_rt": rt_arrivals,
                        "primo_arrivo": first_arrival,
                    })
                    
                return arrivals
                
        except aiohttp.ClientError as err:
            _LOGGER.error("Connection error with GTT API for stop ID %s: %s", self._stop_id, err)
            return None
        except Exception as err:
            _LOGGER.error("Error while parsing GTT data for stop ID %s: %s", self._stop_id, err)
            return None
        
    async def get_stop_data(self) -> list[dict] | None:
        """Retrieve and process stop data"""
        _LOGGER.debug("Fetching data for stop ID: %s", self._stop_id)
        
        try:
            async with async_timeout.timeout(TIMEOUT):
                response = await self._session.get(self._urlGttTools)
                response.raise_for_status() # Exception for HTTP errors (like 4xx or 5xx)
                
                # GTTTools API return a JSON string with an array
                data = await response.json(content_type=None)
                
                # Analyze the return and create a simple stopdata
                stopdata = []
                for stop_data in data:
                    # Retrieve stop data
                    stopdata.append({
                        "code": stop_data.get("code"),
                        "name": stop_data.get("name"),
                        "description": stop_data.get("description"),
                        "city": stop_data.get("city")
                    })
                    
                return stopdata
                
        except aiohttp.ClientError as err:
            _LOGGER.error("Connection error with GTTTools API for stop ID %s: %s", self._stop_id, err)
            return None
        except Exception as err:
            _LOGGER.error("Error while parsing GTTTools data for stop ID %s: %s", self._stop_id, err)
            return None