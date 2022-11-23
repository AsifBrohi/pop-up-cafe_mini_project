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
Testing for updating order is shown  below
"""

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
