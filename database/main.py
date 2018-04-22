PASSWD = "D3f@ultP"

#!/usr/bin/python
cartList = [
]

categoryList = [
["chocolate milk dark white", "chocolates", "100"],
["bag handbag backpack totebag", "bags", "100"],
["pencil colored lead mechanical", "pencils", "100"],
["pen", "pens", "100"],
["toy", "toys", "100"],
["cpu", "cpus", "100"]
]

customerList = [
["addrLine1", "Alex", "password1", "Alex@mail.com"],
["addrLine2", "Bob", "password2", "Bob@mail.com"],
["addrLine3", "Catherine", "password3", "Catherine@mail.com"],
["addrLine4", "Dallas", "password4", "Dallas@mail.com"],
["addrLine5", "Edward", "password5", "Edward@mail.com"],
["addrLine6", "Fred", "password6", "Fred@mail.com"],
["addrLine7", "Greg", "password7", "Greg@mail.com"],
["addrLine8", "Hubert", "password8", "Hubert@mail.com"],
["addrLine9", "Isabella", "password9", "Isabella@mail.com"]
]
  
employeeList = [
#One Shipper Per Region
#One Warehouse Manager Per Region
#One Packer Per Region
[],
[],
]

employeeAddressBookList = [
[],
[]
]

inventoryList = [
[],
[]
]

invoiceList = [
[],
[]
]

productList = [
#Multi-attribute products
#Chocolate Products
["milk", "milkchocolate.png", "1.00", "Milk Chocolate", "100", "50", "5", "IN STOCK"],
["dark", "darkchocolate.png", "1.50", "Dark Chocolate", "100", "3", "5", "LOW STOCK"],
["white", "whitechocolate.png", "2.00", "White Chocolate", "100", "0", "5", "EMPTY"],
#Bag Products
["handbag", "handbag.png", "10.00", "Hand Bag", "100", "50", "5", "IN STOCK"],
["backpack", "backpack.png", "20.00", "Backpack", "100", "3", "5", "LOW STOCK"],
["totebag", "totebag.png", "5.00", "Tote Bag", "100", "0", "5", "EMPTY"],
#Pencil Products
["lead", "leadpencil.png", "0.25", "Lead Pencil", "100", "50", "5", "IN STOCK"],
["mechanical", "mechanicalpencil.png", "1.00", "Mechanical Pencil", "100", "3", "5", "LOW STOCK"],
["colored", "coloredpencil.png", "3.00", "Colored Pencil", "100", "0", "5", "EMPTY"],

#Single-attribute products
["pen", "pens.png", "2.00", "Pen", "100", "75", "5", "IN STOCK"],
["toy", "toy.png", "7.50", "Toy", "100", "2", "5", "LOW STOCK"],
["cpu", "cpu.png", "20.00", "Cpu", "100", "0", "5", "EMPTY"],
]

regionList = [
["1", "North America", "NA"],
["2", "South America", "SA"],
["3", "Asia", "AS"],
["4", "Africa", "AF"],
["5", "Europe", "EU"],
["6", "Australia", "AU"],
["7", "Antarctica", "AN"]
]

supplierList = [
["suppAddr1", "supp1@mail.com", "1234567", "Hershey Chocolate"],
["suppAddr2", "supp2@mail.com", "2345678", "Jansport"],
["suppAddr3", "supp3@mail.com", "3456789", "Ticonderoga"],
["suppAddr4", "supp4@mail.com", "4567890", "Papermate"],
["suppAddr5", "supp5@mail.com", "5678901", "Hasbro"],
["suppAddr6", "supp6@mail.com", "6789012", "Intel"],
]

warehouseList = [
[],
[]
]

import MySQLdb
from sqlScriptReader import *
# Open database connection
db = MySQLdb.connect(host="localhost",user="ramir",passwd=PASSWD,db="ecommerce")

print("Connected to database:")
#database cursor object intialized
cursor = db.cursor()

#Drop all tables and recreate entire database
#executeScriptsFromFile(cursor, 'definition.sql')

#SQL query to INSERT a record into the Table
#THANK GOD FOR THE AUTOINCREMENT STATEMENT IN SQL FOR THE ID
print('INSERT into CUSTOMER')
currentcustomer = []
x = 1
for row in customerList:
	address = row[0]
	customer_name = row[1]
	password = row[2]
	email = row[3]
	
	cursor.execute('''INSERT into Customer (address, customer_name, email, password) values (%s, %s, %s, %s)''', (address, customer_name, email, password))
	db.commit()
	print(x)
	currentcustomer.append(x)
	x += 1
	
