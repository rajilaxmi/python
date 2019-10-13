# print whether the number is perfect number or not
def perfect(n):
	sum=0
	for x in range(1,n):
		if n%x==0:
			sum+=x
	return sum==n

print perfect(9)


'''
for 6:True
for 9:False
'''
