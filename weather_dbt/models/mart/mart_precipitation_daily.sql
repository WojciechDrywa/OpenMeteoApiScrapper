{{ config(materialized='view') }}

SELECT
    location,
    timestamp::date as date,
    SUM(ROUND(
        COALESCE(
            COALESCE(precipitation_sum, 0) / NULLIF(COALESCE(precipitation_hours, 0), 0),
            0
        ),
    1)) AS avg_precipitation,
    SUM(precipitation_sum) as total_precipitation,
    ROUND(AVG(precipitation_hours), 1) as total_precipitation_hours,
    SUM(rain_sum) as rain,
    SUM(snowfall_sum) as snow,
    'forecast' as source,
    'daily' as frequency
FROM
    {{ ref('clean_daily_forecast')}}
GROUP BY
    location, date, precipitation_sum, precipitation_hours

UNION ALL

SELECT
    location,
    timestamp::date as date,
    SUM(ROUND(
        COALESCE(
            COALESCE(precipitation_sum, 0) / NULLIF(COALESCE(precipitation_hours, 0), 0),
            0
        ),
    1)) AS avg_precipitation,
    SUM(precipitation_sum) as total_precipitation,
    ROUND(AVG(precipitation_hours), 1) as total_precipitation_hours,
    SUM(rain_sum) as rain,
    SUM(snowfall_sum) as snow,
    'historical' as source,
    'daily' as frequency
FROM
    {{ ref('clean_daily_historical')}}
GROUP BY
    location, date, precipitation_sum, precipitation_hours
ORDER BY
    location, date
