#!/usr/bin/env python3
from random import randint
from brain_games import engine
from colorama import init, Fore


def main():
    init(autoreset=True)
    print(Fore.LIGHTMAGENTA_EX + 'What number is missing in the progression?')
    x = 0
    while x <= 3:
        num1 = randint(1, 10)
        num2 = randint(100, 120)
        n = randint(2, 9)
        numbers = []
        for i in range(num1, num2, n):
            numbers.append(i)
        numbers.sort()
        cor_ans = numbers[n]
        numbers[n] = ".."
        string = " ".join(map(str, numbers[0:10]))
        engine.question(string)
        engine.answer()
        if engine.ans == str(cor_ans):
            if x == 2:
                engine.congratulations()
                break
            else:
                engine.correct()
            x += 1
        elif engine.ans != str(cor_ans):
            engine.wrong_answer(engine.ans, cor_ans)
            break


if __name__ == '__main__':
    main()
