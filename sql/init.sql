CREATE SCHEMA location;

DROP TABLE IF EXISTS location.property;
CREATE TABLE location.property(
	location_name VARCHAR(255) PRIMARY KEY NOT NULL,
	property_name VARCHAR(255) NOT NULL,
	property_code VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS location.property_clean;
CREATE TABLE location.property_clean(
	location_name VARCHAR(255) PRIMARY KEY NOT NULL,
	property_name VARCHAR(255),
	property_code VARCHAR(255)
);


CREATE SCHEMA energy;

DROP TABLE IF EXISTS energy.electricity;
CREATE TABLE energy.electricity(
    timestamp VARCHAR(255),
    reporting_group VARCHAR(255),
    location_name VARCHAR(255) REFERENCES location.property_clean(location_name),
    value DECIMAL,
    unit VARCHAR(10)
);

DROP TABLE IF EXISTS energy.electricity_clean;
CREATE TABLE energy.electricity_clean(
	location_name VARCHAR(255),
    timestamp TIMESTAMP,
    value DECIMAL,
    unit VARCHAR(255)
);