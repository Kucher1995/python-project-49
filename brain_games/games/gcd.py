from random import randrange


exercise = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num2


def generate_question():
    num1 = randrange(1, 20)
    num2 = randrange(20, 50)
    numbs = (f'{num2} {num1}')
    ans = gcd(num1, num2)
    return numbs, ans
