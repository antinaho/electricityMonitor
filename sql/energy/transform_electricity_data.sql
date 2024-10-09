INSERT INTO energy.electricity_clean (
    location_name,
    timestamp,
    value,
    unit)
SELECT
    location_name,
    to_timestamp(timestamp, 'YYYY-MM-DD HH24:MI:SS'),
    value,
    unit
FROM energy.electricity
WHERE
    value >= 0;
