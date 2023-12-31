from random import randrange
from brain_games import cli
from colorama import Fore


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()
    x = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while x <= 3:
        if x == 3:
            print(Fore.GREEN + f'Congratulations, {cli.name}!')
            break
        n = randrange(1, 50)
        print(f'Question: {n}')
        ans = input('Your answer: ')
        if n % 2 == 0 and ans == 'yes' or n % 2 != 0 and ans == 'no':
            print('Correct!')
            x += 1
        elif n % 2 == 0 and ans != 'yes':
            print(f"'{ans}' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {cli.name}!")
            break
        elif n % 2 != 0 and ans != 'no':
            print(f"'{ans}' is wrong answer ;(. Correct answer was 'no'. Let's try again, {cli.name}!")
            break


if __name__ == '__main__':
    main()
