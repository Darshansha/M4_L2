def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorials for negative numbers are not defined")
else:
    print(f"The factorial of {num} is {factorial(num)}")