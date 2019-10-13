# convert an arrray to an array of machine values and return the bytes representation
from array import *
a=array('b',[91,98,99,49,50,51])
s=""
s=a.tobytes()
print(s)