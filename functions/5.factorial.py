# prin the factorial of a number
def factorial(a):
	fact=1
	for i in range(a,0,-1):
		fact*=i
	return fact

a=4
print factorial(a)

'''
24
'''