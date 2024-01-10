from random import randrange


def exercise():
    print('Find the greatest common divisor of given numbers.')


def question():
    num1 = randrange(1, 20)
    num2 = randrange(20, 50)
    numbs = (f'{num2} {num1}')
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return numbs, num2, None, None


def main(ans, check, y=0, x=0):
    if ans == str(check):
        return True, ans
    else:
        return False, check
