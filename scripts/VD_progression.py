from VD_games.games.progression import generate_question
from VD_games.games.engine import run_game


def main():
    game_description = "What number is missing in the progression?"
    run_game(generate_question, game_description)


if __name__ == "__main__":
    main()
