import sys

sys.path.insert(0,'/Users/AsifB/Documents/Data_engineering_new_gen/pop_up_cafe_project/src')

import inside_product,inside_couriers,inside_orders,cafe_data
from unittest.mock import patch
from unittest import mock


@patch("builtins.input", side_effect= ["0", cafe_data.products.pop(0)])
def test_delete_item_option_0(mock_input):
    inside_product.delete_product()
    assert cafe_data.products[0] != {"name": "sandwich", "price": float(2.44)}

@patch("builtins.input", side_effect= ["1", cafe_data.products.pop(0)])
def test_delete_item_option_1(mock_input):
    inside_product.delete_product()
    assert cafe_data.products[0] != {"name": "crisp", "price":float(0.45)}

"""
Testing for deleting courier is shown below 
"""

@patch("builtins.input", side_effect= ["0", cafe_data.courier_dict.pop(0)])
def test_delete_courier_option_0(mock_input):
    inside_couriers.delete_name()
    assert cafe_data.courier_dict[0] != {"name": "Charlie", "phone": "07907563746"}



@patch("builtins.input", side_effect = ["0", cafe_data.orders.pop(0)])
def test_delete_order_option_0(mock_input):
    inside_orders.delete_order()
    assert cafe_data.orders!= {
    "customer_name": "John", 
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone":"07908675645",
    "courier": 1, 
    "status": "preparing",
    "items":"1,2,3"}
