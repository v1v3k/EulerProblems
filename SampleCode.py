__author__ = 'georgev'


def ifelse():
    if True:
        print("true")
    elif True and False:
        print(123)
    elif True or False:
        print(123)
    else:
        print("hello")


def multiline():
    word = 'word'
    sentence = "This is a sentence."
    paragraph = """This is a paragraph. It is
    made up of multiple lines and sentences."""
    print(word, sentence, paragraph)


def userInput():
    var1 = input("Enter Something ");
    print(var1)


if __name__ == "__main__":
    print("Main Function started")
    ifelse()
    multiline()
    userInput()