RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
print("="*25)
print(GREEN+" password gernator"+RESET)
import random
import string 
length=int(input(BLUE+"  Enter password length:"+RESET))
characters=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(length):
    password +=random.choice(characters)
print(YELLOW+"password"+RESET,password)