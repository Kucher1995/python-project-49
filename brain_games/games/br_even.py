from random import randrange
from brain_games import eng


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    x = 0
    while x <= 3:
        z = randrange(1, 50)
        eng.question(z)
        eng.answer()
        if z % 2 == 0 and eng.ans == 'yes' or z % 2 != 0 and eng.ans == 'no':
            if x == 2:
                eng.congratulations()
                break
            else:
                eng.correct()
            x += 1
        elif z % 2 == 0 and eng.ans != 'yes':
            eng.wrong_answer(eng.ans, 'yes')
            break
        elif z % 2 != 0 and eng.ans != 'no':
            eng.wrong_answer(eng.ans, 'no')
            break
