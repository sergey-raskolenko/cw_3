from src.functions import main
import os

if __name__ == '__main__':
    filename = os.path.join(os.path.dirname(__file__), 'operations.json')
    print(*main(filename), sep="\n\n")
