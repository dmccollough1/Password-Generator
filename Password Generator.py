import string
from random import *
print ("\n")
print ("DISCLAIMER! This program Will Not store or save these passwords! \nPlease Keep these in a secure place.\n")
print ("Generating Random Password \n")
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print (password)