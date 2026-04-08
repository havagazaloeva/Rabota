import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from games.engine import run_game


def is_even(n):
    return n % 2 == 0

def generate_even():
    num = random.randint(1, 100)
    question = str(num)
    correct_answer = "yes" if is_even(num) else "no"
    return question, correct_answer

def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(generate_even, "Even Game", rules)

if __name__ == "__main__":
    main()
