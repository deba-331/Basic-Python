travelling= input("Are you travelling. input Yes/No:\n").upper()

while travelling == 'YES':
    passenger=int(input("Please enter the traveler count:\n"))
    for i in range(1,passenger+1):
        name=input("Enter passenger name:\n")
        age=input("Enter Passenger age:\n")
        gender=input("Enter the gender of the passenger as (M/F):\n")
        print(name)
        print(age)
        print(gender)
        
    travelling=input("Wish to add someone else:")
