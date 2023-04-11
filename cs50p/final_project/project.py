from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from cfonts import render, say
from newsapi import NewsApiClient
from tinydb import TinyDB, Query
from pwinput import pwinput
from passlib.hash import pbkdf2_sha256
from os import system, name
from sys import exit
from exception import LoginException, RegisterException, RemoveUserException
from panels import main_panel, home_panel

console = Console()
db = TinyDB('db.json')
Users = Query()

def clear_console():
	system('cls' if name == 'nt' else 'clear')


def main():
	title = render('PyJournal', font="shade", colors=['white', 'blue'], align='center')
	print(title)
	main_panel()
	while True:
		opt = str(input())
		if opt == '1':	
			username = input('Username: ')
			password = pwinput(prompt='Password: ')
			login_user(username, password)
			main_panel()
		elif opt == '2':
			new_user = input('Register your username: ')
			new_pass = pwinput(prompt='Register your password: ')
			new_register = register_user(new_user, new_pass)
			clear_console()
			console.print(new_register[0], style=new_register[1])
			main_panel()
		elif opt == '3':
			clear_console()
			main_panel()
		elif opt == '4':
			username = input('Username: ')
			password = pwinput(prompt='Password: ')
			remove_user = remove_account(username, password)
			clear_console()
			console.print(remove_user[0], style=remove_user[1])
			main_panel()
		elif opt == '5':
			clear_console()
			exit()
		else:
			console.print('Option not valid!', style='red on white')


def register_user(new_user, new_pass):
	try:
		encrypt = pbkdf2_sha256.hash(new_pass)
		if db.search(Users.user == new_user):
			raise RegisterException
		else:
			db.insert({'user': new_user, 'password': encrypt, 'interests': []})
			return 'Account has been successfully registered!', 'green on white'
	except RegisterException:
		return 'You already has an account!', 'red on white'


def login_user(username, password):
	try:
		user = db.search(Users.user == username)
		if not user:
			raise LoginException
		decrypt = pbkdf2_sha256.verify(password, user[0]['password'])
		if not decrypt:
			raise LoginException
		home(username)
	except LoginException:
		clear_console()
		console.print('User / Password is not correct!', style='red on white')


def remove_account(username, password):
	try:
		user = db.search(Users.user == username)
		while True:
			confirm_remove = input('Do you really want to remove your account? [Y|N] ')
			if confirm_remove.upper() == 'Y':
				decrypt = pbkdf2_sha256.verify(password, user[0]['password'])
				if not decrypt:
					raise RemoveUserException
				else:
					db.remove(Users.user == username)
					return 'Your account was successfully removed!', 'green on white'
				break
			if confirm_remove.upper() == 'N':
				break
	except RemoveUserException:
		clear_console()
		return 'Your account wasn\'t found!', 'red on white'


def home(user):
	clear_console()
	home_panel(user)
	while True:
		opt = input("Choose an option: ")
		


if __name__ == "__main__":
	main()