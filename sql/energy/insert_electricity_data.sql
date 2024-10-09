INSERT INTO energy.electricity (
    timestamp,
    reporting_group,
    location_name,
    value,
    unit)
VALUES (
    %s,
    %s,
    %s,
    %s,
    %s);