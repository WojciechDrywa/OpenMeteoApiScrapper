{{ config(materialized='view') }}

SELECT
    location,
    TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI') as date,
    ROUND(AVG(temperature_2m), 1) as avg_temperature,
    'forecast' as source,
    'hourly' as frequency
FROM
    {{ ref('clean_hourly_forecast')}}
GROUP BY 
    location, TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI'), temperature_2m, source, frequency

UNION ALL

SELECT
    location,
    TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI') as date,
    ROUND(AVG(temperature_2m), 1) as avg_temperature,
    'historical' as source,
    'hourly' as frequency
FROM
    {{ ref('clean_hourly_historical')}}
GROUP BY 
    location, TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI'), temperature_2m, source, frequency
ORDER BY
    location, date
