import random
import sys
import binascii
from datetime import datetime
random.seed(datetime.now().timestamp())


result=""
for i in range(0,255):
    randval = random.randint(0,sys.maxsize)
    randstr=str(randval)
    result+=randstr

print(result)

