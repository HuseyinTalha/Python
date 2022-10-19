import re
password = input("enter")
if (len(password)<7):
	print("password denied (len short)")
elif (len(password)>31):
		print("password denied (len long)")
elif  not re.search('[A-Z]', password):
	print("password denied (capital)")
elif not re.search('[a-z]', password):
	print("password denied (small)")
elif not re.search('[0-9]', password):
	print("password denied (digits)")
elif re.search('\s', password):
	print("password denied (space)")
elif not re.search('[!#$+*?=/%]', password):
	print("password denied (symbol)")
elif re.findall('password', password):
	print("password denied (password)")
else:
	print("password correct")
