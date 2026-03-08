from games.engine import run_game
from games.gcd import generate_question_gcd

def main():
    run_game(
        generate_question_gcd,
        game_name="VD-gcd",
        rules="Find the greatest common divisor of given numbers."
    )

if __name__ == "__main__":
    main()
