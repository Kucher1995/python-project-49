from random import randrange
from brain_games import engine
from math import gcd


def main():
    print('Find the greatest common divisor of given numbers.')
    x = 0
    while x < 3:
        z = randrange(20, 50)
        y = randrange(1, 20)
        engine.question(f'{z} {y}')
        engine.answer()
        if engine.ans == str(gcd(z, y)):
            engine.correct()
            x += 1
        else:
            engine.wrong_answer(engine.ans, gcd(z, y))
            break
    else:
        engine.congratulations()
