# Импорт необходимых библиотек
from src.functions import main
import os

# Конструкция запуска основной функции, с переменной в виде абсолютного пути к json-файлу, и вывода ее данных
if __name__ == '__main__':
    filename = os.path.join(os.path.dirname(__file__), 'operations.json')
    print(*main(filename), sep="\n\n")
