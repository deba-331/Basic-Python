from math import *
n=int(input("enter the range of the counting"))
for a in range(1,n+1):
    for b in range(a,n):
        c = a**2 + b**2
        c1=int(sqrt(c))
        if (c == c1**2):
            print(a,b,c1)
        

