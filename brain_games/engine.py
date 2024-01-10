from brain_games import cli


def start_game(game):
    name = cli.welcome_user()
    game.exercise()
    x = 0
    while x < 3:
        w = game.question()
        num1 = w[2]
        num2 = w[3]
        question(w[0])
        ans = answer()
        check = w[1]
        y = game.main(ans, check, num1, num2)
        true_false = y[0]
        false = y[1]
        if true_false is True:
            correct_answer()
            x += 1
            continue
        elif true_false is False:
            wrong_answer(ans, name, false)
            break
    else:
        congratulate(name)


def question(n):
    print(f'Question: {n}')


def answer():
    ans = input('Your answer: ')
    return ans


def wrong_answer(ans, name, check):
    print(f"""{ans} is wrong answer ;(. Correct answer was {check}.
Let's try again, {name}!""")


def correct_answer():
    print('Correct!')


def congratulate(name):
    print(f'Congratulations, {name}!')
