from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def main_panel():
	console.print(Panel(
		"""Welcome to PyJournal! Read and receive news about your interests,
		 filtered and delivered directly to you!\n
		 1. Sign-in to your account\n
		 2. Register a new profile to save your interests\n
		 3. Back to menu\n
		 4. Delete your account\n
		 5. Quit
		 """,
		title='PyJournal!',
		subtitle='CS50P Final Project - Armando Souza',
		padding=2,
		title_align='center', 
		highlight=True,
		style='bold white on blue'))


def home_panel(user):
	console.print(Panel(
		"""PyJournal Homepage. You can read your news, change or set your interests, change your password or logout.\n
		 1. Read random news\n
		 2. Read news based on my interests\n
		 3. Set or change my interests\n
		 4. Change my password\n
		 5. Logout
		 """,
		title='PyJournal - Homepage',
		subtitle=f'{user}',
		padding=2,
		title_align='center', 
		highlight=True,
		style='bold white on blue'))


def interest_panel(user):
	console.print(Panel(
		"""A list with your interests. You can add, change or remove interests from your list.\n
		 1. Check my interest\'s list\n
		 2. Add a new interest\n
		 3. Remove a interest\n
		 4. Back to menu
		 """,
		title='PyJournal - Interests',
		subtitle=f'{user}',
		padding=2,
		title_align='center', 
		highlight=True,
		style='bold white on blue'))


def article_panel(article):
	console.print(Panel(
		f"""{article['description']}\n
			Author: {article['author']}\n
			Published at: {article['publishedAt']}""",
		title=article['title'],
		padding=2,
		highlight=True,
		style='bold white on blue'
	))


def list_news(list):
	table = Table(title='PyJournal News')
	table.add_column('ID', justify='left', style='cyan')
	table.add_column('Title', style='magenta')
	for i, news in enumerate(list):
		table.add_row(str(i+1), news['title'])
	console.print(table)


def list_interests(list):
	table = Table(title='My interests')
	table.add_column('ID', justify='left', style='cyan')
	table.add_column('Interest', style='magenta')
	for i, interest in enumerate(list):
		table.add_row(str(i + 1), interest)
	console.print(table)