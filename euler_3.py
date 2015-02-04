import math

__author__ = 'vivek'


def divisors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            if (checkIsPrime(i)):
                print(i)


def divisors1(num):
    largest = 1
    for i in range(1, math.floor(math.sqrt(num))):
        if num % i == 0:
            print(i, checkIsPrime(i), num / i, checkIsPrime(num / i))
            if checkIsPrime(i):
                largest = i
            if checkIsPrime(num / i) :
                largest = num / i
                break
    return largest


def checkIsPrime(num1):
    num = (math.floor(math.sqrt(num1)))
    for i in range(2, num + 1):

        if num1 % i == 0 and num1 != i:
            return False
    return True


if __name__ == "__main__":
    # divisors(10)
    divisors1(10)

    #print(i,checkIsPrime(i))
    print("-" * 10)
    print(600851475143)
    print(divisors1(600851475143))
    print("-" * 10)

