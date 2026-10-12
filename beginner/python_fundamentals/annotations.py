def greet(name:str)->str: #parameter type is string and it returns a string 
    return "Hello "+name

print(greet("Arjun"))




def add(a:int,b:int)->int:
    return a+b

print(add("Hello ","Arjun"))

#It still works because Python doesn't enforce the annotated types at runtime by default.
#Annotations help developers understand code and allow tools such as type checkers to detect potential mistakes.