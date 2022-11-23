import sys
sys.path.insert(0,'/Users/AsifB/Documents/Data_engineering_new_gen/pop_up_cafe_project/src')
import inside_product,cafe_data
from unittest.mock import patch
from unittest import mock


"""
Testing for printing products list 

"""
@patch("builtins.print")
def test_open_menu(mock_print):
    inside_product.open_menu()
    mock_print.assert_called_with({'name': 'coffee', 'price': 1.4})

"""
Testing for adding new item into the product list 


"""
@patch("builtins.input", side_effect= ["coke",float(2.34)])
def test_add_item(mock_input):
    inside_product.add_item()
    assert cafe_data.products[-1] == {"name":"coke", "price":float(2.34)}

"""
Testing for updating existing items in product list 


"""
@patch("builtins.input", side_effect= ["0", "pasta",float(2.56)])
def test_update_item_option_0(mock_input):
    inside_product.update_item()
    assert cafe_data.products[0] == {"name":"pasta", "price":float(2.56)}

@patch("builtins.input", side_effect= ["1", "tuna",float(2.36)])
def test_update_item_option_1(mock_input):
    inside_product.update_item()
    assert cafe_data.products[1] == {"name":"tuna", "price":float(2.36)}

@patch("builtins.input", side_effect= ["2", "cherry",float(0.50)])
def test_update_item_option_2(mock_input):
    inside_product.update_item()
    assert cafe_data.products[2] == {"name":"cherry", "price":float(0.50)}

@patch("builtins.input", side_effect= ["3", "latte",float(2.60)])
def test_update_item_option_3(mock_input):
    inside_product.update_item()
    assert cafe_data.products[3] == {"name":"latte", "price":float(2.60)}



