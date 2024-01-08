from random import randrange
from brain_games import engine
from brain_games.engine import correctly_answer, wrong_answer


def exercise():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    z = randrange(1, 50)
    engine.question(z)
    engine.answer()
    if engine.is_even(z) is True and engine.ans == 'yes':
        correctly_answer()
        return True
    elif engine.is_even(z) is False and engine.ans == 'no':
        correctly_answer()
        return True
    elif engine.is_even(z) is True and engine.ans != 'yes':
        wrong_answer(engine.ans, 'yes')
        return False
    else:
        engine.is_even(z) is False and engine.ans != 'no'
        wrong_answer(engine.ans, 'no')
        return False
