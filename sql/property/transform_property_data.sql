INSERT INTO location.property_clean (
        location_name,
        property_name,
        property_code)
SELECT location_name,
       property_name,
       property_code
FROM location.property
WHERE 
	location_name NOT LIKE '%(disabloitu)%'
	AND location_name NOT LIKE '%(disabled)%'
	AND property_name NOT LIKE '%(disabloitu)%'
	AND property_name NOT LIKE '%(disabled)%'

	AND location_name NOT LIKE '%New property%'

	AND location_name != ''
	AND property_name != ''
	AND property_code != '';