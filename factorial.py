def factorial(num):
    fact=1
    if num<0:
        print("the number should be positive")
    elif num==1:
        print("the value is 1")
    else:
        for i in range(1,num+1):
            fact*=i
        print(fact)
            
number=int(input("enter the number:\n"))
factorial(number)

