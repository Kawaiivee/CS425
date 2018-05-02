USE ecommerce;
CREATE OR REPLACE VIEW `customerCart` as 
SELECT
	Customer.customer_name as firstname,
	Customer.customer_id as cid,
        Product.product_id as pid,
        Product.product_name as productName,
        Product.description as productDescription,
        Cart.quantity as quantity,
        
    "My Cart" as title,
    "0" as stat
FROM Cart
inner join  Customer on Customer.customer_id = Cart.customer_id 
inner join Product on Product.product_id = Cart.product_id