CREATE TABLE IF NOT EXISTS hourly_forecast (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ,
    temperature_2m FLOAT,
    relative_humidity_2m FLOAT,
    cloud_cover FLOAT,
    apparent_temperature FLOAT,
    wind_speed_10m FLOAT,
    wind_direction_10m FLOAT,
    wind_gusts_10m FLOAT,
    snowfall FLOAT,
    precipitation_probability FLOAT,
    rain FLOAT,
    showers FLOAT,
    is_day BOOLEAN,
    location TEXT
);

CREATE TABLE IF NOT EXISTS hourly_current (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ,
    temperature_2m FLOAT,
    relative_humidity_2m FLOAT,
    cloud_cover FLOAT,
    apparent_temperature FLOAT,
    wind_speed_10m FLOAT,
    wind_direction_10m FLOAT,
    wind_gusts_10m FLOAT,
    snowfall FLOAT,
    precipitation_probability FLOAT,
    rain FLOAT,
    showers FLOAT,
    is_day BOOLEAN,
    location TEXT
);

CREATE TABLE IF NOT EXISTS hourly_historical (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ,
    temperature_2m FLOAT,
    relative_humidity_2m FLOAT,
    cloud_cover FLOAT,
    apparent_temperature FLOAT,
    wind_speed_10m FLOAT,
    wind_direction_10m FLOAT,
    wind_gusts_10m FLOAT,
    snowfall FLOAT,
    precipitation_probability FLOAT,
    rain FLOAT,
    showers FLOAT,
    is_day BOOLEAN,
    location TEXT
);

CREATE TABLE IF NOT EXISTS daily_forecast (
    id SERIAL PRIMARY KEY,
    timestamp DATE,
    temperature_2m_max FLOAT,
    temperature_2m_min FLOAT,
    precipitation_sum FLOAT,
    rain_sum FLOAT,
    snowfall_sum FLOAT,
    precipitation_hours FLOAT,
    sunshine_duration FLOAT,
    daylight_duration FLOAT,
    wind_speed_10m_max FLOAT,
    wind_gusts_10m_max FLOAT,
    wind_direction_10m_dominant FLOAT,
    location TEXT
);

CREATE TABLE IF NOT EXISTS daily_current (
    id SERIAL PRIMARY KEY,
    timestamp DATE,
    temperature_2m_max FLOAT,
    temperature_2m_min FLOAT,
    precipitation_sum FLOAT,
    rain_sum FLOAT,
    snowfall_sum FLOAT,
    precipitation_hours FLOAT,
    sunshine_duration FLOAT,
    daylight_duration FLOAT,
    wind_speed_10m_max FLOAT,
    wind_gusts_10m_max FLOAT,
    wind_direction_10m_dominant FLOAT,
    location TEXT
);

CREATE TABLE IF NOT EXISTS daily_historical (
    id SERIAL PRIMARY KEY,
    timestamp DATE,
    temperature_2m_max FLOAT,
    temperature_2m_min FLOAT,
    precipitation_sum FLOAT,
    rain_sum FLOAT,
    snowfall_sum FLOAT,
    precipitation_hours FLOAT,
    sunshine_duration FLOAT,
    daylight_duration FLOAT,
    wind_speed_10m_max FLOAT,
    wind_gusts_10m_max FLOAT,
    wind_direction_10m_dominant FLOAT,
    location TEXT
);
