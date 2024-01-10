from random import randint


def exercise():
    print('What number is missing in the progression?')


def random_progression():
    num1 = randint(1, 10)
    num2 = randint(100, 120)
    n = randint(2, 9)
    numbers = []
    for i in range(num1, num2, n):
        numbers.append(i)
    numbers.sort()
    correct_answer = numbers[n]
    numbers[n] = ".."
    string = " ".join(map(str, numbers[0:10]))
    return correct_answer, string


def question():
    num1 = randint(1, 10)
    num2 = randint(100, 120)
    n = randint(2, 9)
    numbers = []
    for i in range(num1, num2, n):
        numbers.append(i)
    numbers.sort()
    correct_answer = numbers[n]
    numbers[n] = ".."
    string = " ".join(map(str, numbers[0:10]))
    return string, correct_answer, None, None


def main(ans, correct_answer, y=0, x=0):
    if ans == str(correct_answer):
        return True, ans
    else:
        ans != str(correct_answer)
        return False, correct_answer
