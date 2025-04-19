def cube(num):
    return num*num*num

def three(num):
    if num %3 == 0:
        return cube(num)
    else:
        print("Not divisible by 3")

num = int(input("Enter a number to check:"))
print(three(num))