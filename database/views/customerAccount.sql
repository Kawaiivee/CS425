USE ecommerce;

CREATE or replace VIEW customerAccount AS
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