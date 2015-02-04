__author__ = 'georgev'
import math
if __name__=="__main__":
    sum=0
    for i in range(1,101):
        sum+=math.pow(i,2)
    print(sum-(math.pow((math.fsum(range(1,101))),2)))
