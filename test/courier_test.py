import sys
sys.path.insert(0,'/Users/AsifB/Documents/Data_engineering_new_gen/pop_up_cafe_project/src')
import inside_couriers, cafe_data
from unittest.mock import patch
from unittest import mock

"""
Testing for printing courier list 

"""
@patch("builtins.print")
def test_open_courier(mock_print):
    inside_couriers.open_courier()
    mock_print.assert_called_with({'name': 'Roger', 'phone': '07985746352'})


"""
Testing for adding new courier into the courier dictionary list 


"""



@patch("builtins.input", side_effect = ["Aidan", "07986465723"])
def test_add_name(mock_input):
    inside_couriers.add_name()
    assert cafe_data.courier_dict[-1] == {"name":"Aidan","phone":"07986465723"}

"""
Testing for updating existing courier in courier dictionary list 


"""


@patch("builtins.input", side_effect = ["0","Aidan", "07986465723"])
def test_update_name_option_0(mock_input):
    inside_couriers.update_name()
    assert cafe_data.courier_dict[0] == {"name":"Aidan","phone":"07986465723"}

@patch("builtins.input", side_effect = ["1","Nicky", "079324354353"])
def test_update_name_option_1(mock_input):
    inside_couriers.update_name()
    assert cafe_data.courier_dict[1] == {"name":"Nicky","phone": "079324354353"}

@patch("builtins.input", side_effect = ["2","George", "079838485867"])
def test_update_name_option_2(mock_input):
    inside_couriers.update_name()
    assert cafe_data.courier_dict[2] == {"name":"George","phone":"079838485867"}

@patch("builtins.input", side_effect = ["3","Chelsea", "07834543234"])
def test_update_name_option_3(mock_input):
    inside_couriers.update_name()
    assert cafe_data.courier_dict[3] == {"name":"Chelsea","phone":"07834543234"}

@patch("builtins.input", side_effect = ["4","Bella", "07836452621"])
def test_update_name_option_4(mock_input):
    inside_couriers.update_name()
    assert cafe_data.courier_dict[4] == {"name":"Bella","phone":"07836452621"}

