DROP DATABASE IF EXISTS ecommerce;
CREATE DATABASE IF NOT EXISTS  ecommerce;
USE ecommerce;

/*
Creating Customer table
*/
DROP TABLE IF EXISTS Customer;
CREATE TABLE IF NOT EXISTS Customer
   (  
	customer_id 	int AUTO_INCREMENT not null, 
	region 		varchar(20) not null,
	costomer_name 	varchar(50) not null,
	card_info	int,
	address		varchar(50) not null,
	email		varchar(50) not null,
	password	
	PRIMARY KEY (customer_id)
   );

/*
Creating CustomerAddressBook table
*/
DROP TABLE IF EXISTS CustomerAddressBook;
CREATE TABLE IF NOT EXISTS CustomerAddressBook	
   (  
	customer_id 	int not null,
	address		varchar(50),
	counter		int UNSIGNED NOT NULL default 0,
	FOREIGN KEY(customer_id) REFERENCES Customer(customer_id)
   );

DROP TABLE IF EXISTS Product;

/*
Creating Product table
*/
CREATE TABLE IF NOT EXISTS Product	
   (  
	product_id 	int AUTO_INCREMENT ,
	product_name	varchar(250)  ,
	packing_specs	varchar(50),
	units		varchar(50),
	description	varchar(250) ,
	price		DECIMAL(6,2) NOT null,
	status		varchar(10),
	quantity	int not null,
	primary key (product_id)
   );

/*
Creating Category table
*/
DROP TABLE IF EXISTS Category;
CREATE TABLE IF NOT EXISTS Category	
   (  
	product_id 	int not null,
	category	varchar(20),
	counter		int UNSIGNED NOT NULL default 0,
	FOREIGN KEY(product_id) REFERENCES Product(product_id)
   );

/*
Creating Cart
*/
DROP TABLE IF EXISTS Cart;
CREATE TABLE IF NOT EXISTS Cart	
   (  
	customer_id 	int,
	cart_line	int AUTO_INCREMENT ,
	product_id	int not null,
	quantity	int not null,
	FOREIGN KEY(customer_id) REFERENCES Customer(customer_id),
	FOREIGN KEY(product_id) REFERENCES Product(product_id),
	primary key (cart_line)
	
   );
/*
Creating Supplier
*/
DROP TABLE IF EXISTS Supplier;
CREATE TABLE IF NOT EXISTS Supplier	
   (  
	supplier_id 	int AUTO_INCREMENT,
	region		varchar(20) NOT NULL ,
	name		varchar(50) NOT NULL,
	address		varchar(50) not null,
	
	primary key (supplier_id)
	
   );

/*
Creating Employee
*/
DROP TABLE IF EXISTS Employee;
CREATE TABLE IF NOT EXISTS Employee	
   (  
	employee_type 	varchar(20)
	employee_id	int NOT NULL,
	region		varchar(50) NOT NULL,
	email		varchar(50),
	employee_name	int,
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
	region	 	varchar(50)
	warehouse_id	int NOT NULL,
	address		varchar(50) NOT NULL,
	manager_id	int,
	primary key (warehouse_id)
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


USE mysql;
SHOW databases;
USE ecommerce;
SHOW tables;
SHOW columns from Customer;
SHOW columns from Product;
SHOW columns from Cart;