print('INSERT into CUSTOMERADDRESSBOOK')
currentcustomeraddressbook = []
x = 1
for row in customerList:
	address = row[0]
	counter = 8000 + x
	cursor.execute('''INSERT into CustomerAddressBook (address, counter, customer_id) values (%s, %s, %s)''', (address, counter, x))
	db.commit()
	print(x)
	currentcustomeraddressbook.append(x)
	x += 1

print('INSERT into PRODUCT')
currentproduct = []
x = 1
for row in productList:
	description = row[0]
	image_link = row[1]
	price = row[2]
	product_name = row[3]
	quantity = row[4]
	units = row[5]
	refill_point = row[6]
	status = row[7]

	cursor.execute('''INSERT into Product (description, image_link, price, product_name, quantity, units, refill_point, status) values (%s, %s, %s, %s, %s, %s, %s, %s)''', (description, image_link, price, product_name, quantity, units, refill_point, status))
	db.commit()
	
	currentproduct.append(x)
	print(x)
	x += 1

print('INSERT into CATEGORY')
currentcategory = []
x = 1
for row in categoryList:
	attributes = row[0]
	category = row[1]
	counter = row[2]
	
	cursor.execute('''INSERT into Category (attributes, category, counter, product_id) values (%s, %s, %s, %s)''', (attributes, category, counter, x))
	db.commit()	
		
	currentcategory.append(x)
	print(x)
	x += 1

print('INSERT into REGION')
region = []
x = 1
for row in regionList:
	region_id = row[0]
	region_name = row[1]
	description = row[2]
	
	cursor.execute('''INSERT into Region (region_id, region_name, description) values (%s, %s, %s)''', (region_id, region_name, description))
	db.commit()
	region.append(x)
	print(x)
	x += 1
	
print("INSERT into CART")
# number of carts depends on number of customers
currentcart = []
x = 1
for row in customerList:
	customer_id = str(x)
	cursor.execute('''INSERT into Cart (customer_id, product_id, quantity) values (%s, product_id, 0)''', (customer_id))
	db.commit()
	
	currentcart.append(x)
	print(x)
	x += 1

print('INSERT into SUPPLIER')
currentsupplier = []
x = 1
for row in supplierList:
	address = row[0]
	email = row[1]
	phone = row[2]
	supplier_name = row[3]
	
	cursor.execute('''INSERT into Supplier (address, email, phone, supplier_name) values (%s, %s, %s, %s)''', (address, email, phone, supplier_name))
	db.commit()
	
	currentsupplier.append(x)
	print(x)
	x += 1

print("INSERT into EMPLOYEE")
currentemployee = []
x = 1
for row in employeeList:
	email = row[0]
	employee_type = row[1]
	employee_id = row[2]
	employee_name = row[3]

	cursor.execute('''INSERT into Employee () values ()''', (address, customer_name, email, password))
	db.commit()
	
	currentemployee.append(x)
	print(x)
	x += 1

print("INSERT into EMPLOYEE")
currentemployee = []
x = 1
for row in employeeAddressBookList:
	print('INSERT into EMPLOYEEADDRESSBOOK')
	address = row[0]
	customer_name = row[1]
	password = row[2]
	email = row[3]
	
	cursor.execute('''INSERT into Customer (address, customer_name, email, password) values (%s, %s, %s, %s)''', (address, customer_name, email, password))
	db.commit()

print("INSERT into EMPLOYEE")
currentemployee = []
x = 1	
for row in inventoryList:
	print('INSERT into INVENTORY')
	address = row[0]
	customer_name = row[1]
	password = row[2]
	email = row[3]
	
	cursor.execute('''INSERT into Customer (address, customer_name, email, password) values (%s, %s, %s, %s)''', (address, customer_name, email, password))
	db.commit()

print("INSERT into EMPLOYEE")
currentemployee = []
x = 1	
for row in invoiceList:
	print('INSERT into INVOICELIST')
	address = row[0]
	customer_name = row[1]
	password = row[2]
	email = row[3]
	
	cursor.execute('''INSERT into Customer (address, customer_name, email, password) values (%s, %s, %s, %s)''', (address, customer_name, email, password))
	db.commit()

print("INSERT into EMPLOYEE")
currentemployee = []
x = 1
for row in warehouseList:
	print('INSERT into WAREHOUSE')
	address = row[0]
	customer_name = row[1]
	password = row[2]
	email = row[3]
	
	cursor.execute('''INSERT into Customer (address, customer_name, email, password) values (%s, %s, %s, %s)''', (address, customer_name, email, password))
	db.commit()
# disconnect from server
db.close()


