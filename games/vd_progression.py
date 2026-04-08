import random


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)

    progression = [start + i * step for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    
    progression_str = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            progression_str.append("..")
        else:
            progression_str.append(str(num))
    
    question = " ".join(progression_str)
    return question, correct_answer


def generate_question():
    return generate_progression()
