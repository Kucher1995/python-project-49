from random import randrange
from brain_games import engine


def exercise():
    print('What is the result of the expression?')


def main():
    z = randrange(20, 50)
    y = randrange(1, 20)
    massiv = ['-', '+', '*']
    random_expression = massiv[randrange(0, 3)]
    x = f'{z} {random_expression} {y}'
    ans = engine.question_answer(x)
    match random_expression:
        case '-':
            if z - y == int(ans):
                engine.correct_answer()
                return True
            else:
                engine.wrong_answer(ans, (z - y))
                return False
        case '+':
            if z + y == int(ans):
                engine.correct_answer()
                return True
            else:
                engine.wrong_answer(ans, (z + y))
                return False
        case '*':
            if z * y == int(ans):
                engine.correct_answer()
                return True
            else:
                engine.wrong_answer(ans, (z * y))
                return False
    return
