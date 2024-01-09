from random import randrange
from brain_games import engine


def exercise():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def main():
    y = randrange(1, 20)
    engine.question(y)
    ans = input('Your answer: ')
    if engine.is_prime(y) is True and ans == 'yes':
        engine.correct_answer()
        return True
    elif engine.is_prime(y) is False and ans == 'no':
        engine.correct_answer()
        return True
    elif engine.is_prime(y) is True and ans != 'yes':
        engine.wrong_answer(ans, 'yes')
        return False
    else:
        engine.is_prime(y) is False and ans != 'no'
        engine.wrong_answer(ans, 'no')
        return False
