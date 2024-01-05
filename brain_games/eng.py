#!/usr/bin/env python3
from brain_games import cli


def start_game(game):
    cli.welcome_user()
    game.main()


def question(n):
    print(f'Question: {n}')


def answer():
    global ans
    ans = input('Your answer: ')
    return ans


def wrong_answer(a, b):
    print(f"'{a}' is wrong answer ;(. Correct answer was '{b}'. Let's try again, {cli.name}!")


def correct():
    print('Correct!')


def congratulations():
    print(f'Congratulations, {cli.name}!')


def prime(z):
    k = 0
    for i in range(2, z // 2 + 1):
        if (z % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False
