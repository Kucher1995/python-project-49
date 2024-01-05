#!/usr/bin/env python3
from random import randrange
from brain_games import engine
from math import gcd


def main():
    print('What is the result of the expression?')
    x = 0
    while x <= 3:
        z = randrange(20, 50)
        y = randrange(1, 20)
        engine.question(f'{z} {y}')
        engine.answer()
        if engine.ans == str(gcd(z, y)):
            if x == 2:
                engine.congratulations()
                break
            else:
                engine.correct()
            x += 1
        elif engine.ans != str(gcd(z, y)):
            engine.wrong_answer(engine.ans, gcd(z, y))
            break


if __name__ == '__main__':
    main()
