# pop-up-cafe_mini_project



## Project Background
Your client has launched a pop-up café in a busy business district. They
are offering home-made lunches and refreshments to the surrounding
offices. As such, they require a software application which helps them to
log and track orders

## Client requirements
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

Every week there was additional requiremnets to meet from the client on specs 
week 1 

As a user I want to:
create a product and add it to a list
view all products
STRETCH update or delete a product
Spec
A product should just be a string containing its name, i.e: "Coke Zero" A list of products should be a list of strings , i.e: ["Coke Zero"

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
}


## How did you guarantee the project's requirements?


## If you had more time, what is one thing you would improve upon?


## What did you most enjoy implementing?
