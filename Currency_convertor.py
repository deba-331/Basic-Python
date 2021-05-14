#Currency convertor

# fetching values from a file
with open("C:/Users/debanjan/Desktop/new_text_doc.txt") as file:
    lines=file.readlines()
    #print(lines)
    

currency_dict= {}
#Reading values from the list lines
for line in lines:
    #splitting the values to create nested lists
    values=line.split("\t")
    #assigning keys and values to the dictionary
    currency_dict[values[0]]= values[1]

amount_to_convert=int(input("Enter your amount to convert: ")) 
print("The available currencies are as below:\n")
#dictionary comprehension
[print(item) for item in currency_dict.keys()] 
currency=input("Please enter the currency type:") 
# converting the currency
convert=amount_to_convert*float(currency_dict[currency])
print(f"The amount {amount_to_convert} is equal to {convert} for the currency{currency}")
    

