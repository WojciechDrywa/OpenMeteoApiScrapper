SELECT
    timestamp::timestamp AS timestamp,
    location,
    ROUND(temperature_2m_max::numeric, 1) AS temperature_2m_max,
    ROUND(temperature_2m_min::numeric, 1) AS temperature_2m_min,
    ROUND(precipitation_sum::numeric, 1) AS precipitation_sum,
    ROUND(rain_sum::numeric, 1) AS rain_sum,
    ROUND(snowfall_sum::numeric, 1) AS snowfall_sum,
    ROUND(precipitation_hours::numeric, 1) AS precipitation_hours,
    ROUND(sunshine_duration::numeric / 60.0, 1) AS sunshine_duration,
    ROUND(daylight_duration::numeric / 60.0, 1) AS daylight_duration,
    ROUND(wind_speed_10m_max::numeric, 1) AS wind_speed_10m_max,
    ROUND(wind_gusts_10m_max::numeric, 1) AS wind_gusts_10m_max,
    COALESCE(wind_direction_10m_dominant::numeric, null) AS wind_direction_10m_dominant
FROM {{ ref('stg_daily_forecast') }}
WHERE
    temperature_2m_max IS NOT NULL
    AND temperature_2m_min IS NOT NULL
    AND precipitation_sum IS NOT NULL
    AND rain_sum IS NOT NULL
    AND snowfall_sum IS NOT NULL
    AND wind_speed_10m_max IS NOT NULL
    AND wind_gusts_10m_max IS NOT NULL
