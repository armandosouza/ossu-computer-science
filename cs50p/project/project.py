from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from cfonts import render, say
from newsapi import NewsApiClient
from tinydb import TinyDB, Query
from pwinput import pwinput
from passlib.hash import pbkdf2_sha256
from os import system, name, getenv
from sys import exit
from exception import LoginException, RegisterException, RemoveUserException, UserException
from panels import main_panel, home_panel, interest_panel, article_panel, list_news, list_interests
from dotenv import load_dotenv
from datetime import date
import requests

load_dotenv()
NEWS_API_ID = getenv('NEWS_API_ID')
console = Console()
db = TinyDB('db.json')
Users = Query()
news_api = NewsApiClient(NEWS_API_ID)

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
			if login_user(username, password):
				home(username)
			else:
				console.print('User / Password is not correct!', style='red on white')
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
			raise UserException
		decrypt = pbkdf2_sha256.verify(password, user[0]['password'])
		if not decrypt:
			raise LoginException
		return True
	except (LoginException, UserException):
		clear_console()
		return False


def remove_account(username, password):
	try:
		user = db.search(Users.user == username)
		if not user:
			raise RemoveUserException
		decrypt = pbkdf2_sha256.verify(password, user[0]['password'])
		if not decrypt:
			raise RemoveUserException
		else:
			db.remove(Users.user == username)
			return 'Your account was successfully removed!', 'green on white'
	except RemoveUserException:
		clear_console()
		return 'Your account wasn\'t found!', 'red on white'


def home(username):
	clear_console()
	home_panel(username)
	while True:
		opt = input('Choose an option: ')
		if opt == '1':
			url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_ID}'
			search_news(url, username)
		elif opt == '2':
			user = db.search(Users.user == username)
			list_interests(user[0]['interests'])
			interest = input('Choose one of your interests [enter the ID]: ')
			interest_chose = user[0]['interests'][int(interest) - 1]
			url = ('https://newsapi.org/v2/everything?'
       			f'q={interest_chose}&'
       			'pageSize=25&'
       			'sortBy=popularity&'
       			f'apiKey={NEWS_API_ID}')
			search_news(url, username)
		elif opt == '3':
			clear_console()
			interest_panel(username)
			while True:
				int_opt = input('Choose an option: ')
				if int_opt == '1':
					user = db.search(Users.user == username)
					if len(user[0]['interests']) > 0:
						list_interests(user[0]['interests'])
					else:
						clear_console()
						console.print('Your interest list is empty!', style='red on white')
						interest_panel(username)
				elif int_opt == '2':
					user = db.search(Users.user == username)
					new_interest = input('Enter the name of your new interest: ').lower()
					if new_interest in user[0]['interests']:
						console.print('Interest already added in your list!', style='red on white')
					else:
						interests = user[0]['interests']
						interests.append(new_interest)
						db.update({'interests': interests}, Users.user == username)
						console.print('Interest successfully added!', style='green on white')
				elif int_opt == '3':
					user = db.search(Users.user == username)
					list_interests(user[0]['interests'])
					remove_interest = input('Enter the name of interest to remove it: ').lower()
					if remove_interest not in user[0]['interests']:
						console.print('Interest not found!', style='red on white')
					else:
						interests = []
						for i in user[0]['interests']:
							if i != remove_interest:
								interests.append(i) 
						db.update({'interests': interests}, Users.user == username)
						console.print('Interest successfully removed!', style='green on white')
				elif int_opt == '4':
					clear_console()
					home_panel(username)
					break
				else:
					console.print('Option not valid!', style='red on white')
		elif opt == '4':
			user = db.search(Users.user == username)
			new_password = pwinput(prompt='Enter your new password: ')
			check_password = pwinput(prompt='Enter your new password again: ')
			if new_password == check_password:
				db.update({'password': pbkdf2_sha256.hash(new_password)}, Users.user == username)
				console.print('Password successfully changed!', style='green on white')
			else:
				console.print('Passwords does not match!', style='red on white')
		elif opt == '5':
			clear_console()
			break
		else:
			console.print('Option not valid!', style='red on white')


def search_news(url, user):
	try:
		response = requests.get(url).json()
		articles = response['articles']
		list_news(articles)
		while True:
			news_opt = input('Choose an ID to read the news or press 0 to back to menu: ')
			if int(news_opt) == 0:
				clear_console()
				home_panel(user)
				break
			elif int(news_opt) in range(1, len(articles) + 1):
				article_panel(articles[int(news_opt) - 1])
			else:
				clear_console()
				console.print('Option not valid!', style='red on white')
				home_panel(user)
	except requests.exceptions.RequestException:
		clear_console()
		console.print('There was an error requesting news!', style='red on white')


if __name__ == "__main__":
	main()