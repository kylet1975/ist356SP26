positive_count = 0
negative_count = 0
count = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break
    if num != 0:
        count += 1
    elif num > 0:
        positive_count += 1
    else:
        negative_count += 1

print("Positive numbers entered:", positive_count)
print("Negative numbers entered:", negative_count)
print("Total numbers entered:", count)