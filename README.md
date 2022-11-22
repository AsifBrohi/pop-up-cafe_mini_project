# pop-up-cafe_mini_project



## Project Background
My client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding offices. As such, they require a software application which helps them to log and track orders

## Client requirements
The client has given me these requirements for the app. 

• I want to maintain a collection of products and couriers.
• When a customer makes a new order, I need to create this on the
system.
• I need to be able to update the status of an order i.e: preparing,
out-for-delivery, delivered.
• When I exit my app, I need all data to be persisted and not lost.
• When I start my app, I need to load all persisted data.
• I need to be sure my app has been tested and proven to work well.
• I need to receive regular software updates


## How did your design go about meeting the project's requirements?

My design meeting the projects requirment was first to create a list of products and creating a main menu function seen below 


def main_menu():

    print("Welcome to my Cafe, Please pick the options below")

    print("***MAIN MENU***")
    command_ = int(input("0===>EXIT\n1===>PRODUCT MENU\n:"))
    while True:
      if command_ == 0:
        
        exit()
      elif command_ == 1:
        products_menu()
     

I got user to input an interger either to exit the app or to go to the products menu. 
This was the structure of my app. 

## Solutoin core 

## How did you guarantee the project's requirements?
Every week there was additional requiremnets to meet and specs from the client on specs 

Every week I updated the app with only the requirements and specs which were given to me from the client. 

### week 1 
Client has given me requirements which were 

create a product and add it to a list
view all products
STRETCH update or delete a product

At the start I just created a Main Menu function which had users input an integer to either exit the app or go to the products page. I implemented a while loop which had If statements for the users input. 

week 2:
As a user I want to:
create a product or courier and add it to a list
view all products or couriers
persist my data
STRETCH I want to be able to update or delete a product or courier
Spec
A product should just be a string containing its name, i.e: "Coke Zero"
A list of products should be a list of strings , i.e: ["Coke Zero"]
A courier should just be a string containing its name, i.e: "John"
A list of couriers should be a list of strings , i.e: ["John"]
Data should be persisted to a .txt file on a new line for each courier or product , ie:

As a user I want to:
create a product or order and add it to a list
view all products or orders
STRETCH I want to be able to update or delete a product or order
Spec
A product should just be a string containing its name, i.e: "Coke Zero"
A list of products should be a list of strings, i.e: ["Coke Zero"]
An order should be a dict, i.e:

week 3: 
As a user I want to:
create a product, courier, or order and add it to a list
view all products, couriers, or orders
update the status of an order
persist my data (products and couriers)
STRETCH update or delete a product, order, or courier
Spec
A product should just be a string containing its name, i.e: "Coke Zero"
A list of products should be a list of strings, i.e: ["Coke Zero"]
A courier should just be a string containing its name, i.e: "John"
A list of couriers should be a list of strings, i.e: ["John"]
An order should be a dict, i.e:

Created a Main Menu function 
As a user I want to:
create a product, courier, or order and add it to a list
view all products, couriers, or orders
update the status of an order
persist my data (products and couriers)
STRETCH update or delete a product, order, or courier
Spec
A product should just be a string containing its name, i.e: "Coke Zero"
A list of products should be a list of strings, i.e: ["Coke Zero"]
A courier should just be a string containing its name, i.e: "John"
A list of couriers should be a list of strings, i.e: ["John"]
An order should be a dict, i.e:

As a user I want to:
• create a product, courier, or order dictionary and add it to a list
• view all products, couriers, or orders
• update the status of an order
• persist my data
• STRETCH update or delete a product, order, or courier
• BONUS list orders by status or courier
Spec
• A product should be a dict, i.e:
{
"name": "Coke Zero",
"price": 0.8 // Float
}
• A courier should be a dict, i.e:
{
"name": "Bob",
"phone": "0789887889"
}
• An order should be a dict, i.e:
{
"customer_name": "John",
"customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"customer_phone": "0789887334",
"courier": 2, // Courier index
"status": "preparing",
"items": "1, 3, 4" // Product index


## If you had more time, what is one thing you would improve upon?


## What did you most enjoy implementing?

test -- guarenteed how it works 

what would i change --> class 

enjoy 