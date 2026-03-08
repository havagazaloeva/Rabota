import random

def generate_question_even():
    number = random.randint(1, 100)
    question = str(number)
    correct = "yes" if number % 2 == 0 else "no"
    return question, correct
