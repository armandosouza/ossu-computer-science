from validator_collection import validators, checkers, errors
from validators import domain


def main():
    print(check_mail(input("What's your email address? ")))


def check_mail(email):
    try:
        email_address = validators.email(email)
        exist_domain = domain(email_address)
        if exist_domain:
            return None
        return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()