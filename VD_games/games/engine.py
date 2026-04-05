from prompt import string


def run_game(generate_question, game_name, rules):
    print(f"Welcome to the {game_name}!")
    print("Welcome to the VD Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    print(rules)
    rounds = 3

    for _ in range(rounds):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = string("Your answer: ")

        if str(user_answer) == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
