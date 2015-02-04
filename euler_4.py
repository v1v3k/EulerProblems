__author__ = 'georgev'


def largestPal():
    arr = []
    print("--")


    for i in reversed(range(100,999)):
        for j in reversed(range(100,999)):
            mul = i * j
            if (isPal(mul)):
                arr.append(mul)
    for i in arr:
        print(i)
    print (max(arr))
def isPal(num):
    return str(num) == str(num)[::-1]


if __name__ == "__main__":
    largestPal()
    print(isPal(99999))
