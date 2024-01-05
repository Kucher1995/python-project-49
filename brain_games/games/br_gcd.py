from random import randrange
from brain_games import eng
from math import gcd


def main():
    print('Find the greatest common divisor of given numbers.')
    x = 0
    while x <= 3:
        z = randrange(20, 50)
        y = randrange(1, 20)
        eng.question(f'{z} {y}')
        eng.answer()
        if eng.ans == str(gcd(z, y)):
            if x == 2:
                eng.congratulations()
                break
            else:
                eng.correct()
            x += 1
        elif eng.ans != str(gcd(z, y)):
            eng.wrong_answer(eng.ans, gcd(z, y))
            break
