import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from games.engine import run_game


def generate_calc():
    operations = ['+', '-', '*']
    op = random.choice(operations)
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    if op == '+':
        correct = a + b
    elif op == '-':
        correct = a - b
    else:
        correct = a * b

    question = f"{a} {op} {b}"
    return question, correct

def main():
    rules = 'What is the result of the expression?'
    run_game(generate_calc, "Calculator Game", rules)

if __name__ == "__main__":
    main()
