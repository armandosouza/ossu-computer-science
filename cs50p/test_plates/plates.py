def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if verify_two_initial_letters(s[0:2]):
        if verify_len_plate(len(s)):
            if verify_special_char(s):
                if verify_number_in_middle(s):
                    return True
    return False


def verify_two_initial_letters(letters):
    if(letters.isalpha()):
        return True
    else:
        return False


def verify_len_plate(length):
    if(2 <= length <= 6):
        return True
    else:
        return False


def verify_special_char(plate):
    if(plate.isalnum()):
        return True


def verify_number_in_middle(plate):
    first_number = False
    letter_after_number = False
    ending_plate = plate[2:]
    if ending_plate[0] == "0":
        return False
    for c in ending_plate:
        if first_number == False and c.isdigit():
            first_number = True
        elif first_number and c.isalpha():
            letter_after_number = True
    if(first_number and letter_after_number):
        return False
    else:
        return True


if __name__ == "__main__":
    main()