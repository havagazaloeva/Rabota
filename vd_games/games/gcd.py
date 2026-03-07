import random
import math

def generate_question_gcd():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    correct = math.gcd(a, b)
    question = f"{a} {b}"
    return question, correct
