import random


OPERATIONS = [
    ("+", lambda x, y: x + y),
    ("-", lambda x, y: x - y),
    ("*", lambda x, y: x * y),
]


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation, func = random.choice(OPERATIONS)
    question = f"{num1} {operation} {num2}"
    correct_answer = str(func(num1, num2))
    return question, correct_answer
