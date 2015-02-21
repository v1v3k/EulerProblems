__author__ = 'georgev'

import math
def main():
    sum=1000;
    for a in range(1,math.floor(1000/3)):
        for b in range(a+1,math.floor(1000/2)):
            c=1000-a-b
            if(a*a +b*b == c*c):
                print(a,b,c)
                print(a*b*c)


if __name__=="__main__":
    main()


