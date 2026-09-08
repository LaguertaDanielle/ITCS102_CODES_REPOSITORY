#conditional statements/control structures/selsection statement

import getpass

username = "Danielle"
password = "halaNahulog000"

u = input("Enter Username: ")
p = getpass.getpass("Enter Password: ")

if username == u and password == p :
	print("ACCESS GRANTED")
else :
	print("ACCESS DENIED")