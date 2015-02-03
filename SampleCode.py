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

def generalStuff():
    var1=10
    print (var1)

    #multi assign
    a=b=c=1
    a,b,c=1,2,"john"
    print(a,b,c)


def stringOp():
    str="Hello World!"
    print(str)
    print(str[0])
    print(str[2:5])#3to5
    print(str[2:])#3to all
    print(str[:3])#1to3



def listOp():
    list1=['abcd',786,2.23,'john',70.2]
    print (list1)
    tinylist1=[123,'john']
    print(tinylist1)
    print (list1[1:5])
    #index i and j-1 --> [i:j]
    print (list1+tinylist1)


'''
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list
'''
#read only list
def tupleOp():
    tuple1=('abcd',786,2.23,'john')





if __name__ == "__main__":
    print("Main Function started")
    #ifelse()
    #multiline()
    #userInput()
    #generalStuff()
    #stringOp()
    listOp()