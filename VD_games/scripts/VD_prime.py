import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from games.engine import run_game


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime():
    num = random.randint(1, 100)
    question = str(num)
    correct_answer = "yes" if is_prime(num) else "no"
    return question, correct_answer

def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(generate_prime, "Prime Game", rules)

if __name__ == "__main__":
    main()
