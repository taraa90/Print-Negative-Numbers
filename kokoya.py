minimum = int(input("Enter the Minimum Number = "))
maximum = int(input("Enter the Maximum Number = "))

print("\nAll Negative Numbers from {0} and {1}".format(minimum, maximum)) 
for num in range(minimum, maximum + 1):
    if num < 0:
        print(num, end = '   ')
