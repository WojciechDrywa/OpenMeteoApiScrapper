{{ config(materialized='view') }}

SELECT
    location,
    TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI') as date,
    precipitation_probability,
    rain as rain,
    showers as showers,
    'forecast' as source,
    'hourly' as frequency
FROM
    {{ ref('clean_hourly_forecast')}}

UNION ALL

SELECT
    location,
    TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI') as date,
    precipitation_probability,
    rain as rain,
    showers as showers,
    'historical' as source,
    'hourly' as frequency
FROM
    {{ ref('clean_hourly_historical')}}

GROUP BY
    location, TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI'), precipitation_probability, rain, showers
