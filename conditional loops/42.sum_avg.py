#to print the sum and average of n integers 
count=0
sum=0
num=1
avg=0
while num!=0:
	num=int(input("Enter a number: "))
	sum+=num
	count+=1
avg=sum/(count-1)
if count==0:
	print("Enter some more number:");
else:
	print("The sum and average is %d %d"%(sum, avg))
	
	
'''
Enter a numer: 25
Enter a number: 25
Enter a number: 0
The sum and average is 50 25
'''
