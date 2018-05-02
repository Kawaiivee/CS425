USE ecommerce;

CREATE or replace VIEW supplierAccount AS
	SELECT
		Supplier.address AS address,
        Supplier.supplier_id as id,
        Supplier.supplier_name AS firstname,
        Supplier.email AS email,
        Supplier.password AS psw,
        'My Account' AS title,
        '0' AS stat
	FROM
		Supplier