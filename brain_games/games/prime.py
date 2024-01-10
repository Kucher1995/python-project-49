from random import randrange


def exercise():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def question():
    num1 = randrange(1, 20)
    k = 0
    for i in range(2, num1 // 2 + 1):
        if (num1 % i == 0):
            k = k + 1
    if (k <= 0):
        return num1, 'yes', None, None
    else:
        return num1, 'no', None, None


def main(ans, ch, y=0, x=0):
    if ch == 'yes' and ans == 'yes':
        return True, ans
    elif ch == 'no' and ans == 'no':
        return True, ans
    elif ch == 'yes' and ans != 'yes':
        return False, 'yes'
    else:
        ch == 'no' and ans != 'no'
        return False, 'no'
