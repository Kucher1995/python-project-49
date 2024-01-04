#!/usr/bin/env python3
from brain_games import cli
from colorama import Fore


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
    print(Fore.RED + f"'{a}' is wrong answer ;(. Correct answer was '{b}'. Let's try again, {cli.name}!")


def correct():
    print('Correct!')


def congratulations():
    print(Fore.GREEN + f'Congratulations, {cli.name}!')
