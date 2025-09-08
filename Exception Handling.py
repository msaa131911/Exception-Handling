try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    Result= num1/num2
    print(result)
except (ZeroDivisionError, ValueError):
    print("Invalid input")
finally:
    print("This will always execute")