import random 
def getchoice():
    player_choice=input("Enter rock,paper or scissors: ")
    options=["rock","paper","scissors"]
    comp_choice=random.choice(options)
    choices={"player":player_choice,"computer":comp_choice}
    return choices 

def check(player,computer):
    if player==computer:
        return "its a tie"
    message = f"You choose {player}, computer chose {computer}" #else
    return message

res1=getchoice()
res2=check(res1["player"],res1["computer"])
print(res2)

#if no parameter means 

#res1 = getchoice()
#def check():
 #   player = res1["player"]
  #  computer = res1["computer"]

#    if player == computer:
 #       return "It's a tie"

#    message = f"You chose {player}, computer chose {computer}"

 #   return message


#res2 = check()

#print(res2)