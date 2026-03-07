import random

def generate_question_calc():
  operators = ('+', '-', '*')
  a = random.randint(1, 20)
  b = random.randint(1, 20)
  op = random.choice(operators)

  if op == '+':
    correct = a + b
  elif op == '-':
    correct = a - b
  else:
    correct = a * b

  question = f"{a} {op} {b}"
  return question, correct
