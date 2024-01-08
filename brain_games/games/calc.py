from random import randrange
from brain_games import engine


def exercise():
    print('What is the result of the expression?')


def main():
    z = randrange(20, 50)
    y = randrange(1, 20)
    massiv = [f'{z} - {y}', f'{z} + {y}', f'{z} * {y}']
    random_expression = massiv[randrange(0, 3)]
    result = eval(random_expression)
    engine.question(random_expression)
    engine.answer()
    if engine.ans == str(result):
        engine.correctly_answer()
        return True
    else:
        engine.wrong_answer(engine.ans, result)
        return False
