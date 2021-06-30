import random
import string
def main():
    selected_option = int(input("Please enter the password difficulty level:"
                                " \n 1. Easy \n 2. Medium \n 3.Hard "
                                " \n 4. Very Hard \n "))
    while selected_option < 1 or selected_option > 4:
        selected_option = int(input("Please enter the password difficulty level between 1 and 4:"
                                    " \n 1. Easy \n 2. Medium \n 3.Hard "
                                    " \n 4. Very Hard \n "))
    def get_password(ranged):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(ranged))
        print("your password is: " + password)
    if selected_option == 1:
        get_password(6)
    elif selected_option == 2:
        get_password(9)
    elif selected_option == 3:
        get_password(11)
    else:
        get_password(12)
main()