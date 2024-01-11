import string
import random
from string import Formatter

user_login = "".join(random.sample ((string.ascii_lowercase), 6))
user_password = "".join(random.sample ((string.ascii_letters + string.digits), 8))

print(user_login)
print(user_password)

my_string = "We have been\n to welcome\n\n back OLD friends, \n\n\n and to make new ones"

print(string.capwords(my_string))

