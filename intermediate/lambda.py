
check= lambda n: "Even" if n%2==0 else "Odd"
print(check(4))
print(check(5))

#############
student=[("Arjun",90),("Ram",60)]
res=sorted(student,key=lambda s:s[1]) # s=("Arjun",90) so here the key tells teh lambda to look at index 1 which is the mark then uses sorted () to sort
print(res)