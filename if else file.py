# if we are asked to print odd no's-weird,even no's range from 6-20 weird and 2_5 not weird and even no's greater than 20 are not weird.
import math
import os
import random
import re
import sys
n =int(input().strip())
if n%2 !=0:
    print("Wierd")
elif n%2 ==0 and n>2 and n<=5:
    print("Not Weird")
elif n%2 ==0 and n>=6 and n<=20:
    print("Weird")
elif n%2 ==0 and n>20:
    print("Not Weird") 