#!/usr/bin/env python3
from random import randrange
from brain_games import engine
from colorama import init, Fore


def main():
    init(autoreset=True)
    print(Fore.LIGHTMAGENTA_EX + 'What number is missing in the progression?')
    x = 0
    while x <= 3:
        y = randrange(1, 20)
        engine.question(y)
        engine.answer()
        if engine.is_prime(y) is True and engine.ans == 'yes' or engine.is_prime(y) is False and engine.ans == 'no':
            if x == 2:
                engine.congratulations()
                break
            else:
                engine.correct()
            x += 1
        elif engine.is_prime(y) is True and engine.ans != 'yes':
            engine.wrong_answer(engine.ans, 'yes')
            break
        elif engine.is_prime(y) is False and engine.ans != 'no':
            engine.wrong_answer(engine.ans, 'no')
            break


if __name__ == '__main__':
    main()
