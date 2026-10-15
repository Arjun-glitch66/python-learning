#Collections
#in general
num=[1,2,2,3,1]
def count():
    freq={}
    for n in nums:
        if n in freq:
            freq[n]+=1
        else:
            freq[n]=1
    return freq
res=count()
print(res)
#using counter
from collections import Counter
num=[1,2,2,3,1]
freq=Counter(int)
print(freq) #Counter({2: 3, 1: 2, 3: 1})
print(freq[2]) #2
print(freq[3]) #1

print(freq.most_common(1)) #[(2, 3)] most common frequent
print(freq.most_common(2)) # top 2 most common frequent

#############################################
#in general
student=("Arjun", 20, 9.9)
print(student[0])
print(student[1])
#namedtuple
from collections import namedtuple
student=namedtuple("student",["name","age"])
s=student("Arjun",20)
print(s.name)#no need to remember the index position
print(s.age)
############################################
#in general dictionery will preserves insertion order but ordereddict have move to end and pop options
from collections import OrderedDict
data=OrderedDict()
data["a"] = 1
data["b"] = 2
data["c"] = 3
print(data) #OrderedDict([('a', 1), ('b', 2), ('c', 3)])
data.move_to_end("a") #by default its true , data.move_to_end("a",last=False) it moves to front...same for data.popitem("a",last=False)
print(data) #OrderedDict([('b', 2), ('c', 3), ('a', 1)])
#######################################
#deque
from collections import deque

dq = deque([10, 20, 30])
dq.append(40)
dq.appendleft(5)
print(dq) #deque([5, 10, 20, 30, 40])
dq.pop()
dq.popleft()
print(dq) #deque([10, 20, 30])

####################################
#in general
freq = {}
if "apple" in freq:
    freq["apple"] = freq["apple"] + 1
else:
    freq["apple"] = 1
print(freq)

#defaultdict
from collections import defaultdict
fruits = ["apple", "banana", "apple", "apple", "banana"]

freq = defaultdict(int) #here int() is not used becuase python calls it when needs default values and return 0

for fruit in fruits:
    freq[fruit] += 1 # if and else is not used ....internally for 1st iteration if apple is not there in freq={}, int() return 0 by default and increment happens so final answer is 1 

print(freq)

###############
from collections import defaultdict
groups = defaultdict(list) #by default it gives an empty list 
groups["fruits"].append("apple") # if the group fruit is not there in groups={}, it creates a empty list and then append continues
groups["fruits"].append("banana")
groups["vegetables"].append("carrot")

print(groups["fruits"])
print(groups["vegetables"])