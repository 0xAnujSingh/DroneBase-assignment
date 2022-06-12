import bcrypt
from app import Users

# def login(id, password):
#     for i in range(3):
#         user_id = input("Please enter your registered user_id: ")
#         user_password = input("Please enter your registered password: ")
#         if id == user_id:
#             # print("Correct login")
#             return id
    
#         if password == user_password:
#             # print("Correct passsword")
#             return password

#         else:
#             print("Please enter correct id or password\n") 

#     return login(id, password)
#     # return ("Invalid user_id or password ")   
                 
# login("1234", "12345")



def login(id, password):
    name = input("Please enter your registered user_id: ")
    passw = input("Password: ")
    flag = False
    while not flag:
        if id != name or password != passw:
            return login(id, password)
        else:
            flag = True
            print("You enter correct id and password\n")
            continue
        

login("1234", "12345")


print("createUser: To create new user")
print("updateUser: To update user")
print("deleteUser: To delete user")
print("readUser: To read all users")


dict = {}

while True:
    print("\n", end="")
    cmd = input("Enter a command: ")

    # It will create a new user with new login and password
    if cmd == "createUser":

        userName = input("Enter your id: ")
        password = input("Enter your password: ")
        
        # If login and password already exists then print already exists  
        # if id in dict: 
        #     print("Id already exists. Please enter another one")
        #     continue

        dict[userName] = Users(userName)
        dict[password] = Users(password)


    elif cmd == "updateUser":
        pass

    elif cmd == "deleteUser":
        pass

    elif cmd == "readUser":
        pass

    else:
        print("Invalid command. Please try from the given options")



















# def login(id, password):
#     name = input("Enter your id: ")
#     passw = input("Enter your passw: ")
#     flag = False
#     dict = {}
#     while not flag:
#         if id != name or password != passw:
#             print("Invalid id or password")
#             return login(id, password)
#         else:
#             flag = True
#             dict[name] = passw
            
#             print("You enter correct id and password")
#             continue
#     print(dict)    

# login("1234", "12345")

# print("createUser: To create new user")
# print("updateUser: To update user")
# print("deleteUser: To delete user")
# print("readUser: To read all users")