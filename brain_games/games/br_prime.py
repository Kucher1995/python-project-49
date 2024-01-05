from random import randrange
from brain_games import engine


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    x = 0
    while x < 3:
        y = randrange(1, 20)
        engine.question(y)
        engine.answer()
        if engine.prime(y) is True and engine.ans == 'yes' or engine.prime(y) is False and engine.ans == 'no':
            engine.correct()
            x += 1
        elif engine.prime(y) is True and engine.ans != 'yes':
            engine.wrong_answer(engine.ans, 'yes')
            break
        else:
            engine.prime(y) is False and engine.ans != 'no'
            engine.wrong_answer(engine.ans, 'no')
            break
    else:
        engine.congratulations()
