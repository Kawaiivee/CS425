DROP DATABASE IF EXISTS ecommerce;
CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

/*
Creating Customer table
*/
DROP TABLE IF EXISTS Customer;
CREATE TABLE IF NOT EXISTS Customer
   (  
	address		varchar(50) not null,
	customer_name 	varchar(50) not null,
	customer_id 	int AUTO_INCREMENT not null, 
	email		varchar(50) not null,
	password	varchar(50) not null,	-- We will eventually hash this
    PRIMARY KEY (customer_id)
   );

/*
Creating CustomerAddressBook table
*/
DROP TABLE IF EXISTS CustomerAddressBook;
CREATE TABLE IF NOT EXISTS CustomerAddressBook	
   (  
   	address		varchar(50),
	counter		int UNSIGNED NOT NULL default 0,
	customer_id 	int ,	
	FOREIGN KEY(customer_id) REFERENCES Customer(customer_id)
   );

DROP TABLE IF EXISTS Product;

/*
Creating Product table
*/
CREATE TABLE IF NOT EXISTS Product	
   (
	description	varchar(250),
	image_link	varchar(250),
	price		DECIMAL(6,2) NOT null,
	product_id 	int AUTO_INCREMENT ,
	product_name	varchar(250) ,
	quantity	int not null,	
	units		varchar(50),
	refill_point	varchar(50),
	status		varchar(10),
	primary key (product_id)
   );

/*
Creating Category table
*/
DROP TABLE IF EXISTS Category;
CREATE TABLE IF NOT EXISTS Category	
   (
	attributes	varchar(250),
	category	varchar(20),
	counter		int UNSIGNED NOT NULL default 0,
	product_id 	int not null,
	FOREIGN KEY(product_id) REFERENCES Product(product_id)
   );
/*
Creating Region
*/
DROP TABLE IF EXISTS Region;
CREATE TABLE IF NOT EXISTS Region	
   (
	region_id	int NOT NULL,
	region_name	varchar(250),
	description	varchar(250),
	PRIMARY KEY(region_id)
   );

/*
Creating Cart
*/
DROP TABLE IF EXISTS Cart;
CREATE TABLE IF NOT EXISTS Cart
       (
	customer_id	int,
	product_id	int,
	quantity	int not null,
	FOREIGN KEY(customer_id) REFERENCES Customer(customer_id),
	FOREIGN KEY(product_id) REFERENCES Product(product_id)
   );
/*
Creating Supplier
*/
DROP TABLE IF EXISTS Supplier;
CREATE TABLE IF NOT EXISTS Supplier	
   (  
	address		varchar(50) not null,
	email		varchar(50),
	phone		varchar(20),
	supplier_id 	int AUTO_INCREMENT,
	supplier_name	varchar(50) NOT NULL,
	primary key (supplier_id)
	
   );

/*
Creating Employee
*/
DROP TABLE IF EXISTS Employee;
CREATE TABLE IF NOT EXISTS Employee	
   (  
	email		varchar(50),
	password	varchar(50) not null,
	employee_type 	varchar(20),
	employee_id	int AUTO_INCREMENT not null,

region		varchar(50) NOT NULL,

	employee_name	varchar(50) NOT NULL,
	primary key (employee_id)
   );   

/*
Creating EmployeeAddressBook table
*/
DROP TABLE IF EXISTS EmployeeAddressBook;
CREATE TABLE IF NOT EXISTS EmployeeAddressBook	
   (  
	employee_id 	int not null,
	address		varchar(50),
	FOREIGN KEY(employee_id) REFERENCES Employee(employee_id)
   );
   
/*
Creating warehouse
*/
DROP TABLE IF EXISTS Warehouse;
CREATE TABLE IF NOT EXISTS Warehouse	
   (  
	region	 	varchar(50),
	warehouse_id	int NOT NULL,
	address		varchar(50) NOT NULL,
	manager_id	int,
	primary key (warehouse_id),
	FOREIGN KEY(manager_id) REFERENCES Employee(employee_id)
   );   


/*
Creating Inventory
*/
DROP TABLE IF EXISTS Inventory;
CREATE TABLE IF NOT EXISTS Inventory	
   (  
	inventory_line 	int AUTO_INCREMENT,
	cost		DECIMAL(6,2) NOT NULL,
	quantity	int NOT NULL,
	product_id	int,
	warehouse_id	int ,
	supplier_id	int,
	FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id),
	FOREIGN KEY (product_id) REFERENCES Product(product_id),
	FOREIGN KEY (warehouse_id) REFERENCES Warehouse(warehouse_id),
	primary key (inventory_line)
	
   );

/*
Creating Invoice
*/
DROP TABLE IF EXISTS Invoice;
CREATE TABLE IF NOT EXISTS Invoice	
   (  
	invoice_no 	int AUTO_INCREMENT,
	invoice_line	int NOT NULL,
	amount		DECIMAL(6,2) NOT NULL,
	product_id	int,
	supplier_id	int,
	quantity	int NOT NULL,
	FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id),
	FOREIGN KEY (product_id) REFERENCES Product(product_id),
	primary key (invoice_no)
	
   );
