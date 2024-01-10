from random import randint


def exercise():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def question():
    num1 = randint(1, 20)
    if num1 % 2 == 0:
        return num1, 'yes', None, None
    else:
        num1 % 2 != 0
        return num1, 'no', None, None


def main(ans, z, y=0, x=0):
    if z == 'yes' and ans == 'yes':
        return True, ans
    elif z == 'no' and ans == 'no':
        return True, ans
    elif z == 'yes' and ans != 'yes':
        return False, 'yes'
    else:
        z == 'no' and ans != 'no'
        return False, 'no'
