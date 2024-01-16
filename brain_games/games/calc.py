from random import randrange


exercise = 'What is the result of the expression?'


def result(num1, num2, random_expression):
    match random_expression:
        case '-':
            x = num1 - num2
        case '+':
            x = num1 + num2
        case '*':
            x = num1 * num2
    return x


def generate_question():
    num1 = randrange(20, 50)
    num2 = randrange(1, 20)
    massiv = ['-', '+', '*']
    random_expression = massiv[randrange(0, 3)]
    w = f'{num1} {random_expression} {num2}'
    ans = result(num1, num2, random_expression)
    return w, ans
