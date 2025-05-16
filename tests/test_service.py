import pytest
from weather.service import WeatherService
from config.locations import LOCATIONS

@pytest.fixture
def service():
    return WeatherService()

def test_get__historical_weather(service):
    lat = 54.3521
    lon = 18.6464
    start = "2025-04-10"
    end = "2025-04-10"
    
    data = service.get_historical_weather(lat, lon, start, end)
    
    assert data is not None
    assert hasattr(data, 'Hourly')
    assert hasattr(data.Hourly(), 'Variables')
    assert hasattr(data, 'Daily')
    assert hasattr(data.Daily(), 'Variables')
    
def test_get_weather(service):
    lat = 53.8836
    lon = 18.2137
    
    data = service.get_weather(lat, lon)
    
    assert data is not None
    assert hasattr(data, 'Hourly')
    assert hasattr(data.Hourly(), 'Variables')
    assert hasattr(data, 'Daily')
    assert hasattr(data.Daily(), 'Variables')
    
def test_get_weather_forecast(service):
    lat = LOCATIONS["dabrowa"]["latitude"]
    lon = LOCATIONS["dabrowa"]["longitude"]

    data = service.get_weather_forecast(lat, lon)
    
    assert data is not None
    assert hasattr(data, 'Hourly')
    assert hasattr(data.Hourly(), 'Variables')
    assert hasattr(data, 'Daily')
    assert hasattr(data.Daily(), 'Variables')
    