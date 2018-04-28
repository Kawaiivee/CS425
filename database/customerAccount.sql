USE ecommerce;
<<<<<<< HEAD
CREATE OR REPLACE VIEW customerAccount AS
    SELECT 
        Customer.address AS address,
        Customer.customer_name AS firstname,
        Customer.customer_id AS id,
        Customer.email AS email,
        Customer.password AS psw,
        'My Account' AS title,
        '0' AS stat
    FROM
        Customer
=======

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
>>>>>>> origin/master
