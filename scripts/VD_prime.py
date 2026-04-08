from VD_games.games.prime import generate_question
from VD_games.games.engine import run_game


def main():
    game_description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(generate_question, game_description)


if __name__ == "__main__":
    main()
