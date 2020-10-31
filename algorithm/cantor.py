#カントールの対関数とその逆関数

def cantor(x,y):
    x = int(x)
    y = int(y)
    return (x+y)*(x+y+1)//2 + y

def i_cantor(n):
    n = int(n)
    s = 0
    i = 0
    buf = 0
    while buf<n:
        buf+=i+1
        if buf<=n:
            i+=1
            s=buf
    y = n-s
    x = i-y
    return x,y


print("Enter 2 integers for Cantor's pairing function F(x,y):")

x,y = input().split()

print(cantor(x,y))


print("\nEnter an integer for the inverse of F(x,y):")

n = input()

print(i_cantor(n))
