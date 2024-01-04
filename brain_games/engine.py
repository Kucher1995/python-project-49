from brain_games.cli import welcome_user
from colorama import Fore


def start_game(game):
    welcome_user()
    game

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
