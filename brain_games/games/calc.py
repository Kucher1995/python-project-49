from random import randrange


EXERCISE = 'What is the result of the expression?'


def get_result(num1, num2, random_expression):
    '''Calculating the result of a random expression'''
    match random_expression:
        case '-':
            x = num1 - num2
        case '+':
            x = num1 + num2
        case '*':
            x = num1 * num2
    return x


def generate_question():
    '''Generating a random expression and returns the correct answer.'''
    num1 = randrange(20, 50)
    num2 = randrange(1, 20)
    massiv = ['-', '+', '*']
    random_operation = massiv[randrange(0, 3)]
    random_expression = f'{num1} {random_operation} {num2}'
    correct_answer = get_result(num1, num2, random_operation)
    return random_expression, correct_answer
