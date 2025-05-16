import pytest
from unittest.mock import patch, MagicMock
from weather.service import WeatherService

@patch("weather.service.openmeteo_requests.Client")
def test_get_weather_forecast_mocked(mock_client_class):
    mock_variables = {"temperature_2m": [20.1, 20.2]}
    
    mock_hourly = MagicMock()
    mock_hourly.Variables = mock_variables
    
    mock_response = MagicMock()
    mock_response.Hourly.return_value = mock_hourly
    
    mock_client = MagicMock()
    mock_client.weather_api.return_value = [mock_response]
    mock_client_class.return_value = mock_client
    
    service = WeatherService()
    lat, lon = 52.1, 20.9
    result = service.get_weather_forecast(lat, lon)
    
    assert result is not None
