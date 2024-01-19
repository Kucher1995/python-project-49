from brain_games import cli


def start_game(game):
    '''Launch the selected game.
    Greeting the player.
    Explanation of the rules.
    Checking the player's answer for correctness
    '''
    name = cli.welcome_user()
    print(game.EXERCISE)
    x = 0
    while x < 3:
        question, correct_answer = game.generate_question()
        get_question(question)
        user_answer = get_answer()
        if user_answer == str(correct_answer):
            print_correct()
            x += 1
            continue
        elif user_answer != correct_answer:
            print_wrong_answer(user_answer, name, correct_answer)
            break
    else:
        print_congratulate(name)


def get_question(n):
    '''Displaying a question to the user'''
    print(f'Question: {n}')


def get_answer():
    '''Getting a response from the user'''
    answer = input('Your answer: ')
    return answer


def print_wrong_answer(answer, name, correct_answer):
    '''Display user error message'''
    print(f"""{answer} is wrong answer ;(. Correct answer was {correct_answer}.
Let's try again, {name}!""")


def print_correct():
    '''Displaying a message about the user's correct answer'''
    print('Correct!')


def print_congratulate(name):
    '''Congratulations to the user on his victor'''
    print(f'Congratulations, {name}!')
