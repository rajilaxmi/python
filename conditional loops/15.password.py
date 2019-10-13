# to check the validation of a string
import re
pass1=raw_input("Enter a password:")
bool1=re.search("[a-zA-Z]",pass1)
bool2=re.search("[0-9]",pass1)
bool3=re.search("[$@#]",pass1)
len1=len(pass1)
if (len1>6 and len<16) or (bool1 or bool2 or bool3):
		print "Password is valid."
else:
	print "password is invalid"