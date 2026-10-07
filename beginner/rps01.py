import random 
def getchoice():
    player_choice=input("Enter rock,paper or scissors: ")
    options=["rock","paper","scissors"]
    comp_choice=random.choice(options)
    choices={"player":player_choice,"computer":comp_choice}
    return choices 

#with no parameters 
res1=getchoice() #stores the choices made
def check():
    p=res1["player"]#access the dictioery value
    c=res1["computer"]
    message=f"you chose {p} and computer chose {c}"
    print(message)
    if p==c:
        return "Its a tie"
    if p=="rock":
        if c=="scissors":
            return"You win"
        else:
            return"Computer wins"

    if p=="paper":
        if c=="rock":
            return"You win"
        else:
            return"Computer wins"

    if p=="scissors":
        if c=="paper":
            return"You win"
        else:
            return"Computer wins"

res2=check()
print(res2)