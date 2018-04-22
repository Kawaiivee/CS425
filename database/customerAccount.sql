USE ecommerce;

DROP  VIEW `customerAccount`;
CREATE VIEW `customerAccount` as 
SELECT Customer.address as address,
	Customer.customer_name as firstname,
    Customer.customer_id as cid,
    Customer.email as email,
    Customer.password as passwd,
    "My Account" as title,
    "0" as stat
FROM Customer, Product