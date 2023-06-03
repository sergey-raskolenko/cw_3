import pytest

from src.functions import *


def test_load_data_from_json(path_to_test_json, data_from_test_json):
	assert load_data_from_json(path_to_test_json) == data_from_test_json


def test_delete_empty_operation(data_for_delete_empty_operation, expected_result_for_delete_empty_operation):
	assert delete_empty_operation(data_for_delete_empty_operation) == expected_result_for_delete_empty_operation


def test_sort_data_by_date(data_from_test_json, sorted_by_date_data_from_test_json):
	assert sort_data_by_date(data_from_test_json) == sorted_by_date_data_from_test_json


def test_get_executed_data(data_from_test_json, executed_data_from_test_json):
	assert get_executed_data(data_from_test_json) == executed_data_from_test_json


@pytest.mark.parametrize("list_of_dict, expected", [
	([{}, {}, {}, {}, {}, {}], [{}, {}, {}, {}, {}]),
	([{}, {}, {}], [{}, {}, {}])
])
def test_list_of_5_or_less_operations(list_of_dict, expected):
	assert list_of_5_or_less_operations(list_of_dict) == expected


def test_transform_date(test_operation, true_operation_date):
	assert transform_date(test_operation) == true_operation_date


@pytest.mark.parametrize("operation_address, expected", [
	('', ''),
	('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
	('Счет 64686473678894779589', 'Счет **9589'),
	('Visa Platinum 1246377376343588', 'Visa Platinum 1246 37** **** 3588'),
])
def test_mask_address(operation_address, expected):
	assert mask_address(operation_address) == expected
