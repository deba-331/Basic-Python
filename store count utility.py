# Python program to calculate the numbers
sum=0
while (True):
    
    price=input("Enter the price amount or press 'q' to quit:\n")
    if(price != 'q'):
        sum= sum+float(price)
        print(f"The total so far is {sum}")
    else:
        print(f"Your total bill is {sum}. Thank you ")
        break
    

