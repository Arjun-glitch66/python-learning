#STINGS ARE IMMUTABLE
word = "Python"
word[0] = "J"  # TypeError
##########CORRECT method
word = "Python"
word = "J" + word[1:]

print(word)  # Jython
########################

word = "Python"

print(word[0:3])  # Pyt
print(word[2:])   # thon
print(word[:4])   # Pyth
print(word[::2])  # Pto
print(word[::-1]) # nohtyP

################
sentence = "I love Python"

words = sentence.split() #by default detects white space and put comma

print(words) #['I', 'love', 'Python']

#@#############
data = "apple,banana,orange"

fruits = data.split(",")

print(fruits) #['apple', 'banana', 'orange']
################
letters = ["P", "y", "t", "h", "o", "n"]

print("-".join(letters))#P-y-t-h-o-n