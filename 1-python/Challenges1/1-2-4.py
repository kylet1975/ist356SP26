# Challenge 1-2-4

#Write a program to create a shopping list. 

#loop until "quit" is entered.
#input a grocery item
#input a quantity
#save the item as the key in the dictionary and quantity as the value
#if the item is in the dictionary already, add the quantity to the existing value

shopping_list = {}
while True:
    item = input("Enter a grocery item (or 'quit' to exit): ")
    if item.lower() == "quit":
        break
    quantity = int(input("Enter the quantity: "))
    if item in shopping_list.key:   
            shopping_list[item] += quantity
    
    if item in shopping_list:
        shopping_list[item] += quantity
    else:
        shopping_list[item] = quantity
    
    print(f"Current shopping list: {shopping_list}")
















    #create a program that takes in numbers and letters 
    #and stores them in a dictionary 

    list = []
    dict = {}
    while True:
        entry = input("Enter an item (or 'quit' to exit): ")
        if entry.lower() == "quit":
            break
        list = int(input(f"Enter the quantity for {entry}: "))
        
        if entry in dict:
            dict[entry] += list
        else:
            dict[entry] = list
        
        print(f"Current list: {dict}")

