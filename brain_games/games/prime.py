from random import randrange
from brain_games import engine


def exercise():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def main():
    y = randrange(1, 20)
    engine.question(y)
    engine.answer()
    if engine.is_prime(y) is True and engine.ans == 'yes':
        engine.correctly_answer()
        return True
    elif engine.is_prime(y) is False and engine.ans == 'no':
        engine.correctly_answer()
        return True
    elif engine.is_prime(y) is True and engine.ans != 'yes':
        engine.wrong_answer(engine.ans, 'yes')
        return False
    else:
        engine.is_prime(y) is False and engine.ans != 'no'
        engine.wrong_answer(engine.ans, 'no')
        return False
