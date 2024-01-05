from random import randint
from brain_games import eng


def main():
    print('What number is missing in the progression?')
    x = 0
    while x <= 3:
        num1 = randint(1, 10)
        num2 = randint(100, 120)
        n = randint(2, 9)
        numbers = []
        for i in range(num1, num2, n):
            numbers.append(i)
        numbers.sort()
        cor_ans = numbers[n]
        numbers[n] = ".."
        string = " ".join(map(str, numbers[0:10]))
        eng.question(string)
        eng.answer()
        if eng.ans == str(cor_ans):
            if x == 2:
                eng.congratulations()
                break
            else:
                eng.correct()
            x += 1
        elif eng.ans != str(cor_ans):
            eng.wrong_answer(eng.ans, cor_ans)
            break
