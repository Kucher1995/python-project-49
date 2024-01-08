from random import randrange
from brain_games import engine


def exercise():
    print('Find the greatest common divisor of given numbers.')


def main():
    z = randrange(20, 50)
    y = randrange(1, 20)
    engine.question(f'{z} {y}')
    engine.answer()
    if engine.ans == str(engine.gcd(z, y)):
        engine.correctly_answer()
        return True
    else:
        engine.wrong_answer(engine.ans, engine.gcd(z, y))
        return False
