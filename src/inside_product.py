import cafe_data

def open_menu():
    for view_products in cafe_data.products:
        print(view_products)
    

def add_item():
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
   
    #sort this out make it flow better , user friendly 
  
def update_item():
    for product_index , value in enumerate(cafe_data.products):
        print(product_index, value)
    update_product = input("""
    Please use the index to pick a product to update
    >>>>
    """)
    if update_product:
        new_name = input("New product name? ")
        new_price = float(input("New Price?"))
        cafe_data.products[int(update_product)]["name"] = new_name
        cafe_data.products[int(update_product)]["price"] = new_price
    for product in cafe_data.products:
        print(product)
    
def delete_product():
    for product_index , value in enumerate(cafe_data.products):
        print(product_index, value)
    product_delete = input("""
    Please use the index to pick a product to delete
    >>>>
    """)
    if product_delete:
        del cafe_data.products[int(product_delete)]
    for product in cafe_data.products:
        print(product)
        
