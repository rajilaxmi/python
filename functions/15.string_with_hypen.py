#display the string using hypens instead of white spaces
def hypen(str1):
	list1=str1.split(" ")
	list1.sort()
	return('-'.join(list1))

str1="The quick fox went into the bushes"
print hypen(str1)
