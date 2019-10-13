# check whether a string is a palindrome or not
def palin(str1):
	if str1[::1]==str1[::-1]:
		return True
	else:
		return False

str1="yes"
print palin(str1)


'''
for madam:True
for yes:False
'''