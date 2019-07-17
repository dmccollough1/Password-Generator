# Importing random for the int value and string for the output of the password
import random, string
from random import *

# Print disclaimer for user information
print ("DISCLAIMER! This program Will Not store or save these passwords! \nPlease Keep these in a secure place.\n")
characters = string.ascii_letters + string.punctuation  + string.digits

# Combine characters and display the password
password =  "".join(choice(characters) for x in range(randint(12, 20)))
print ("Your password is: ")
print (password)