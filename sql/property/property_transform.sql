CREATE TABLE IF NOT EXISTS property_clean(
	location_name VARCHAR(255) PRIMARY KEY NOT NULL,
	property_name VARCHAR(255),
	property_code VARCHAR(255)
);

INSERT INTO property_clean (location_name, property_name, property_code)
SELECT location_name, property_name, property_code
FROM property
WHERE 
	location_name NOT LIKE '%(disabloitu)%'
	AND location_name NOT LIKE '%(disabled)%'
	AND property_name NOT LIKE '%(disabloitu)%'
	AND property_name NOT LIKE '%(disabled)%'

	AND location_name NOT LIKE '%New property%'

	AND location_name NOT LIKE '%empty%'
	AND property_name NOT LIKE '%empty%'
	AND property_code != '0'
	AND property_code != ''