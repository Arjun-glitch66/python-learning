from itertools import product
a=[1,2]
b=[3,4]
result=product(a,b)
print(list(result))#[(1,3),(1,4),(2,3),(2,4)]
####################
nums=[1,2]
res=product(nums,repeat=2) #creates duplicate of [1,2]
print(list(res))
############################
from itertools import permutations
letters=["A","B","C"]
res=permutations(letters,2)
print(list(res)) #[('A', 'B'), ('A', 'C'), ('B', 'A'),('B', 'C'), ('C', 'A'), ('C', 'B')]
#########################
from itertools import combinations
letters = ["A", "B", "C"]
res=combinations(letters,2)
print(list(res))#[('A', 'B'), ('A', 'C'), ('B', 'C')]
###############################
from itertools import combinations_with_replacement
nums = [1,2,3]
res=combinations_with_replacement(nums,2)
print(res) #[(1, 1), (1, 2), (1, 3),(2, 2), (2, 3), (3, 3)] ...2,1 or 3,1 or 3,2 not there its combination order matters but replacemnt allowed
######################
from itertools import accumulate
nums = [1,2,3,4]
result = list(accumulate(nums)) #accumulate (nums,operator.mul) will multiply [1, 2, 6, 24]
print(result) #[1, 3, 6, 10]
#################
from itertools import groupby 
nums = [1,1,2,2,2,3,1]
nums.sort() #groupby groups the concsecutive nums so the last 1 is formed as seperate group to avoid sort it first 
for key, group in groupby(nums):
    print(key, list(group))
    #1 [1, 1, 1]
    #2 [2, 2, 2]
    #3 [3]
#####################
from itertools import count
for i in count(2,3): #count() generates number from specified to infinity , here starts from 2 with step count 3 
    print(i) #2 5 8 11
    if i >= 11:
        break
######################
from itertools import cycle
colours=["r","g","b"]
c=cycle(colours)
for i in range(7):
    print(next(c)) # r g b r g b r