import sys
import os
import time

def fizBuzzer(n):
    strBuild = ""
    if n % 3 == 0: strBuild += "Fizz"
    if n % 5 == 0: strBuild += "Buzz"
    if strBuild == "": strBuild = str(n)
    return strBuild

if __name__ == '__main__': 
    print(fizBuzzer(int(sys.argv[1])))


