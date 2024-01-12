from brain_games import cli


def start_game(game):
    name = cli.welcome_user()
    game.exercise()
    x = 0
    while x < 3:
        w = game.generate_question()
        get_question(w[0])
        ans = get_answer()
        if ans == str(w[1]):
            print_correct()
            x += 1
            continue
        elif ans != w[1]:
            print_wrong_answer(ans, name, w[1])
            break
    else:
        print_congratulate(name)


def get_question(n):
    print(f'Question: {n}')


def get_answer():
    ans = input('Your answer: ')
    return ans


def print_wrong_answer(ans, name, check):
    print(f"""{ans} is wrong answer ;(. Correct answer was {check}.
Let's try again, {name}!""")


def print_correct():
    print('Correct!')


def print_congratulate(name):
    print(f'Congratulations, {name}!')
