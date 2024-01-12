from random import randrange


def exercise():
    print('What is the result of the expression?')


def generate_question():
    num1 = randrange(20, 50)
    num2 = randrange(1, 20)
    massiv = ['-', '+', '*']
    random_expression = massiv[randrange(0, 3)]
    w = f'{num1} {random_expression} {num2}'
    match random_expression:
        case '-':
            x = num1 - num2
            return w, x
        case '+':
            x = num1 + num2
            return w, x
        case '*':
            x = num1 * num2
            return w, x
