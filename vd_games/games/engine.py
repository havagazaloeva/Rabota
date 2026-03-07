def run_game(generate_question, game_name, rules):
    print(f"Welcome to the {game_name}!")
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(rules)

    rounds = 3
    for _ in range(rounds):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        try:
            user_answer = int(user_answer)
        except ValueError:
            pass
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
