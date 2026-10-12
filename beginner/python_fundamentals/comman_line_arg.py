import sys
name=sys.argv[1]
print("hI",name)
#in terminal type python command_line_arg.py Arjun
#so Arjun is the index 1



#example
#python main.py Arjun 20
#Output:
#['main.py', 'Arjun', '20'] main.py is the file name but its also cosidered as index 0
#sys.argv[0]	main.py
#sys.argv[1]	Arjun
#sys.argv[2]	20