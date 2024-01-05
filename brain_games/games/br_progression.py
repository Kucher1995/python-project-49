from random import randint
from brain_games import engine


def main():
    print('What number is missing in the progression?')
    x = 0
    while x < 3:
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
            engine.correct()
            x += 1
        else:
            engine.ans != str(correct_answer)
            engine.wrong_answer(engine.ans, correct_answer)
            break
    else:
        engine.congratulations()
