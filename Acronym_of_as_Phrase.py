###Abbreviation of an entered phase

#saving the sentence as alist of all the words present
sentence=input("Enter a sentence").split()
print(sentence)
a=''
#iterating over the list
for i in sentence:
    #getting the first letetrs of each element and converting it into upper case
    a=a+(i[0]).upper()
print(a)


