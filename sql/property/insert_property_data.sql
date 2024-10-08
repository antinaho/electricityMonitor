INSERT INTO location.property(
	location_name, 
	property_name, 
	property_code)
VALUES(
	%s,
	%s,
	%s
)
ON CONFLICT (location_name) DO NOTHING;

