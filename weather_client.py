"""
Client for fetching weather data from a public API.
"""

import requests
from typing import Dict, Optional


def get_weather(city: str, api_key: str) -> Optional[Dict]:
    """Fetch current weather for a city. Returns None on failure."""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
        }
    except requests.RequestException:
        return None
