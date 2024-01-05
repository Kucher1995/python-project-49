#!/usr/bin/env python3
from random import randrange
from brain_games import eng


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    x = 0
    while x <= 3:
        y = randrange(1, 20)
        eng.question(y)
        eng.answer()
        if eng.prime(y) is True and eng.ans == 'yes' or eng.prime(y) is False and eng.ans == 'no':
            if x == 2:
                eng.congratulations()
                break
            else:
                eng.correct()
            x += 1
        elif eng.prime(y) is True and eng.ans != 'yes':
            eng.wrong_answer(eng.ans, 'yes')
            break
        elif eng.prime(y) is False and eng.ans != 'no':
            eng.wrong_answer(eng.ans, 'no')
            break


if __name__ == '__main__':
    main()
