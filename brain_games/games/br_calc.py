#!/usr/bin/env python3
from random import randrange
from brain_games import engine


def main():
    print('What is the result of the expression?')
    x = 0
    while x <= 3:
        z = randrange(20, 50)
        y = randrange(1, 20)
        massiv = [f'{z} - {y}', f'{z} + {y}', f'{z} * {y}']
        random_expression = massiv[randrange(0, 3)]
        result = eval(random_expression)
        engine.question(random_expression)
        engine.answer()
        if engine.ans == str(result):
            if x == 2:
                engine.congratulations()
                break
            else:
                engine.correct()
            x += 1
        elif engine.ans != str(result):
            engine.wrong_answer(engine.ans, result)
            break


if __name__ == '__main__':
    main()
