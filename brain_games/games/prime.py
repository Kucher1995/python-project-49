from random import randrange


def exercise():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def generate_question():
    num1 = randrange(1, 20)
    if num1 <= 1:
        return num1, 'yes'
    for i in range(2, int(num1**0.5) + 1):
        if num1 % i == 0:
            return num1, 'no'
    return num1, 'yes'
