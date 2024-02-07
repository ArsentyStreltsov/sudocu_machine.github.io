from flask import Flask, request, jsonify, send_from_directory
import numpy as np
from sudoku import solve_sudoku, check_sudoku_solution  # Убедитесь, что функция импортирована из правильного места



app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return send_from_directory('.', 'templates/index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json['board']
    board = np.array(data)  # Преобразование входных данных в массив NumPy
    solved_board = solve_sudoku(board)  # Прямой вызов с массивом NumPy

    if isinstance(solved_board, np.ndarray):  # Проверка, что возвращается массив NumPy
        return jsonify({'board': solved_board.tolist()})  # Преобразование в список для JSON
    else:
        return jsonify({'error': 'Нет решения'}), 400


@app.route('/check', methods=['POST'])
def check():
    data = request.json['board']
    board = np.array(data)  # Преобразование входных данных в массив NumPy
    if check_sudoku_solution(board):  # Функция для проверки решения
        return jsonify({'valid': True})
    else:
        return jsonify({'valid': False})


if __name__ == '__main__':
    app.run(debug=True)