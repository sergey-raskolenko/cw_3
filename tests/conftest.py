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
def true_output_of_test_json():
	return [
		f'26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.',
		f'28.12.2018 Открытие вклада\n -> Счет **2391\n49192.52 USD',
		f'29.11.2018 Перевод с карты на карту\nMasterCard 3152 47** **** 5065 -> Visa Gold 9447 34** **** 5960\n3348.98 USD'
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


@pytest.fixture
def executed_data_from_test_json():
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
def test_operation():
	return {
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


@pytest.fixture
def true_test_operation_date():
	return "26.08.2019"


@pytest.fixture
def true_test_operation_address_from():
	return 'Maestro 1596 83** **** 5199'


@pytest.fixture
def true_test_operation_address_to():
	return 'Счет **9589'


@pytest.fixture
def true_test_operation_amount_and_currency():
	return '31957.58 руб.'


@pytest.fixture
def true_test_operation_output():
	return f'26.08.2019 Перевод организации\n'\
		f'Maestro 1596 83** **** 5199 -> Счет **9589\n'\
		f'31957.58 руб.'


@pytest.fixture
def test_operation_without_from_address():
	return {
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


@pytest.fixture
def true_from_address_of_operation_without_from_address():
	return ''
