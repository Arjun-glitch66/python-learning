from enum import Enum

class Difficulty(Enum):
    Easy=1
    Medium=2
    Hard=3
num=int(input("Enter 1/2/3: "))
if num==Difficulty.Easy.value:
    print("Easy mode")
elif num==Difficulty.Medium.value:
    print("Medium mode")
else:
    print("Hard mode")
print("Sample testing 1")
print(Difficulty.Easy)
print("SAMPLE TESTING 2")
print(Difficulty.Medium.value)