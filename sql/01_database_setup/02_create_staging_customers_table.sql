/* customers table
 -> customer_id -> Text primary key
 -> customer_unqiue_id -> text Not Null
 -> customer_zip_code_prefix -> Text Not Null
 -> customer_city -> Text
 -> customer_state -> Varchar(2)
 */ 

create table staging.customers (customer_id TEXT PRIMARY KEY, 
						customer_unqiue_id TEXT NOT NULL ,
						customer_zip_code_prefix TEXT NOT NULL,
						customer_city TEXT NOT NULL,
						customer_state  VARCHAR(2) NOT NULL
						) 


-- Insert data by using import export from clicking on table and import from csv
-- select count(*) from staging.customers; to check if data is loaded