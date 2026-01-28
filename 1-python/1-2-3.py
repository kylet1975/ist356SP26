# Challenge 1-2-3

#Write a sentinel controlled loop to input a color until "quit" is entered.
#add each color to a list only when the color is not already in the list
#prredint the list each time in the loop

colors = []
while True:
    color = input("Enter a color (or 'quit' to exit): ") 
    if color.lower() == "quit":
        
        break
    if color.lower() not in colors:
        colors.append(color.lower())
    print(colors)    