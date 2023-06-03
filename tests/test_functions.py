from src.functions import *


def test_load_data_from_json(path_to_test_json, data_from_test_json):
	assert load_data_from_json(path_to_test_json) == data_from_test_json


def test_delete_empty_operation(data_for_delete_empty_operation, expected_result_for_delete_empty_operation):
	assert delete_empty_operation(data_for_delete_empty_operation) == expected_result_for_delete_empty_operation


def test_sort_data_by_date():
	pass


def test_get_executed_data():
	pass
