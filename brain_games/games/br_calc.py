from random import randrange
from brain_games import eng


def main():
    print('What is the result of the expression?')
    x = 0
    while x <= 3:
        z = randrange(20, 50)
        y = randrange(1, 20)
        massiv = [f'{z} - {y}', f'{z} + {y}', f'{z} * {y}']
        random_expression = massiv[randrange(0, 3)]
        result = eval(random_expression)
        eng.question(random_expression)
        eng.answer()
        if eng.ans == str(result):
            if x == 2:
                eng.congratulations()
                break
            else:
                eng.correct()
            x += 1
        elif eng.ans != str(result):
            eng.wrong_answer(eng.ans, result)
            break
