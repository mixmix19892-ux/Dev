# game.py

from gameparts import Board
# Из файла exceptions.py, который лежит в пакете gameparts,
# импортируется класс FieldIndexError
from gameparts.exceptions import FieldIndexError

def main():
    game = Board()
    game.display()
    # Пользователь вводит номер строки
    row = int(input('Введите номер строки: '))
    # Если введённое значение меньше нуля или больше или равно
    # field_size (это значение равно трём, оно хранится в модуле
    # parts.py)...
    if row < 0 or row >= game.field_size:
        # ...выбросить исключение FieldIndexError
        ...
        raise FieldIndexError('Введено значение за границами игрового поля!')
    column = int(input('Введите номер столбца: '))
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

if __name__ == '__main__':
    main()



# Создать игровое поле — объект класса Board
game = Board()
# Отрисовать поле в терминале
game.display()
# Разместить на поле символ по указанным координатам — сделать ход
game.make_move(1, 1, 'X')
print('Ход сделан!')
# Перерисовать поле с учётом сделанного хода
game.display()

