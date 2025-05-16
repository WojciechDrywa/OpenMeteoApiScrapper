SELECT
    timestamp,
    location,
    ROUND(temperature_2m::numeric, 1) AS temperature_2m,
    ROUND(relative_humidity_2m::numeric, 1) AS relative_humidity_2m,
    ROUND(cloud_cover::numeric, 1) AS cloud_cover,
    ROUND(apparent_temperature::numeric, 1) AS apparent_temperature,
    ROUND(wind_speed_10m::numeric, 1) AS wind_speed_10m,
    ROUND(wind_direction_10m::numeric, 1) AS wind_direction_10m,
    ROUND(wind_gusts_10m::numeric, 1) AS wind_gusts_10m,
    ROUND(snowfall::numeric, 1) AS snowfall,
    ROUND(precipitation_probability::numeric, 1) AS precipitation_probability,
    ROUND(rain::numeric, 1) AS rain,
    ROUND(showers::numeric, 1) AS showers,
    is_day
FROM {{ ref('stg_hourly_historical') }}
WHERE
    temperature_2m IS NOT NULL
    AND relative_humidity_2m IS NOT NULL
    AND cloud_cover IS NOT NULL
    AND apparent_temperature IS NOT NULL
    AND wind_speed_10m IS NOT NULL
    AND wind_direction_10m IS NOT NULL
    AND wind_gusts_10m IS NOT NULL
    AND snowfall IS NOT NULL
    AND rain IS NOT NULL
    AND showers IS NOT NULL
