import random
password_length=int(input("enter the length of the password:\n"))
#inputting the characters to be in the password
characters_of_password='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456790@#$%^&*!+_-'".,<>"
#joinning the random samples list to get an output as a string
password="".join(random.sample(characters_of_password,password_length))
print(password)
