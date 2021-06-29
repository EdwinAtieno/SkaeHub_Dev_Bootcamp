# create a function to split sentence then be able to get the length of the word
def Sentence(s):

    # split the sentence in separate words
    words = s.split()

    # check and get the length of the last word
    if len(words) == 0:
        return 0
    return len(words[-1])
def main():

    ursentence=Sentence(input("please enter your sentence "))
    # print the lenght of the last word in the input sentence
    print(ursentence)

if __name__ == '__main__':
   main()