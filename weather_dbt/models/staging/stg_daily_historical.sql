SELECT
    timestamp::timestamp AS timestamp,
    location,
    temperature_2m_max::numeric AS temperature_2m_max,
    temperature_2m_min::numeric AS temperature_2m_min,
    precipitation_sum::numeric AS precipitation_sum,
    rain_sum::numeric AS rain_sum,
    snowfall_sum::numeric AS snowfall_sum,
    precipitation_hours::numeric AS precipitation_hours,
    sunshine_duration::numeric AS sunshine_duration,
    daylight_duration::numeric AS daylight_duration,
    wind_speed_10m_max::numeric AS wind_speed_10m_max,
    wind_gusts_10m_max::numeric AS wind_gusts_10m_max,
    wind_direction_10m_dominant::numeric AS wind_direction_10m_dominant
FROM {{ source('weather_data', 'daily_historical') }}