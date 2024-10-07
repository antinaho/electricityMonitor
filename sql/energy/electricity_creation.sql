CREATE TABLE IF NOT EXISTS electricity(
    location_name VARCHAR(255) REFERENCES property_clean(location_name),
    timestamp VARCHAR(255),
    value DECIMAL,
    unit VARCHAR(10)
);