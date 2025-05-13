import sys

def generateWaveOfStars(n):
    spaces = " " * (n//2)
    strBuild = ""

    for i in range(1, n+1, 2):
        upperStr = ""
        lowerStr = ""
        for j in range(i+1):
            print("j", j)
            upperStr += spaces[j:] + ("*" * j)+spaces[j:]+"\n"
            lowerStr = spaces[j:]+("*" * j)+spaces[j:]+"\n" + lowerStr
        
        strBuild += upperStr + lowerStr

    return strBuild



if __name__ == '__main__': 
    print(generateWaveOfStars( int(sys.argv[1])))


