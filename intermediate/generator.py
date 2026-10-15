#in general
num=list(range(1000)) #this creates a list with [1,2,3,.....]immediately which is not memeory efficient
for n in num:
    print(n)

#by generators we use yield so that it can yeild only when its required 
def numbers():
    for i in range(1000):
        yield i

nums = numbers()
print(next(nums)) #this creates 0 then pauses
print(next(nums)) #1 then pause
print(next(nums)) #2
