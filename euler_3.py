__author__ = 'vivek'

def divisors(num):
    for i in range(1, num+1):
       if num%i==0:
           if(checkIsPrime(i)):
               print (i)

def checkIsPrime(i):
    print ("do something")



if __name__=="__main__":
    divisors(10)
    print (range(1,10))