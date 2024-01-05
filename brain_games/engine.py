#!/usr/bin/env python3
import prompt


def start_game(game):
    welcome_user()
    game.main()


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def question(n):
    print(f'Question: {n}')


def answer():
    global ans
    ans = input('Your answer: ')
    return ans


def wrong_answer(a, b):
    print(f"'{a}' is wrong answer ;(. Correct answer was '{b}'. Let's try again, {name}!")


def correct():
    print('Correct!')


def congratulations():
    print(f'Congratulations, {name}!')


def prime(z):
    k = 0
    for i in range(2, z // 2 + 1):
        if (z % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False
