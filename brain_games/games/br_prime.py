#!/usr/bin/env python3
from random import randrange
from brain_games import engine


def main():
    print('What number is missing in the progression?')
    x = 0
    while x <= 3:
        y = randrange(1, 20)
        engine.question(y)
        engine.answer()
        if engine.prime(y) is True and engine.ans == 'yes' or engine.prime(y) is False and engine.ans == 'no':
            if x == 2:
                engine.congratulations()
                break
            else:
                engine.correct()
            x += 1
        elif engine.prime(y) is True and engine.ans != 'yes':
            engine.wrong_answer(engine.ans, 'yes')
            break
        elif engine.prime(y) is False and engine.ans != 'no':
            engine.wrong_answer(engine.ans, 'no')
            break


if __name__ == '__main__':
    main()
