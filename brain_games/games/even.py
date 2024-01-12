from random import randint


def exercise():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def generate_question():
    num1 = randint(1, 20)
    if num1 % 2 == 0:
        return num1, 'yes'
    elif num1 % 2 != 0:
        return num1, 'no'
