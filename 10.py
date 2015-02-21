__author__ = 'georgev'
import math

def primeSum():
    primecount=0
    num=1
    sum=0
    while(num<2000000):
        num=num+1
        if isprime(num):
            primecount=primecount+1
            sum=sum+num

    print (sum)

def isprime(num):
    for i in range (2,math.floor(math.sqrt(num))+1):
        if(num%i==0 and num!=i):
            return False
    return True

primeSum()