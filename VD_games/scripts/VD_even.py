from games.engine import run_game
from games.even import generate_question_even

def main():
    run_game(
        generate_question_even,
        game_name="VD-even",
        rules="Answer 'yes' if the number is even, otherwise answer 'no'."
    )

if __name__ == "__main__":
    main()
