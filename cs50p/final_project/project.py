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
from exception import LoginException, RegisterException

console = Console()
db = TinyDB('db.json')
Users = Query()

def clear_console():
	system('cls' if name == 'nt' else 'clear')


def panel():
	console.print(Panel(
		"""Welcome to PyJournal! Read and receive news about your interests,
		 filtered and delivered directly to you!\n
		 1. Sign-up to your account\n
		 2. Register a new profile to save your interests\n
		 3. Back to menu\n
		 4. Quit
		 """,
		title='PyJournal!',
		subtitle='CS50P Final Project - Armando Souza',
		padding=2,
		title_align='center', 
		highlight=True,
		style='bold white on blue'))


def main():
	title = render('PyJournal', font="shade", colors=['white', 'blue'], align='center')
	print(title)
	panel()
	while True:
		opt = str(input())
		if opt == '1':
			login_user()
			break
		elif opt == '2':
			register_user()
			panel()
			pass
		elif opt == '3':
			clear_console()
			panel()
			pass
		elif opt == '4':
			exit()
		else:
			console.print('Option not valid!', style='red on white')


def register_user():
	try:
		new_user = input('Register your username: ')
		new_pass = pwinput(prompt='Register your password: ')
		encrypt = pbkdf2_sha256.hash(new_pass)
		if db.search(Users.user == new_user):
			raise RegisterException
		else:
			db.insert({'user': new_user, 'password': encrypt, 'interests': []})
			console.print('Account has been successfully registered!', style='green on white')
	except RegisterException:
		console.print('You already has an account!', style='red on white')
		clear_console()


def login_user():
	try:
		username = input('Username: ')
		password = pwinput(prompt='Password: ')
		user = db.search(Users.user == username)
		decrypt = pbkdf2_sha256.verify(password, user[0]['password'])
		if not decrypt:
			raise LoginException
	except LoginException:
		console.print('Password is not correct!', style='red on white')
		clear_console()


if __name__ == "__main__":
	main()