from random import randrange
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()
    x = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while x < 3:
        n = randrange(1, 50)
        print(f'Question: {n}')
        answer = input('Your answer:')
        if x >= 2:
            print(f'Congratulations,!')
            break
        elif n % 2 == 0 and answer == 'yes' or n % 2 != 0 and answer == 'no':
            print('Correct!')
            x += 1
        elif n % 2 == 0 and answer != 'yes':
            print(f"{answer} is wrong answer ;(. Correct answer was 'yes'. Let's try again,!")
            break
        elif n % 2 != 0 and answer != 'no':
            print(f"{answer} is wrong answer ;(. Correct answer was 'no'. Let's try again,!")
            break

if __name__ == '__main__':
    main()
