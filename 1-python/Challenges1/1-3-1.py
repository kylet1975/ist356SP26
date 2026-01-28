### Challenge 1-3-1

#Write a function called `average` which takes a list of numbers as input then outputs
# the average of the numbers sum / count

#Call your function with an arbitrary list of numbers you create.

def average(numbers):

    if len(numbers) == 0:  

        return 0

    return sum(numbers) / len(numbers)

user_input = input("Enter numbers separated by spaces: ")



numbers_list = [float(num) for num in user_input.split()]



print("your average numbers is:", average(numbers_list))




def get_average_from_user() -> float:
    numbers = []

    while True:
        user_input = input("Enter a number (or type 'stop' to finish): ")

        if user_input.lower() == "stop":
            return sum(numbers) / len(numbers)

        numbers.append(float(user_input))


result = get_average_from_user()
print("your average is:", result)