a=[1,2] #list is mutable we can put any datatye in list 
a.append([3,4])
print(a)       # [1,2,[3,4]]

b=[1,2]
b.extend([3,4])
print(b)       # [1,2,3,4]

############

nums=[10,20,30,40,50]

nums.remove(30) #throws error if not available
print(nums)       # [10,20,40,50]

x=nums.pop() # pop removes and returns if nothing is mentioned removes the last element
print(x)          # 50
print(nums)       # [10,20,40]


del nums[0]
print(nums)       # [20,40]

nums.clear()
print(nums)       # []

#################
nums=[4,1,5,2,3]

nums.sort()
print(nums)             # [1,2,3,4,5]

nums.sort(reverse=True)
print(nums)             # [5,4,3,2,1]

nums.reverse()
print(nums)             # [1,2,3,4,5]

#############
a=[10,20,30]

b=a
c=a.copy()
d=a[:] #or a[::]

a[0]=99

print(b)    # [99,20,30]
print(c)    # [10,20,30]
print(d)    # [10,20,30]