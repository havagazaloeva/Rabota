from games.engine import run_game
from games.calc import generate_question_calc

def main():
    run_game(
        generate_question_calc,
        game_name="VD-calc",
        rules="What is the result of the expression?"
    )

if __name__ == "__main__":
    main()
