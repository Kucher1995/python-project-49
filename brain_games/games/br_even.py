#!/usr/bin/env python3
from random import randrange
from brain_games import engine
from colorama import init, Fore


def main():
    init(autoreset=True)
    print(Fore.LIGHTMAGENTA_EX + 'Answer "yes" if the number is even, otherwise answer "no".')
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


if __name__ == '__main__':
    main()
