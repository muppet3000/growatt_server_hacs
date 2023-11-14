"""Define constants for the Growatt Server component."""
from homeassistant.const import Platform

CONF_PLANT_ID = "plant_id"

DEFAULT_PLANT_ID = "0"

DEFAULT_NAME = "Growatt"

SERVER_URLS = [
    "https://openapi.growatt.com/",
    "https://server-api.growatt.com/",
    "https://server.growatt.com/",
    "https://server-us.growatt.com/",
    "https://server.pvbutler.com/",
    "http://server.smten.com/",
    "https://pvplusanz.jinkosolar.com/",
]

DEPRECATED_URLS: list[str] = []

DEFAULT_URL = SERVER_URLS[0]

DOMAIN = "growatt_server_api"

PLATFORMS = [Platform.SENSOR]

LOGIN_INVALID_AUTH_CODE = "502"
