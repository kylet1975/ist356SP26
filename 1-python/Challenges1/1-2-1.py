#Challenge 1-2-1

valid_password = "secret"

for i in range(5):
    pw  = input("Enter Password:")
    if pw == valid_password:
        print("access granted")
        break 
else:
    print("too many failed attempts")
# Stores the correct password in a variable
# Runs a loop 5 times, allowing 5 password attempts. 
# Prompts the user to enter a password.
    #If the password matches "secret":
        #Prints "access granted"
        #break exits the loop 
    #If the password is incorrect:
        
# The loop continues to the next attempt.
# Should the user fail to enter the correct password in 5 attempts, the loop ends.
# Print "too many failed attempts" if the user did not enter the

