#DESCRIPTION: Library to send notifications and error messages to a user.
#AUTHOR:      Zachary Collier
#DATE:        July 29th, 2024

def ErrorMessage(message):#Prints an error message with the desired message
    print("---!!!---")
    print(f"ERR: {message}")
    print("---!!!---")

def NotifMessage(message):#Prints a notification message with the desired message
    print("--!--")
    print(f"NOTICE: {message}")
    print("--!--")