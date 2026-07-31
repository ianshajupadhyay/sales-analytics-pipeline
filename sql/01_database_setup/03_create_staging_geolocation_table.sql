/* geolocation table
 -> geolocation_zip_code_prefix -> Text
 -> geolocation_lat -> Numberic Not Null
 -> geolocation_lng -> Numberic Not Null
 -> geolocation_city -> Text
 -> geolocation_state -> Varchar(2)
 */ 

 create table staging.geolocation (
	geolocation_zip_code_prefix TEXT NOT NULL, 
	geolocation_lat NUMERIC NOT NULL, 
	geolocation_lng NUMERIC NOT NULL, 
	geolocation_city TEXT NOT NULL,
	geolocation_state VARCHAR(2) NOT NULL,
	PRIMARY KEY (
		geolocation_zip_code_prefix, 
		geolocation_lat, 
		geolocation_lng , 
		geolocation_city , 
		geolocation_state)
 )