from random import randrange


def exercise():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def generate_question():
    num1 = randrange(1, 20)
    k = 0
    for i in range(2, num1 // 2 + 1):
        if (num1 % i == 0):
            k = k + 1
    if (k <= 0):
        return num1, 'yes'
    else:
        return num1, 'no'
