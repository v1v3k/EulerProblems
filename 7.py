__author__ = 'georgev'
import math

def prime100():
    primecount=0
    num=1
    while(primecount<10001):
        num=num+1
        if isprime(num):
            primecount=primecount+1
            print(num)

    print (num)

def isprime(num):
    for i in range (2,math.floor(math.sqrt(num))+1):
        if(num%i==0 and num!=i):
            return False
    return True

print (prime100())
