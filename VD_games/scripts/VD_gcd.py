import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from games.engine import run_game


def generate_gcd():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    question = f"{a} {b}"
    correct = math.gcd(a, b)
    return question, correct

def main():
    rules = 'Find the greatest common divisor of given numbers.'
    run_game(generate_gcd, "GCD Game", rules)

if __name__ == "__main__":
    main()
