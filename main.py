users = {"rian": "ilikecats", "arsh": "comeoncity"}

def createUser():
    '''
    Prompts user to create Admin or Service ID with password
    Added to users dict if not already existing

    Example:
    >>> Enter new username: sudo
    >>> Enter password: asdfghjkl

    Adds {"sudo":"asdfghjkl"} to users dict
    '''

    username = input("Enter new username: ")
    if username not in users:
        password = input("Enter password: ")

        users[username] = password

    else:
        print("User already exists")

def login():
    '''

    '''
