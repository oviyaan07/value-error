try:
    num=int(input("enter a number: "))
    print(f"the entered number is {num}")
except ValueError as x:
    print("the exception is", x)