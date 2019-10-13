# to generate a multi-dimensional array 
row_num=int(input("Enter the row number:"))
col_num=int(input("Enter the column number:"))
list1=[[0 for col in range(col_num)] for row in range(row_num)]
#print list1
for row in range(row_num):
	for col in range(col_num):
		list1[row][col]=row*col

print list1