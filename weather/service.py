import openmeteo_requests
import requests_cache
from retry_requests import retry
from datetime import date, timedelta
from config.weather_variables import HOURLY, DAILY


class WeatherService:
    def __init__(self):
        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        self.client = openmeteo_requests.Client(session=retry_session)
        
    def _fetch(self, url: str, params: dict):
        responses = self.client.weather_api(url, params=params)
        return responses[0] if responses else None


    def get_historical_weather(self, latitude: float, longitude: float, start_date: str, end_date: str):
        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "start_date": start_date,
            "end_date": end_date,
            "hourly": HOURLY,
            "daily": DAILY,
            "timezone": "auto"
        }

        return self._fetch(url, params)

    def get_weather(self, latitude: float, longitude: float):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": HOURLY,
            "daily": DAILY,
            "forecast_days": 1
        }
        
        return self._fetch(url, params)

    def get_weather_forecast(self, latitude: float, longitude: float):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": HOURLY,
            "daily": DAILY,
            "start_date": (date.today() - timedelta(days=1)).strftime("%Y-%m-%d"),
            "end_date": (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")
        }
        
        response = self._fetch(url, params)
        return response 