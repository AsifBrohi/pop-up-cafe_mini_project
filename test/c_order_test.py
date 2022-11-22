import sys 
sys.path.insert(0,'/Users/AsifB/Documents/Data_engineering_new_gen/pop_up_cafe_project/src')
import inside_orders, cafe_data



from unittest.mock import patch
from unittest import mock

import inside_orders
"""
Testing for adding new order is shown below 

"""
@patch("builtins.input", side_effect = [
    "Aidan", 
    "Unit 34, 400 Main Street, LONDON, W7 2ER",
    "07908675645",
    1, 
    '1,2,3'])
def test_add_order(mock_input):
    inside_orders.add_order()
    assert cafe_data.orders[-1] == {"customer_name": "Aidan", 
    "customer_address": "Unit 34, 400 Main Street, LONDON, W7 2ER",
    "customer_phone":"07908675645",
    "courier": 1, 
    "status": "preparing",
    "items":"1,2,3"}




"""
Testing for updating status of order shown below 
"""

@patch("builtins.input", side_effect =["0","0"])
def test_update_order_status_option0(mock_input):
    inside_orders.update_order_status()
    assert cafe_data.orders[0] == {"customer_name": "John", 
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone":"07908675645",
    "courier": 1, 
    "status": "done",
    "items":"1,2,3"}

@patch("builtins.input", side_effect =["0","1"])
def test_update_order_status_option0_1(mock_input):
    inside_orders.update_order_status()
    assert cafe_data.orders[0] == {"customer_name": "John", 
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone":"07908675645",
    "courier": 1, 
    "status": "cancelled",
    "items":"1,2,3"}

@patch("builtins.input", side_effect =["0","2"])
def test_update_order_status_option0_2(mock_input):
    inside_orders.update_order_status()
    assert cafe_data.orders[0] == {"customer_name": "John", 
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone":"07908675645",
    "courier": 1, 
    "status":"out for delivery",
    "items":"1,2,3"}

@patch("builtins.input", side_effect =["0","3"])
def test_update_order_status_option0_3(mock_input):
    inside_orders.update_order_status()
    assert cafe_data.orders[0] == {"customer_name": "John", 
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone":"07908675645",
    "courier": 1, 
    "status":"delivered",
    "items":"1,2,3"}



@patch("builtins.input", side_effect =["1","0"])
def test_update_order_status_option1(mock_input):
    inside_orders.update_order_status()
    assert cafe_data.orders[1] == { "customer_name": "Yasmine", 
    "customer_address": "Unit 4, 22 Main Street, LONDON, WH1 2ER",
    "customer_phone":"07987564536",
    "courier": 2, 
    "status": "done",
    "items":"1,2,3"}

@patch("builtins.input", side_effect =["1","1"])
def test_update_order_status_option1_1(mock_input):
    inside_orders.update_order_status()
    assert cafe_data.orders[1] == { "customer_name": "Yasmine", 
    "customer_address": "Unit 4, 22 Main Street, LONDON, WH1 2ER",
    "customer_phone":"07987564536",
    "courier": 2, 
    "status": "cancelled",
    "items":"1,2,3"}

@patch("builtins.input", side_effect =["1","2"])
def test_update_order_status_option1_2(mock_input):
    inside_orders.update_order_status()
    assert cafe_data.orders[1] == { "customer_name": "Yasmine", 
    "customer_address": "Unit 4, 22 Main Street, LONDON, WH1 2ER",
    "customer_phone":"07987564536",
    "courier": 2, 
    "status": "out for delivery",
    "items":"1,2,3"}

@patch("builtins.input", side_effect =["1","3"])
def test_update_order_status_option1_3(mock_input):
    inside_orders.update_order_status()
    assert cafe_data.orders[1] == { "customer_name": "Yasmine", 
    "customer_address": "Unit 4, 22 Main Street, LONDON, WH1 2ER",
    "customer_phone":"07987564536",
    "courier": 2, 
    "status": "delivered",
    "items":"1,2,3"}

"""
Testing for updating order is shown  below
"""
@patch("builtins.input", side_effect = [
    "0",
    "Aidan", 
    "Unit 34, 400 Main Street, LONDON, W7 2ER",
    "07908675645",
     1,
    "0",
    '2,3,4'])
def test_update_order_option0(mock_input):
    inside_orders.update_order()
    assert cafe_data.orders[0]== {
    "customer_name":"Aidan", 
    "customer_address":"Unit 34, 400 Main Street, LONDON, W7 2ER",
    "customer_phone":"07908675645",
    "courier": 1,
    "status":"done",
    "items":"2,3,4"}

@patch("builtins.input", side_effect = [
    "1",
    "Romeo", 
    "Unit 34, 460 Main Street, LONDON, W7 WZR",
    "0765767657657",
     2,
    "3",
    '3,3,4'])
def test_update_order_option1(mock_input):
    inside_orders.update_order()
    assert cafe_data.orders[1]== {
    "customer_name":"Romeo", 
    "customer_address":"Unit 34, 460 Main Street, LONDON, W7 WZR",
    "customer_phone":"0765767657657",
    "courier": 2,
    "status":"delivered",
    "items":"3,3,4"}
