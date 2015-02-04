import math
__author__ = 'georgev'


def hcf(a,b):
    while(b>0):
        a= a%b
        if a==0:
            return b
        b=b%a
    return a

def lcm(a,b):
    num=[a,b]
    lcm_val= a*b/hcf(max(num),min(num))
    return lcm_val

if __name__=="__main__":
    lcm1=1
    for i in range(2,21):
        lcm1=lcm(lcm1,i)
        print (lcm1)
    print (lcm1)
