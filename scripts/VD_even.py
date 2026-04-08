from VD_games.games.even import generate_question
from VD_games.games.engine import run_game


def main():
    game_description = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(generate_question, game_description)


if __name__ == "__main__":
    main()
