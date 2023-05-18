def correct_len(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def correct_characters(name):
    for character in name:
        if not (character.isalnum() or character == "_" or character == "-"):
            return False
        return True


def no_redundant_symbols(name):
    if ' ' in name:
        return False
    return True


def username_validation(name):
    if correct_len(name) and correct_characters(name) and no_redundant_symbols(name):
        return True
    return False


current_user_names = input().split(", ")
for user in current_user_names:
    if username_validation(user):
        print(user)