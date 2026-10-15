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