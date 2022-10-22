from math import sqrt


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Что-то."""
    if your_number <= 0:
        return

    print('Мы вычислили квадратный корень из введённого вами числа.'
          'Это будет: ', {calculate_square_root(your_number)})


print('Добро пожаловать в самую лучшую программу для'
      'вычисления квадратного корня из заданного числа')
calc(25.5)
