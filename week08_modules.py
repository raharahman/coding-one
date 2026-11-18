#generate list of random numbers
#then multiply together
#import random
from random import randint
import week06_multiply
import math

nums = []

for i in range(0, 10):
    nums.append(randint(0,10))

print(nums)
print(week06_multiply.mult(nums))



