a = [2.3, 8, 'hi']
b = [2.3, 'hi', 8]

print (a == b)

c = {2.3, 8, 'hi'}
d = {2.3, 'hi', 8}

print (c ==d)

s = ['a', 'b', 'c', 'd']
s[0] = 555
print (s)

####dir(list)
####s.append(999)



from random import randint

c = []
i = 0
while i < 5:
    c. append(randint(0, 100))
    i += 1
print (c)