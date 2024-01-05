from random import randrange
from brain_games import engine
from brain_games.engine import prime


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    x = 0
    while x < 3:
        y = randrange(1, 20)
        engine.question(y)
        engine.answer()
        if prime(y) is True and engine.ans == 'yes':
            engine.correct()
            x += 1
        elif prime(y) is False and engine.ans == 'no':
            engine.correct()
            x += 1
        elif prime(y) is True and engine.ans != 'yes':
            engine.wrong_answer(engine.ans, 'yes')
            break
        else:
            prime(y) is False and engine.ans != 'no'
            engine.wrong_answer(engine.ans, 'no')
            break
    else:
        engine.congratulations()
