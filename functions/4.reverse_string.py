# reverse a string and print it
def reverse(str1):
	rev=""
	for c in range(len(str1)-1,-1,-1):
		rev=rev+str1[c]
	return rev
	
str1="1234abcd"
print reverse(str1)

'''
dcba4321
'''