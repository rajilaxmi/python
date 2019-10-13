# to print the number of local variables present in the program
def abc():
	w=7
	e=3.4
	str1="hello"
	f=[8,6,5,4]
	
print(abc.__code__.co_nlocals)

'''
4
'''