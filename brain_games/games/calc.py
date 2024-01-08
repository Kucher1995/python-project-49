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
    engine.question(x)
    engine.answer()
    match random_expression:
        case '-':
            if z - y == int(engine.ans):
                engine.correct_answer()
                return True
            else:
                engine.wrong_answer(engine.ans, (z - y))
                return False
        case '+':
            if z + y == int(engine.ans):
                engine.correct_answer()
                return True
            else:
                engine.wrong_answer(engine.ans, (z + y))
                return False
        case '*':
            if z * y == int(engine.ans):
                engine.correct_answer()
                return True
            else:
                engine.wrong_answer(engine.ans, (z * y))
                return False
    return
