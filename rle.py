#!/usr/bin/python

#run length encoding

def encode(mystring):

	count = 1
	res = ""
	for i, char in enumerate(mystring):
		#char = mystring[i]
		try:
			if char == mystring[i+1]:
				count = count + 1
			else:
				if count == 1:
					res += str(char)
				else:
					res += str(count)
					res += str(char)

				count = 1
		except IndexError:
			if count == 1:	
				res += str(char)
			else:
				res += str(count)
				res += str(char)
	
	return res

def decode(mystring):

	res = ""
	count = 1
	for char in mystring:
		if is_number(char):
			count = int(char)
		else:
			res += str(count*char)
			count = 1

	return res

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
