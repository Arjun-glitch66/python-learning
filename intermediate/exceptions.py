try:
    num=int(input("Enter a number: "))
    result=100/num
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:",result)
finally:
    print("Program finished")