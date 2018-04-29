#!/usr/bin/python
class Customer(object):
    cusCount=1

    def __init__(self,address=    "address", customer_name=  "customer" , email= "cus", password = "password"):  

        address="address" + str(Customer.cusCount) if address=="address" else address
        
        self.customer_name= "customer" + str(Customer.cusCount) if customer_name=="customer" else customer_name		
        self.customer_id=Customer.cusCount
        self.email=         "cus" + str(Customer.cusCount)+ "@email.com" if email=="cus" else email		
        self.password=      "password" + str(Customer.cusCount) if password=="password" else password	
        self.address=address
        self.addressBook=[]
        self.addressBook.append(CustomerAddressBook(self.customer_id,address))
        
        Customer.cusCount+=1
    def __str__(self):
        return (self.address+'", "'+ self.customer_name+'", '+str(self.customer_id)+', "'+self.email+'", "'+self.password)        

class   CustomerAddressBook(object):
    def __init__(self,id,address,counter=0):
        self.id=id
        self.counter=counter
        self.address=address
        print("address Book entry added:",self.id,self.counter,self.address)

class   Cart(object):
    def __init__(self,id,address,counter=0):
        self.id=id
        self.counter=counter
        self.address=address
        print("address Book entry added:",self.id,self.counter,self.address)

    def addEntry(self,id,address,counter=0):
        

#CREATE TABLE IF NOT EXISTS Product	
#   (
#	description	varchar(250),
#	image_link	varchar(250),
#	price		DECIMAL(6,2) NOT null,
#	product_id 	int AUTO_INCREMENT ,
#	product_name	varchar(250) ,
#	quantity	int not null,	
#	units		varchar(50),
#	refill_point	varchar(50),
#	status		varchar(10),
#	primary key (product_id)
#  );

lstCustomers=[]
for x in range(10):
    lstCustomers.append(Customer())
for cs in lstCustomers:
    print(cs)




