from brain_games import cli


def start_game(game):
    cli.welcome_user()
    game.exercise()
    x = 0
    while x < 3:
        y = game.main()
        if y is True:
            x += 1
        elif y is False:
            break
    else:
        congratulate()


def question(n):
    print(f'Question: {n}')


def answer():
    global ans
    ans = input('Your answer: ')
    return ans


def wrong_answer(a, b):
    print(f"""'{a}' is wrong answer ;(. Correct answer was '{b}'.
Let's try again, {cli.name}!""")


def correctly_answer():
    print('Correct!')


def congratulate():
    print(f'Congratulations, {cli.name}!')


def is_prime(z):
    k = 0
    for i in range(2, z // 2 + 1):
        if (z % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        x % 2 != 0
        return False


def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n
