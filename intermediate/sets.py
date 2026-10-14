my_list=[1,2,2,3,3,3]
my_set={1,2,2,3,3,3}

print(my_list) #[1, 2, 2, 3, 3, 3]
print(my_set) #{1, 2, 3}
########################
print(nums[0])  # TypeError no indexing in sets
#########list to set
nums=[1,2,2,3,3]
nums1=set(nums)
#sets give unique values
print(nums1)  # {1, 2, 3}

##################
a = set()
b = {}

print(type(a))  # <class 'set'>
print(type(b))  # <class 'dict'>
##################
nums = {10, 20, 30}

nums.add(40)
print(nums)  # {10, 20, 30, 40}

nums.remove(20)
print(nums)  # {10, 30, 40}
nums.discard(100)  # No error if 100 is absent , remove() will give error if absent 
nums.pop()         # Removes and returns an arbitrary element
nums.clear()       # Removes every element

#############
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)
# {1, 2, 3, 4, 5, 6}
print(A & B)
# {3, 4}
print(A - B)
# {1, 2}
print(A ^ B)
# {1, 2, 5, 6} present in either but not in both 