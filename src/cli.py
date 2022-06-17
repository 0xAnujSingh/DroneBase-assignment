from dotenv import load_dotenv
load_dotenv()

from user import User
from api import getWeather, validate
from getpass import getpass

def login():
    print("Login to use the app:")
    username = input("Username: ")
    password = getpass(prompt="Password: ")
    
    user = User(username = username)

    valid_password = user.checkPassword(password)

    if (valid_password is True):
        return user
    
    return False

def printHelp():
    print("1. createUser: To create new user")
    print("2. updateUser: To update user")
    print("3. deleteUser: To delete user")
    print("4. listUsers: To read all users")
    print("5. getWeather: For weather detail")
    print("6. help: For all command information")
    print("7. exit: Out from the complete code")
    print("0. logout\n")

loggedInUser = None
allUsers = User.readAll()

if len(allUsers) == 0:
    print("Create a new user to use the app")
    username = input("Enter Username: ")
    password = getpass(prompt="Enter Password: ")
    
    loggedInUser = User.createNew(userName=username, password=password)
    print("Created User\n")

print('Commands List:')
printHelp()

while True:
    if (loggedInUser is None):
        loggedInUser = login()

        if loggedInUser is False:
            print("Incorrect Credentials")

        print("\nLogged In\n")

        continue
    
    cmd = input("Enter a command: ").strip()

    if cmd == "createUser" or cmd == "1":
        userName = input("Enter your username: ")
        password = getpass(prompt="Enter your password: ")
        
        is_exists = User.findByUsername(userName)
        if (is_exists == False):
            users = User.createNew(userName, password)
            print(f"New user is created {userName}")
            continue

        print("User already exists")  

    elif cmd == "updateUser" or cmd == "2":
        id = int(input("Enter your Id: "))
        print("What do you wants to update username or password")
        print("username: For updating username ")
        print("password: for updating password ")
        
        cmd = input("Type:\n1. Update username\n2. Update password\n").strip()
        if cmd == "1":
            username = input("Enter your username: ").strip()
            User.update(id, username = username)

        elif cmd == "2":
            password = getpass("Enter a password: ").strip()
            User.update(id, password = password)

        else:
            print("Command not supported")
            continue
        
        print("Updated")

    elif cmd == "deleteUser" or cmd == "3":
        id = int(input("Enter your id: "))

        users = User.delete(id)

        if loggedInUser.id == id:
            loggedInUser = None

        print(f"Deleted with id {id}")
        
    elif cmd == "listUsers" or cmd == "4":
        users = User.readAll()

        print(f"Found {len(users)} users:")
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}")

    elif cmd == "getWeather" or cmd == "5":
        flag = 0
        while flag == 0:
            date = input("Enter date for scheduled flight (in DD/MM/YYYY): ")
            flag = validate(date)

        city = input("Enter city name: ")
        getWeather(city)
        print(f"Your flight has been schedule on {date} date")

    elif cmd == "help" or cmd == "6":
        printHelp()

    elif cmd == "exit" or cmd == "7":
        exit()

    elif cmd == "logout" or cmd == "0":
        loggedInUser = None

    else:
        print("Invalid command. Please try from the given options")
