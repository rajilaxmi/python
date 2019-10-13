# print the number of digits and alphabets found in a string
str1=raw_input("Enter a string:")
d=0
a=0
for _ in str1:
	if _.isdigit():
		d+=1
	elif _.isalpha():
		a+=1
	else:
		pass
print "Numbers: ",d
print "Letters: ",a

'''
Enter a string: w3resource
Numbers: 1
Letters: 9
'''

