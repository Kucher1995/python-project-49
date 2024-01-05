#!/usr/bin/env python3
from colorama import init, Fore
import prompt


def start_game(game):
    welcome_user()
    game.main()


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    init(autoreset=True)
    name = prompt.string(Fore.BLUE + 'May I have your name? ')
    print(Fore.BLUE + f'Hello, {name}!')
    return name


def question(n):
    init(autoreset=True)
    print(Fore.MAGENTA + f'Question: {n}')


def answer():
    global ans
    init(autoreset=True)
    ans = input(Fore.MAGENTA + 'Your answer: ')
    return ans


def wrong_answer(a, b):
    print(Fore.RED + f"'{a}' is wrong answer ;(. Correct answer was '{b}'. Let's try again, {name}!")


def correct():
    init(autoreset=True)
    print(Fore.YELLOW + 'Correct!')


def congratulations():
    print(Fore.GREEN + f'Congratulations, {name}!')


def is_prime(z):
    k = 0
    for i in range(2, z // 2 + 1):
        if (z % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False
