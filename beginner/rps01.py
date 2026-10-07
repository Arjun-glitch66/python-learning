import random 
def getchoice():
    player_choice=input("Enter rock,paper or scissors: ")
    options=["rock","paper","scissors"]
    comp_choice=random.choice(options)
    choices={"player":player_choice,"computer":comp_choice}
    return choices 

choices1=getchoice()
print(choices1)
print("Append testing")
print("Before")
op=["rock","paper","scissors"]
print(op)
print("After")
op.append("stone")
print(op)