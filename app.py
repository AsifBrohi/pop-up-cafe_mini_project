import sys
sys.path.insert(0,'/Users/AsifB/Documents/Data_engineering_new_gen/pop_up_cafe_project/src')

import os


from dict_into import products_menu_file, courier_file, orders_menu_file
from inside_couriers import add_name, delete_name, open_courier, update_name
from inside_orders import (add_order, delete_order, open_order, update_order,
                           update_order_status)
from inside_product import add_item, delete_product, open_menu, update_item




def main_menu():
    cmd_main_menu_ = int(input("""
    Welcome to my Cafe, Please pick the options below
    ****MAIN MENU****
    0: Exit
    1: Product Menu
    2: Couriers
    3: Orders Menu
    >>>
    """ ))
    while True:
      if cmd_main_menu_ == 0: 
        products_menu_file()
        courier_file()
        orders_menu_file()
        exit()
        
      elif cmd_main_menu_== 1:
       
        product_menu()
        
      elif cmd_main_menu_== 2:
        
        courier_menu()
      elif cmd_main_menu_== 3:
       
        orders_menu()
      else:
        print("Not Valid Input, Please try again")
        main_menu()
      break

os.system("cls")       
def product_menu():
  cmd_product_menu = int(input("""
  ****PRODUCT MENU****
  0: Return To Main Menu
  1: Open Menu
  2: Add Item
  3: Update Item
  4: Delete Item
  >>>>
  """ ))
  while True:
    if cmd_product_menu == 0:
      os.system("cls")
      main_menu()
      
    elif cmd_product_menu == 1:
      os.system("cls")

      open_menu()
      main_menu()
    elif cmd_product_menu == 2:
      os.system("cls")
      add_item() #----> going back to product menu very quick without seeing item & price fix 
      added_item= input("""
      Would you like to continue adding items\nType y Or n
      >>>>
      """) 
      while added_item == "y":
        os.system('cls')
        product_menu()
      print("You have Gone back to Main Menu")
      main_menu()
    elif cmd_product_menu == 3:
      os.system("cls")
      update_item()
      updated_item =input("""
      Would you like to continue updating items\nType y Or n
      >>>>
      """)
      while updated_item == "y":
        os.system('cls')
        product_menu()
      print("You have Gone back to Main Menu")
      main_menu()
      
    elif cmd_product_menu == 4:
      os.system("cls")
      delete_product()
      deleted_item =input("""
      Would you like to continue deleting tems\nType y Or n
      >>>>
      """)
      while deleted_item == "y":
        os.system('cls')
        product_menu()
      print("You have Gone back to Main Menu")
      main_menu()
     
    else:
      print("Not Valid Input, Please try again")
      product_menu()
    break
  

def courier_menu():
  cmd_courier_menu = int(input("""
  ****COURIER****
  0: Return To Main Menu
  1: Show Courier List 
  2: Add Courier
  3: Update Courier 
  4: Delete Courier
  >>>>
  """))
  while True:
    if cmd_courier_menu == 0:
      os.system("cls")
      
      main_menu()
    elif cmd_courier_menu == 1:
     os.system("cls")
     
     open_courier()
     courier_menu()
    elif cmd_courier_menu == 2:
      os.system("cls")
      add_name()
      added_courier= input("""
      Would you like to continue adding Courier\nType y Or n
      >>>>
      """) 
      while added_courier == "y":
        os.system('cls')
        courier_menu()
      print("You have Gone back to Main Menu")
      main_menu()
    elif cmd_courier_menu == 3:
      os.system("cls")
      update_name()
      updated_name= input("""
      Would you like to continue updating Courier\nType y Or n
      >>>>
      """) 
      while updated_name == "y":
        os.system('cls')
        courier_menu()
      print("You have Gone back to Main Menu")
      main_menu()
      
    elif cmd_courier_menu == 4:
      os.system("cls")
      delete_name()
      deleted_courier= input("""
      Would you like to continue deleting Courier\nType y Or n
      >>>>
      """) 
      while deleted_courier == "y":
        os.system('cls')
        courier_menu()
      print("You have Gone back to Main Menu")
      main_menu()
    else:
      print("Not Valid Input, Please try again")
      product_menu()
    break    
    

def orders_menu():
  cmd_orders_menu = int(input("""
  ****ORDERS MENU****
  0: Return to Main Menu
  1: View Orders
  2: New Order
  3: Update Staus Of Order
  4: Update Order 
  5: Delete Order 
  >>>> 
  """))
  while True:
    if cmd_orders_menu == 0:
      os.system("cls")
      main_menu()
    elif cmd_orders_menu == 1:
      os.system("cls")
      open_order()
      orders_menu()
    elif cmd_orders_menu == 2:
      os.system("cls")
      add_order()
      added_order= input("""
      Would you like to continue adding new orders\nType y Or n
      >>>>
      """) 
      while added_order == "y":
        os.system('cls')
        orders_menu()
      print("You have Gone back to Main Menu")
      main_menu()
    elif cmd_orders_menu == 3:
      os.system("cls")
      update_order_status()
      updated_order_status= input("""
      Would you like to continue updating order status 
      \nType y Or n
      >>>>
      """) 
      while updated_order_status == "y":
        os.system('cls')
        orders_menu()
      print("You have Gone back to Main Menu")
      main_menu()
    elif cmd_orders_menu == 4:
      os.system("cls")
      update_order()
      updated_order= input("""
      Would you like to continue adding Courier\nType y Or n
      >>>>
      """) 
      while updated_order == "y":
        os.system('cls')
        orders_menu()
      print("You have Gone back to Main Menu")
      main_menu()
    elif cmd_orders_menu == 5:
      os.system("cls")
      delete_order()
      deleted_order= input("""
      Would you like to continue deleting Courier\nType y Or n
      >>>>
      """) 
      while deleted_order == "y":
        os.system('cls')
        orders_menu()
      print("You have Gone back to Main Menu")
      main_menu()
    
    else:
      print("Not Valid Input, Please try again")
      product_menu()
    
    break 



main_menu()
