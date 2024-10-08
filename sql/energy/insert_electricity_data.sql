INSERT INTO energy.electricity (
    location_name,
    timestamp,
    value,
    unit)
VALUES (
    %s,
    %s,
    %s,
    %s);