from random import randrange


EXERCISE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num1):
    '''Checking a number for prime.'''
    if num1 == 1:
        return False
    for i in range(2, int(num1**0.5) + 1):
        if num1 % i == 0:
            return False
    return True


def generate_question():
    '''Generates random number and returns the correct answer.'''
    num1 = randrange(1, 20)
    if is_prime(num1) is True:
        return num1, 'yes'
    else:
        return num1, 'no'
