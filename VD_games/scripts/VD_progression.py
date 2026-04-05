import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from games.engine import run_game


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)

    progression = []
    for i in range(length):
        progression.append(start + i * step)

    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer

def main():
    rules = "What number is missing in the progression?"
    run_game(generate_progression, "Progression Game", rules)

if __name__ == "__main__":
    main()
