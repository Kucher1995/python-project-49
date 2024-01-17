from brain_games import cli


def start_game(game):
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
# Launch the selected game. Greeting the player.
# Explanation of the rules. checking the player's answer for correctness


def get_question(n):
    print(f'Question: {n}')
# Displaying a question to the user


def get_answer():
    answer = input('Your answer: ')
    return answer
# Getting a response from the user


def print_wrong_answer(answer, name, correct_answer):
    print(f"""{answer} is wrong answer ;(. Correct answer was {correct_answer}.
Let's try again, {name}!""")
# Display user error message


def print_correct():
    print('Correct!')
# Displaying a message about the user's correct answer


def print_congratulate(name):
    print(f'Congratulations, {name}!')
# Congratulations to the user on his victory
