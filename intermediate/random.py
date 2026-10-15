import random
num = random.random()
print(num)
##################
import random
num = random.randint(1,6) #includes the end points 
print(num)
####################
random.randrange(2,11,2) #not included with step count of 2
#######################
import random
fruits = ["apple","banana","mango"]
print(random.choice(fruits))
###################
import random
nums = [1,2,3,4,5]
random.shuffle(nums) #[3, 1, 5, 2, 4]
print(nums)
# nums = random.shuffle(nums) shuffle() returns None so nums become None
