from random import randrange
from brain_games import engine


def exercise():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    x = randrange(1, 50)
    ans = engine.question_answer(x)
    if engine.is_even(x) is True and ans == 'yes':
        engine.correct_answer()
        return True
    elif engine.is_even(x) is False and ans == 'no':
        engine.correct_answer()
        return True
    elif engine.is_even(x) is True and ans != 'yes':
        engine.wrong_answer(ans, 'yes')
        return False
    else:
        engine.is_even(x) is False and ans != 'no'
        engine.wrong_answer(ans, 'no')
        return False
