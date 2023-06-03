from src.functions import *


def test_load_data_from_json(path_to_test_json, data_from_test_json):
	assert load_data_from_json(path_to_test_json) == data_from_test_json


def test_delete_empty_operation(data_for_delete_empty_operation, expected_result_for_delete_empty_operation):
	assert delete_empty_operation(data_for_delete_empty_operation) == expected_result_for_delete_empty_operation


def test_sort_data_by_date(data_from_test_json, sorted_by_date_data_from_test_json):
	assert sort_data_by_date(data_from_test_json) == sorted_by_date_data_from_test_json


def test_get_executed_data(data_from_test_json, executed_data_from_test_json):
	assert get_executed_data(data_from_test_json) == executed_data_from_test_json


def test_list_of_5_or_less_operations():
	assert list_of_5_or_less_operations([{}, {}, {}, {}, {}, {}]) == [{}, {}, {}, {}, {}]
	assert list_of_5_or_less_operations([{}, {}, {}]) == [{}, {}, {}]

