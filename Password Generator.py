# Importing random for the int value and string for the output of the password
import random, string
from random import *

# Print disclaimer for user information
print ("DISCLAIMER! This program Will Not store or save these passwords! \nPlease Keep these in a secure place.\n")
print ("Generating Random Password \n")
characters = string.ascii_letters + string.punctuation  + string.digits

# Combine characters and display the password
# Version 0.1.2 - Updated to support longer passwords for strength and security. Password length is now between 12 and 20 characters of alphanumberic and special characters.
password =  "".join(choice(characters) for x in range(randint(12, 20)))
print (password)
