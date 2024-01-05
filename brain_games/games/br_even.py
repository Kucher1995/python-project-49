from random import randrange
from brain_games import engine
from brain_games.engine import correct, wrong_answer, congratulations


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    x = 0
    Y = 'yes'
    N = 'no'
    while x < 3:
        z = randrange(1, 50)
        engine.question(z)
        engine.answer()
        if z % 2 == 0 and engine.ans == Y:
            correct()
            x += 1
        elif z % 2 != 0 and engine.ans == N:
            correct()
            x += 1
        elif z % 2 == 0 and engine.ans != Y:
            wrong_answer(engine.ans, N)
            break
        else:
            z % 2 != 0 and engine.ans != N
            wrong_answer(engine.ans, N)
            break
    else:
        congratulations()
