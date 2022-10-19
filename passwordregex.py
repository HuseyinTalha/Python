import re
password = input("enter")
if(len(password)<7):
	print("password denied (len short)")
if(len(password)>31):
		print("password denied (len long)")
if not re.search('[A-Z]', password):
	print("password denied (capital)")
if not re.search('[a-z]', password):
	print("password denied (small)")
if not re.search('[0-9]', password):
	print("password denied (digits)")
if re.search('\s', password):
	print("password denied (space)")
if not re.search('[!#$+*?=/%]', password):
	print("password denied (symbol)")
if re.findall('password', password):
	print("password denied (password)")
else:
	print("password correct")
