# function that takes two list and returns True if they have at least one common member
def compare_list(a, b):
	for x in a:
		for y in b:
			if x==y:
				return True
			else:
				return False

a=[1,3,5,7]
b=[2,4,6,8]
print compare_list(a,b)

'''
a=[1,3,5,7] b=[1,3,5,7]
True
a=[1,3,5,7] b=[1,4,6,8]
True
a=[1,3,5,7] b=[2,4,6,8]
False
'''
