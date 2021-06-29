#import libraries
import random
import string

#function that gives us the password according to strength
def password_output(type):
    password = []
    if(type == 1):
        for i in range(6):
            password.append(random.choice(string.ascii_lowercase))

    elif(type == 2):
        for i in range(8):
            password.append(random.choice(string.ascii_letters + string.digits))

    elif(type == 3):
        for i in range(12):
            password.append(random.choice(string.ascii_letters + string.digits + string.punctuation ))
    password = ''.join(password)
    return password

def main():
    #prompt user to enter difficulty level of the password
    password_type = int(input("Please enter the password level: \n 1. Easy \n 2. Medium \n 3. Hard \n  "))
    #while loop to ensure that the user input is between 1-3
    while (password_type < 1 or password_type > 3):
        password_type = int(input("Please enter the password level between 1 and 3: \n 1. Easy \n 2. Medium \n 3. Hard \n"))
    #call the function password_output() and print its return statement
    print(password_output(password_type))

if __name__ == "__main__":
    main()