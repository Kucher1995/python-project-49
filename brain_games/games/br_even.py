from random import randrange
from brain_games import engine


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    x = 0
    while x <= 3:
        z = randrange(1, 50)
        engine.question(z)
        engine.answer()
        if z % 2 == 0 and engine.ans == 'yes' or z % 2 != 0 and engine.ans == 'no':
            if x == 2:
                engine.congratulations()
                break
            else:
                engine.correct()
            x += 1
        elif z % 2 == 0 and engine.ans != 'yes':
            engine.wrong_answer(engine.ans, 'yes')
            break
        elif z % 2 != 0 and engine.ans != 'no':
            engine.wrong_answer(engine.ans, 'no')
            break
