from rich.console import Console
from rich.panel import Panel

console = Console()

def main_panel():
	console.print(Panel(
		"""Welcome to PyJournal! Read and receive news about your interests,
		 filtered and delivered directly to you!\n
		 1. Sign-up to your account\n
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
		 1. Read news\n
		 2. Change my interests\n
		 3. Change my password\n
		 4. Logout
		 """,
		title='PyJournal - Homepage',
		subtitle=f'{user}',
		padding=2,
		title_align='center', 
		highlight=True,
		style='bold white on blue'))


def interest_panel():
	console.print(Panel(
		"""A list with your interests. You can add, change or remove interests from your list.\n
		 1. Check my interest\'s list\n
		 2. Add a new interest\n
		 3. Remove a new interest\n
		 4. Back to menu
		 """,
		title='PyJournal - Interests',
		subtitle=f'{user}',
		padding=2,
		title_align='center', 
		highlight=True,
		style='bold white on blue'))