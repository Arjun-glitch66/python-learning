from functools import reduce
numbers=[1,2,3,4,5]

res1=list(map(lambda x:x*x,numbers))
print(res1)

res2=list(filter(lambda x:x%2==0,numbers))
print(res2)

res3=reduce(lambda x,y:x+y,numbers)
print(res3)