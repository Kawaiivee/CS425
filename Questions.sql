/*
1.	Find all products missing a product model number?
*/
SELECT *
FROM products
WHERE products.products_model Is Null;

/*
2.	Find all products with over $500 and less than $699?
*/
SELECT *
FROM products
WHERE products.products_price>500
and  products.products_price<699;


/*
3.	Find all products that need to be ordered?
*/
SELECT *
FROM products
WHERE products.products_quantity <=2;

/*
4.	Find all products in Leather Laptop Cases category?
*/
SELECT products.*
FROM products INNER JOIN (categories_description INNER JOIN products_to_categories ON categories_description.categories_id = products_to_categories.categories_id) ON products.products_id = products_to_categories.products_id
WHERE (((categories_description.categories_name)="Leather Laptop Cases"));


/*
5.	Find all Categories with the  in the text?
*/
SELECT *
FROM categories
WHERE (((categories.categories_keywords) Like "*women*"));


/*
6.	Find all categories added in 2014?
*/
SELECT *
FROM categories
WHERE year( categories.date_added)=2014;


/*
7.	Find all categories added before 2014 and has not been modified?
*/
SELECT *
FROM categories
WHERE (((categories.last_modified)='NULL') AND ((Year([categories].[date_added]))<2014));



/*
8.	Find all products to all main categories (main category has no parent)?
*/
SELECT *
FROM (products INNER JOIN products_to_categories ON products.products_id = products_to_categories.products_id) INNER JOIN categories ON products_to_categories.categories_id = categories.categories_id
WHERE (([categories].[parent_id]=0));


/*
9.	Find all products that are Tote Bags?
*/
SELECT products.*, categories_description.categories_name
FROM categories, products INNER JOIN (products_to_categories INNER JOIN categories_description ON products_to_categories.categories_id = categories_description.categories_id) ON products.products_id = products_to_categories.products_id
WHERE (((categories_description.categories_name)='Tote Bags'));


/*
10.	List all product models that does not start with word "BAG"
*/
SELECT *
FROM products
WHERE (([products].[products_model] Not Like 'BAG*'));
