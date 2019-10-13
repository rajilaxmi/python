#7. print each element from the list and its type
datalist=[1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class":"V", "section":"A"}]
for _ in datalist:
	print _, type(_)

'''
1452 <type 'int'>
11.23 <type 'float'>
...
[5, 12] <type 'list>
{'section':'A','class':'V'} <type 'dict'>
''' 