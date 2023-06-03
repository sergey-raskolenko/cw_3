import os

import pytest


@pytest.fixture
def path_to_test_json():
	return os.path.join(os.path.dirname(__file__), "test_operations.json")


@pytest.fixture
def data_from_test_json():
	return [
		{
			"id": 441945886,
			"state": "EXECUTED",
			"date": "2019-08-26T10:50:58.294041",
			"operationAmount": {
				"amount": "31957.58",
				"currency": {
					"name": "руб.",
					"code": "RUB"
				}
			},
			"description": "Перевод организации",
			"from": "Maestro 1596837868705199",
			"to": "Счет 64686473678894779589"
		},
		{
			"id": 594226727,
			"state": "CANCELED",
			"date": "2018-09-12T21:27:25.241689",
			"operationAmount": {
				"amount": "67314.70",
				"currency": {
					"name": "руб.",
					"code": "RUB"
				}
			},
			"description": "Перевод организации",
			"from": "Visa Platinum 1246377376343588",
			"to": "Счет 14211924144426031657"
		},
		{
			"id": 518707726,
			"state": "EXECUTED",
			"date": "2018-11-29T07:18:23.941293",
			"operationAmount": {
				"amount": "3348.98",
				"currency": {
					"name": "USD",
					"code": "USD"
				}
			},
			"description": "Перевод с карты на карту",
			"from": "MasterCard 3152479541115065",
			"to": "Visa Gold 9447344650495960"
		},
		{
			"id": 172864002,
			"state": "EXECUTED",
			"date": "2018-12-28T23:10:35.459698",
			"operationAmount": {
				"amount": "49192.52",
				"currency": {
					"name": "USD",
					"code": "USD"
				}
			},
			"description": "Открытие вклада",
			"to": "Счет 96231448929365202391"
		}
	]


@pytest.fixture
def data_for_delete_empty_operation():
	return [
		{
			"id": 441945886,
			"state": "EXECUTED",
			"date": "2019-08-26T10:50:58.294041",
			"operationAmount": {
				"amount": "31957.58",
				"currency": {
					"name": "руб.",
					"code": "RUB"
				}
			},
			"description": "Перевод организации",
			"from": "Maestro 1596837868705199",
			"to": "Счет 64686473678894779589"
		},
		{}
	]


@pytest.fixture
def expected_result_for_delete_empty_operation():
	return [
		{
			"id": 441945886,
			"state": "EXECUTED",
			"date": "2019-08-26T10:50:58.294041",
			"operationAmount": {
				"amount": "31957.58",
				"currency": {
					"name": "руб.",
					"code": "RUB"
				}
			},
			"description": "Перевод организации",
			"from": "Maestro 1596837868705199",
			"to": "Счет 64686473678894779589"
		}
	]


@pytest.fixture
def sorted_by_date_data_from_test_json():
	return [
		{
			"id": 441945886,
			"state": "EXECUTED",
			"date": "2019-08-26T10:50:58.294041",
			"operationAmount": {
				"amount": "31957.58",
				"currency": {
					"name": "руб.",
					"code": "RUB"
				}
			},
			"description": "Перевод организации",
			"from": "Maestro 1596837868705199",
			"to": "Счет 64686473678894779589"
		},
		{
			"id": 172864002,
			"state": "EXECUTED",
			"date": "2018-12-28T23:10:35.459698",
			"operationAmount": {
				"amount": "49192.52",
				"currency": {
					"name": "USD",
					"code": "USD"
				}
			},
			"description": "Открытие вклада",
			"to": "Счет 96231448929365202391"
		},
		{
			"id": 518707726,
			"state": "EXECUTED",
			"date": "2018-11-29T07:18:23.941293",
			"operationAmount": {
				"amount": "3348.98",
				"currency": {
					"name": "USD",
					"code": "USD"
				}
			},
			"description": "Перевод с карты на карту",
			"from": "MasterCard 3152479541115065",
			"to": "Visa Gold 9447344650495960"
		},
		{
			"id": 594226727,
			"state": "CANCELED",
			"date": "2018-09-12T21:27:25.241689",
			"operationAmount": {
				"amount": "67314.70",
				"currency": {
					"name": "руб.",
					"code": "RUB"
				}
			},
			"description": "Перевод организации",
			"from": "Visa Platinum 1246377376343588",
			"to": "Счет 14211924144426031657"
		}
	]
