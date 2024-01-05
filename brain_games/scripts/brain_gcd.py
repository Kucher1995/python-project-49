#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games import br_gcd


def main():
    start_game(br_gcd)


if __name__ == '__main__':
    main()
