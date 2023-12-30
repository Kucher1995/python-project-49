from random import randrange
from brain_games import cli
from colorama import Fore


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()
    x = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while x < 3:
        n = randrange(1, 50)
        print(f'Question: {n}')
        answer = input('Your answer: ')
        if x >= 2:
            print(Fore.GREEN + f'Congratulations, {cli.name}!')
            break
        elif n % 2 == 0 and answer == 'yes' or n % 2 != 0 and answer == 'no':
            print('Correct!')
            x += 1
        elif n % 2 == 0 and answer != 'yes':
            print(Fore.RED + f"{answer} is wrong answer ;(. Correct answer was 'yes'. Let's try again, {cli.name}!")
            break
        elif n % 2 != 0 and answer != 'no':
            print(Fore.RED + f"{answer} is wrong answer ;(. Correct answer was 'no'. Let's try again, {cli.name}!")
            break


if __name__ == '__main__':
    main()
