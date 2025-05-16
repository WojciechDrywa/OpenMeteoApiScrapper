{{ config(materialized='view') }}

SELECT
    location,
    timestamp::date as date,
    ROUND(AVG(temperature_2m_max + temperature_2m_min) / 2.0, 1) as avg_temperature,
    ROUND(AVG(temperature_2m_max), 1) as max_temperature,
    ROUND(AVG(temperature_2m_min), 1) as min_temperature,
    'forecast' as source,
    'daily' as frequency
FROM
    {{ ref('clean_daily_forecast')}}
GROUP BY
    location, date

UNION ALL

SELECT
    location,
    timestamp::date as date,
    ROUND(AVG(temperature_2m_max + temperature_2m_min) / 2.0, 1) as avg_temperature,
    ROUND(AVG(temperature_2m_max), 1) as max_temperature,
    ROUND(AVG(temperature_2m_min), 1) as min_temperature,
    'historical' as source,
    'daily' as frequency
FROM
    {{ ref('clean_daily_historical')}}
GROUP BY
    location, date
ORDER BY
    location, date
