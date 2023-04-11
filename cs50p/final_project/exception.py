# own exceptions
class LoginException(Exception):
	"Triggered when occurs an error in login"
	pass

class RegisterException(Exception):
	"Triggered when occurs an error in register"
	pass

class RemoveUserException(Exception):
	"Triggered when occurs an error to remove an user"
	pass