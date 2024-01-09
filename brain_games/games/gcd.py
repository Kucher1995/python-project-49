from random import randrange
from brain_games import engine


def exercise():
    print('Find the greatest common divisor of given numbers.')


def main():
    z = randrange(20, 50)
    y = randrange(1, 20)
    engine.question(f'{z} {y}')
    ans = input('Your answer: ')
    if ans == str(engine.gcd(z, y)):
        engine.correct_answer()
        return True
    else:
        engine.wrong_answer(ans, engine.gcd(z, y))
        return False
