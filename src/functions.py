import json
from datetime import datetime


def load_data_from_json(filename) -> list[dict]:
	"""
	Считывает информация с json-файла и возвращает ее
	:return: Список данных
	"""
	with open(filename, 'r', encoding='utf-8') as f:
		data = json.load(f)
	return data


def delete_empty_operation(operations_list: list[dict]) -> list[dict]:
	"""
	Удаляет пустые записи об операциях из данных
	:return: Список с заполненными данными
	"""
	return [operation for operation in operations_list if operation != {}]


def sort_data_by_date(data: list[dict]) -> list[dict]:
	"""
	Сортирует данные в списке словарей по дате
	:return: Отсортированный список словарей
	"""
	new_data = sorted(data, key=lambda item: item.get('date'), reverse=True)
	return new_data


def get_executed_data(data: list[dict]) -> list[dict]:
	"""
	Сортирует данные в списке по статусу операции
	:return: Отсортированный список словарей
	"""
	return [item for item in data if item['state'] == 'EXECUTED']


def list_of_5_or_less_operations(data: list[dict]) -> list[dict]:
	"""
	Из списка всех выполненных операций возвращает последние 5 или меньше
	:param data: Список всех операций со статусом EXECUTED
	:return: Список длиной в 5 или меньше элементов
	"""
	return data[:5]


def transform_date(operation: dict) -> str:
	"""
	Трансформирует дату к виду '%d.%m.%Y'
	:param operation: словарь операции
	:return: строка с верной датой
	"""
	date = operation['date'].split('T')[0]
	return datetime.strptime(date, '%Y-%m-%d').date().strftime('%d.%m.%Y')


def mask_address(operation_address: str) -> str:
	"""
	Получает информацию об адресе, маскирует ее согласно требованиям
	:param operation_address: Адрес операции
	:return: Замаскированный адрес
	"""
	operation_address = operation_address.split()
	if len(operation_address) == 0:
		return ''
	else:
		if operation_address[-1].isdigit():
			if len(operation_address[-1]) == 16:
				return f'{" ".join(operation_address[:-1])} {operation_address[-1][:4]} ' \
					f'{operation_address[-1][4:6]}** **** {operation_address[-1][-4:]}'
			elif len(operation_address[-1]) == 20:
				return f'{" ".join(operation_address[:-1])} **{operation_address[-1][-4:]}'


def get_address_from(operation: dict) -> str:
	"""
	Возвращает замаскированный адрес операции по ключу 'from'
	:param operation: Словарь операции
	:return: Замаскированный адрес 'from'
	"""
	if 'from' not in operation:
		return ''
	else:
		return mask_address(operation['from'])


def get_address_to(operation: dict) -> str:
	"""
	Возвращает замаскированный адрес операции по ключу 'to'
	:param operation: Словарь операции
	:return: Замаскированный адрес 'to'
	"""
	return mask_address(operation['to'])


def get_amount_and_currency(operation: dict) -> str:
	"""
	Выводит сумму и валюту операции
	:param operation: Словарь операции
	:return: сумма + валюта
	"""
	return f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"


def true_operation_output(operation: dict) -> str:
	"""
	Необходимый вывод всей информации об операции
	:param operation: Словарь операции
	:return: строка с информацией
	"""
	return f"{transform_date(operation)} {operation['description']}\n" \
		f"{get_address_from(operation)} -> {get_address_to(operation)}\n" \
		f"{get_amount_and_currency(operation)}"


def main(filename) -> list:
	"""
	Возвращает список строк из 5 последних выполненных клиентом операций:
	:param filename: Абсолютный путь к json-файлу
	:return: Список строк последних опер
	"""
	data = load_data_from_json(filename)
	data = delete_empty_operation(data)
	data = sort_data_by_date(data)
	data = get_executed_data(data)
	data = list_of_5_or_less_operations(data)
	output_data = []
	for operation in data:
		output_data.append(true_operation_output(operation))
	return output_data
