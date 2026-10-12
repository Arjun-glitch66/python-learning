try:
    num=int(input("Enter a number: "))
    result=100/num
except (ValueError,ZeroDivisionError):
    print("Invalid input")
else:
    print(result)
finally:
    print("Program completed")