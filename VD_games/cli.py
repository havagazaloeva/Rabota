import prompt

def welcome_user():
	name = prompt.string('Your name?')
	print(f'Hello, {name}!')
