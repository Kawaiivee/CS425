USE ecommerce;

DROP VIEW `customerCart`;
CREATE VIEW `customerCart` as 
SELECT
	Customer.customer_name as firstname,
	Customer.customer_id as cid,
    Product.product_id as pid,
    
    "My Cart" as title,
    "0" as stat
FROM Customer, Product
WHERE