# to coount the number of uppercase and lowercase alphabet in a string
def counting(str1):
	d={"upper":0,"lower":0}
	for c in str1:
		if c.isupper():
			d["upper"]+=1
		elif c.islower():
			d["lower"]+=1
		else:
			pass
	print "Number of uppercase alphabets: %d"%d["upper"]
	print "Number of lowercase alphabets: %d"%d["lower"]
	

str1="The Quick Brown Fox"
counting(str1)


'''
Number of uppercase alphabets: 4
Number of lowercase alphabets: 12
'''
