from random import randrange, choice
from brain_games import cli
from brain_games import engine


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()
    x = 0
    print('What is the result of the expression?')
    while x <= 3:
        z = randrange(20, 50)
        y = randrange(1, 20)
        engine.question()
        engine.answer()



if __name__ == '__main__':
    main()
