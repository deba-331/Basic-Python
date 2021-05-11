print("Welcome to SBI ATM")
restart="Yes"
chance=3
balance=102.5
while chance >=0:
    pin=int(input("enter your 4 digit pin: "))
    if pin == (1234):
        print("you have entered the pin correctly\n")
        while restart not in ('n','No','no','NO'):
            print("Enter 1 to check balance")
            print("Enter 2 to withdrawl cash")
            print("Enter 3 to deposite cash")
            print("Enter 4 to return card")
            option = int(input("Enter the action you wish to perform from above options: "))
            if option == 1:
                print("Current Balance is", balance,'\n')
                restart= input("Is there any other action you wish to take then press 'Y'?")
                if restart in ('n','No','no','NO'):
                    print("Thank You! Have a nice day ahead")
                    break
            
            elif option == 2:
                withdrawal=float(input("Enter the amount to be withdrawn with in the options 10/30/50/60/80/100:"))
                if withdrawal in (10.0,30.0,50.0,60.0,80.0,100.0):
                    balance = balance-withdrawal
                    print("Your current balance is after withdrawal is",balance,"\n")
                    restart= input("Do you wish to try again?")
                    if restart in ('n','No','no','NO'):
                        print("Thank You! Have a nice day ahead")
                        break
                else:
                    print("Wrong input!! the amount should be with in the option 10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0")
                    restart= input("Do you wish to try again? Then press 'Y'")
                    if restart in ('n','No','no','NO'):
                        print("Thank You! Have a nice day ahead")
                        break
            elif option == 3:
                deposite = float(input("Please enter the amount you want to deposite: "))
                balance = balance + deposite
                print("Your current balance is after money deposite is",balance,"\n")
                restart= input("Is there any other action you wish to take then press 'Y'?")
                if restart in ('n','No','no','NO'):
                    print("Thank You! Have a nice day ahead")
                    break
            elif option == 4:
                print("Please do not forget to collect your card")
                restart= input("If there is any other action you wish to perform, please enter your card and press 'Y'")
                if restart in ('n','No','no','NO'):
                    print("Thank You! Have a nice day ahead")
                    break
    elif pin != (1234):
        print("The pin you enter is incorrect")
        chance-=1
        if chance == 0:
            print("you are out of chances")
            break
    

