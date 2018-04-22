HOST = "localhost"
USER = "root"
PASSWD = ""

#!/usr/bin/python

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
#21 Total
["Ramir@mail.com", "shipper", "Ramir", "ramirAddr"],
["Sophia@mail.com", "shipper", "Sophia", "sophiaAddr"],
["Aiden@mail.com", "shipper", "Aiden", "aidenAddr"],
["Emma@mail.com", "shipper", "Emma", "emmaAddr"],
["Lucas@mail.com", "shipper", "Lucas", "lucasAddr"],
["Olivia@mail.com", "shipper", "Olivia", "oliviaAddr"],
["Liam@mail.com", "shipper", "Liam", "liamAddr"],

["Rafael@mail.com", "packer", "Rafael", "rafaelAddr"],
["Mia@mail.com", "packer", "Mia", "miaAddr"],
["Noah@mail.com", "packer", "Noah", "noahAddr"],
["Riley@mail.com", "packer", "Riley", "rileyAddr"],
["Mason@mail.com", "packer", "Mason", "masonAddr"],
["Benjamin@mail.com", "packer", "Benjamin", "benjaminAddr"],
["Emily@mail.com", "packer", "Emily", "emilyAddr"],

["Trump@mail.com", "warehousemanager", "Trump", "trumpAddr"],
["Trujillo@mail.com", "warehousemanager", "Trujillo", "trujilloAddr"],
["Hector@mail.com", "warehousemanager", "Hector", "hectorAddr"],
["Mandela@mail.com", "warehousemanager", "Mandela", "mandelaAddr"],
["Messi@mail.com", "warehousemanager", "Messi", "messiAddr"],
["Irwin@mail.com", "warehousemanager", "Irwin", "irwinAddr"],
["Nick@mail.com", "warehousemanager", "Nick", "nickAddr"]
]

warehouseList = [
["warehouseAddr1"],
["warehouseAddr2"],
["warehouseAddr3"],
["warehouseAddr4"],
["warehouseAddr5"],
["warehouseAddr6"],
["warehouseAddr7"],
]

invoiceList = [
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

#One inventory per PRODUCT - cost and quantity -> these should be derived, hardcoded for now
inventoryList = [
["250.00", "100"],
["250.00", "100"],
["250.00", "100"],
["250.00", "100"],
["250.00", "100"],
["250.00", "100"],
["250.00", "100"],
["250.00", "100"],
["250.00", "100"],
["250.00", "100"],
["250.00", "100"],
["250.00", "100"]
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


#DATA ABOVE THIS LINE (also initialize password for database connect
#------------------------------------------------------
#INSERTING DATA INTO database object db with cursor


import MySQLdb
from sqlScriptReader import *
# Open database connection
db = MySQLdb.connect(host=HOST,user=USER,passwd=PASSWD,db="ecommerce")

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
	region.append(description)
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
	if x == 7:
		x = 0
	r = region[x-1]
	employee_id = x
	employee_name = row[2]

	cursor.execute('''INSERT into Employee (email, employee_type, region, employee_name) values (%s, %s, %s, %s)''', (email, employee_type, r, employee_name))
	db.commit()
	
	currentemployee.append(x)
	print(x)
	x += 1

print("INSERT into EMPLOYEEADDRESSBOOK")
currentemployeeaddressbook = []
x = 1
for row in employeeList:
	address = row[3]
	cursor.execute('''INSERT into EmployeeAddressBook (employee_id, address) values (%s, %s)''', (x, address))
	db.commit()

	currentemployeeaddressbook.append(x)
	print(x)
	x += 1

print("INSERT into WAREHOUSE")
currentwarehouse = []
x = 1	
for row in warehouseList:
	r = region[x-1]
	warehouse_id = x
	address = row[0]
	
	cursor.execute('''INSERT into Warehouse (region, warehouse_id, address, manager_id) values (%s, %s, %s, %s)''', (r, x, address, x+14))
	db.commit()
	currentwarehouse.append(x)
	print(x)
	x += 1
	
print("INSERT into INVENTORY")
currentinventory = []
x = 1	
for row in inventoryList:
	cost = row[0]
	quantity = row[1]
	_ids = str(x)
	
	cursor.execute('''INSERT into Inventory (cost, quantity) values (%s, %s)''', (cost, quantity))
	db.commit()
	currentinventory.append(x)
	print(x)
	x += 1
	
print("INSERT into INVOICE")
currentinvoice = []
x = 1
for row in invoiceList:
	invoice_line = str(x)
	
	cursor.execute('''INSERT into Invoice (invoice_line, amount, quantity) values (%s, %s, %s)''', (invoice_line, "0", "0"))
	db.commit()
	currentinvoice.append(x)
	print(x)
	x += 1
# disconnect from server
db.close()


