import random
import string
import sys
# This function uses the string module to make random letters and numbers
def strong_list():
    return "".join(random.choice(string.ascii_letters + string.digits) for x in range(8))
# This function creates a random list of special characters
def special_char():
    return "".join(random.choice("?!&$*%@") for x in range(2))
def main():
    # combine both special characters and mixed
    specials = special_char()
    mixed = strong_list()
    password = (mixed + specials)
    #initialize the password into a list
    passwordarray = []
    passwordarray[:10] = password
    # prompt user to select difficulty
    difficulty = str(input("choose your password to be weak, medium or strong?"))
    # filter out the type of password according to user choice
    if difficulty.lower() == "weak":
        shufflelist = random.sample(passwordarray, len(passwordarray[0:4]))
        userpassword = "".join(shufflelist)
        print (userpassword)
        # check user's satisfaction
        happy = str(input("Best password?  Y/N?"))
        if happy.upper() == "Y":
            sys.exit()
        elif happy.upper() == "N":
            main()
    # condition check for medium
    elif difficulty.lower() == "medium":
        shufflelist = random.sample(passwordarray, len(passwordarray[0:6]))
        userpassword = "".join(shufflelist)
        print(userpassword)
        #check user's satisfaction
        happy = str(input("Best password?  Y/N?"))
        if happy.upper() == "Y":
            sys.exit()
        elif happy.upper() == "N":
            main()
    # condition check for medium
    elif difficulty.lower() == "strong":
        shufflelist = random.sample(passwordarray, len(passwordarray))
        userpassword = "".join(shufflelist)
        print(userpassword)
        # check user's satisfaction
        happy = str(input("Best password?  Y/N?"))
        if happy.upper() == "Y":
            sys.exit()
        elif happy.upper() == "N":
            main()
    # incase does not select
    else:
        print ("Please try again, restarting generator")
        main()
#calling the main function
main()