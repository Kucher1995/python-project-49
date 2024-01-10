from random import randrange


def exercise():
    print('What is the result of the expression?')


def question():
    num1 = randrange(20, 50)
    num2 = randrange(1, 20)
    massiv = ['-', '+', '*']
    random_expression = massiv[randrange(0, 3)]
    w = f'{num1} {random_expression} {num2}'
    return w, random_expression, num1, num2


def main(ans, random_expression, z, y):
    match random_expression:
        case '-':
            if z - y == int(ans):
                return True, ans
            else:
                x = z - y
                return False, x
        case '+':
            if z + y == int(ans):
                return True, ans
            else:
                x = z + y
                return False, x
        case '*':
            if z * y == int(ans):
                return True, ans
            else:
                x = z * y
                return False, x
