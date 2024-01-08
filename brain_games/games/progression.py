from random import randint
from brain_games import engine


def exercise():
    print('What number is missing in the progression?')


def main():
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
    engine.question(string)
    engine.answer()
    if engine.ans == str(correct_answer):
        engine.correctly_answer()
        return True
    else:
        engine.ans != str(correct_answer)
        engine.wrong_answer(engine.ans, correct_answer)
        return False
