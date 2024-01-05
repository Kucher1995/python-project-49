from random import randrange
from brain_games import engine


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    x = 0
    Y = 'yes'
    N = 'no'
    while x < 3:
        z = randrange(1, 50)
        engine.question(z)
        engine.answer()
        if z % 2 == 0 and engine.ans == Y or z % 2 != 0 and engine.ans == N:
            engine.correct()
            x += 1
        elif z % 2 == 0 and engine.ans != Y:
            engine.wrong_answer(engine.ans, N)
            break
        else:
            z % 2 != 0 and engine.ans != N
            engine.wrong_answer(engine.ans, N)
            break
    else:
        engine.congratulations()
