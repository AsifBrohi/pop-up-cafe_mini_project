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

## How did you guarantee the project's requirements?
Every week there was additional requiremnets to meet and specs from the client.

Every week I updated the app with only the requirements and specs which were given to me from the client. 

Focused mainly on requirements first then refactored code. 

### Week 1 
Client has given me requirements which were 

create a product and add it to a list
view all products
STRETCH update or delete a product

Meeting requiremnts At Week1 created two functions main_menu & product_menu inside main_menu i did a while loop to get users to input an interger to navigate thorught the app seen below:

        while True:
            if command_ == 0:
        
            exit()
            elif command_ == 1:
            products_menu()




### Week 2:
Client has given me week 2 requirments which are shown below: 

As a user I want to:
create a product or courier and add it to a list
view all products or couriers
persist my data
I want to be able to update or delete a product or courier

Data should be persisted to a .txt file on a new line for each courier or product

Meeting the requirements of week 2 I created another function courier_menu and added that another elif statment into the main menu function seen below: 

        while True:
            if command_ == 0:
        
            exit()
            elif command_ == 1:
            products_menu()

            elif command == 2:
            courier_menu()
Then created two extra functions for data being peristed to a .txt file and added it when user exits app it saves the changes into a txt file. 


    def read_file():
      for product_ in product_list:
        product.write(product_+"\n")
      product.close()

    def read_courier_file():
      for courier_ in courier_list:
        courier.write(courier_+"\n")
      courier.close()

while True:
      if command_ == 0:
        read_file()
        read_courier_file()
        exit()

Also, created a orders_menu function and added that to mainmenu while loop seen below

    while True:
            if command_ == 0:
        
            exit()
            elif command_ == 1:
            products_menu()

            elif command == 2:
            courier_menu()

            elif command_ == 3:
            orders_menu()


## Week 3: 
Client has given week 3 requiremnts which are:

create a product, courier, or order and add it to a list
view all products, couriers, or orders
update the status of an order
persist my data (products and couriers)
STRETCH update or delete a product, order, or courier

During week 3 of the project I had a problem as the three functions  Product menu, Courier menu, Orders Menu needed to be broken down into indivdual functions seen below: 
   
   
         elif user_courier == 2:
            add_courier = input("ADD COURIER\n")
            courier_list.append(add_courier)
           
            added_courier= input("Continue Adding\ny/n\n")
            while added_courier == "y":
              courier_menu_option()
            print(courier_list)
            main_menu()

For example I changed the code above to this on a different py file
    
    
            def add_name():
                new_name= input("""
                Please Add Name
                >>>>
                """)
                courier_list.append(new_name)




## week 4
Client has given week 4 requirements 
• create a product, courier, or order dictionary and add it to a list
• view all products, couriers, or orders
• update the status of an order
• persist my data
• STRETCH update or delete a product, order, or courier
• BONUS list orders by status or courier

Now products couriers are dict so have to open with a csv file 

        def products_menu_file():
          with open('/Users/AsifB/Documents/Data_engineering_new_gen/pop_up_cafe_project/data/products.csv', w+', newline='') as output_file:
          dict_writer = csv.DictWriter(output_file, key_products)
          dict_writer.writeheader()
          dict_writer.writerows(products)


## Testing 

During testing I wanted to concetrate on the requirements from the client to see if they pass the test. For all my testing I used pytest mock method

Focusing on 
• create a product, courier, or order dictionary and add it to a list
for example seen below: 


            @patch("builtins.input", side_effect= ["coke",float(2.34)])
            def test_add_item(mock_input):
                inside_product.add_item()
                assert cafe_data.products[-1] == {"name":"coke","price":float(2.34)}
• view all products, couriers, or orders
for example seen below:


            @patch("builtins.print")
            def test_open_courier(mock_print):
                inside_couriers.open_courier()
                mock_print.assert_called_with({'name': 'Roger', 'phone': '07985746352'})
![image](https://user-images.githubusercontent.com/52333702/203526349-cb7b0708-582f-478c-b9ce-7d738828c441.png)


• update the status of an order
• persist my data
• STRETCH update or delete a product, order, or courier
• BONUS list orders by status or courier
## If you had more time, what is one thing you would improve upon?
One thing I would improve will be implementing class in my app. 

It will reduce the amount of code and make it easier to read for my collagues. 

Possibly use single respsonablity principle for example in my products menu: 





          class ProductMenu: 
            def open_menu(self):
              for view_products in cafe_data.products:
                print(view_products)
    

            def add_item(self):
                new_item = input("""
                Please Add Item
                >>>>
                """)
                add_price = float(input("""
                Please Add Item Price
                >>>>
                """))
                new_product = {}
                new_product["name"] = new_item
                new_product["price"] = add_price
    
    
                cafe_data.products.append(new_product)
    
                print(f"The item you added is {new_item}, £{add_price} ")
                for i in cafe_data.products:
                    print(i)


## What did you most enjoy implementing?
