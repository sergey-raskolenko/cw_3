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
	return data[:5]


def transform_date(operation: dict):
	date = operation['date'].split('T')[0]
	return datetime.strptime(date, '%Y-%m-%d').date().strftime('%d.%m.%Y')
