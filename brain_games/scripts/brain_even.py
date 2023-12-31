from random import randrange
from brain_games import cli
from brain_games import phras


def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()
    x = 0
    y = "yes"
    n = "no"
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while x <= 3:
        if x == 3:
            phras.congratulations()
            break
        z = randrange(1, 50)
        phras.question(z)
        phras.answer()
        if z % 2 == 0 and phras.ans == y or z % 2 != 0 and phras.ans == n:
            print('Correct!')
            x += 1
        elif z % 2 == 0 and phras.ans != y:
            phras.wrong_answer(phras.ans, y)
            break
        elif z % 2 != 0 and phras.ans != n:
            phras.wrong_answer(phras.ans, n)
            break


if __name__ == '__main__':
    main()
