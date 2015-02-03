__author__ = 'georgev'



def sumOfMultiple35(n):
    i=3
    sum=0

    for i in range(0,1000):
        if(i%3 is 0) or (i%5 is 0):
            sum+=i

    return sum

def sumof(num,range):
    n=int(range/num)
    print (n)

    sum=int(num*(n*(n+1))/2)
    print (sum)
    return sum

if __name__ == "__main__":
    print("Main Function started")
    n=999
    print(sumOfMultiple35(n))
    value = sumof(3,n)+sumof(5,n)-sumof(15,n)
    print(value)