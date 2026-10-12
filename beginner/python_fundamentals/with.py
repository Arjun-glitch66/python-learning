with open("sample.txt","r") as file:
    content=file.read()
    print(content)

#The file is automatically closed when execution leaves the with block, including when an exception occurs.

#"r"	Read
#"w"	Write, replacing existing content
#"a"	Append to existing content
#"x"	Create a new file; fail if it already exists