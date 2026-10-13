from random import random

a = 0.1
b = 0.9
i = 0

while i < 10_000_00:
    n = random()
    if n < a:
        a = n
    elif n > b:
        b = n
    i +=1

print("%.16f" % a)
print (b)

c = random() * 10
d = random() * (10 - 6)
f = random() * (10 - 6) + 6
g = random() * (2 - -2) - 2
print("c = %.16f" % c)
print("d = %.16f" % d)
print("f = %.16f" % f)
print("g = %.16f" % g)

o = round(random() * (10 - 6) + 6) # можем получить  10

print("%.16f" % o)

j = int(random() * (10 - 6) + 6) # не можем получить  10

print("%.16f" % j)