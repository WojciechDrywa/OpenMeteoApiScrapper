SELECT
    timestamp::timestamp AS timestamp,
    location,
    temperature_2m::numeric AS temperature_2m,
    relative_humidity_2m::numeric AS relative_humidity_2m,
    cloud_cover::numeric AS cloud_cover,
    apparent_temperature::numeric AS apparent_temperature,
    wind_speed_10m::numeric AS wind_speed_10m,
    wind_direction_10m::numeric AS wind_direction_10m,
    wind_gusts_10m::numeric AS wind_gusts_10m,
    snowfall::numeric AS snowfall,
    precipitation_probability::numeric AS precipitation_probability,
    rain::numeric AS rain,
    showers::numeric AS showers,
    is_day
FROM {{ source('weather_data', 'hourly_current') }}
