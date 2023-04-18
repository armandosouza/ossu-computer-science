from project import register_user, login_user, remove_account

username = 'admin'
password = 'admin'
other_password = 'admin123'

def test_register_user():
	assert register_user(username, password) == ('Account has been successfully registered!', 'green on white')
	assert register_user(username, other_password) == ('You already has an account!', 'red on white')


def test_login_user():
	assert login_user(username, password) == True
	assert login_user(username, other_password) == False


def test_remove_account():
	assert remove_account(username, password) == ('Your account was successfully removed!', 'green on white')
	assert remove_account(username, password) == ('Your account wasn\'t found!', 'red on white')