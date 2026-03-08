from VD_games.cli import welcome_user


def game_function():
	welcome_user()
	return "Добро пожаловать в игру!"
if __name__ == "__main__":
	print(game_function()) 
