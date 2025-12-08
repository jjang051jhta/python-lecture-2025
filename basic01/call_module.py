import mod01

print(mod01.add(10, 10))
print(mod01.sub(20, 10))

from mod01 import add, sub

print(add(20, 20))
print(sub(20, 20))

from mod01 import *

print(add(20, 20))
print(sub(20, 20))

from mod01 import Math

my_math = Math()
print(my_math.solve(5))

from mod01 import PI

print(PI)
