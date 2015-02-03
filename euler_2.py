__author__ = 'georgev'

sum=0
def fibo(a,b):
    global sum;
    print (b)
    if b%2 is 0:
        sum+=b
    if  a+b <4000000:
        fibo(b,a+b)
if __name__ == "__main__":
    fibo(1,1)
    print (sum)