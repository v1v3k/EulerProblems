__author__ = 'georgev'



def sumOfMultiple35(n):
    i=3
    sum=0
    while i<n:
        if(i%3==0) or (i%5==0):
            print (i)
            sum+=i
        i+=1

    return sum


if __name__ == "__main__":
    print("Main Function started")
    n=1000
    print(sumOfMultiple35(n))