# execute a code using function
mycode='print("Hello World")'
code="""
def multipy(x,y):
	return x*y
print("the product of 2 and 3 is: %d"%multipy(2,3))
"""
exec(mycode)
exec(code)

"""
Hello World
the product of 2 and 3 is: 6
"""