/*
order_items 
order_id -> TEXT NOT NULL
order_item_id -> INTEGER NOT NULL
product_id -> TEXT NOT NULL 
seller_id -> TEXT NOT NULL
shipping_limit_date -> TIMESTAMP NOT NULL
price ->  NOT NULL Check  value >= 0
freight_value -> NOT NULL CHECK VALUE >=0 
order_id , order_item_id provides PRIMARY key
*/

CREATE TABLE staging.order_items (
	order_id TEXT NOT NULL,
	order_item_id INTEGER NOT NULL,
	product_id  TEXT NOT NULL,
	seller_id  TEXT NOT NULL,
	shipping_limit_date TIMESTAMP NOT NULL,
	price NUMERIC(10,2) NOT NULL ,
	freight_value NUMERIC(10,2) NOT NULL ,
	CONSTRAINT pk_order_ietms
	PRIMARY KEY (
		order_id, 
		order_item_id
		) ,
	CONSTRAINT chk_order_items_price
		CHECK (price>=0),
	CONSTRAINT chk_order_items_freight_value
		CHECK(freight_value>=0)
)
