a = 2
b = 4.55
c = "hello"
print(a)
print(b)
print(c)
print (a, end = "___")
print (a,b,c)
print (a,b,c, sep = " : ")
s1 = (f"A:{a},B:{b:.1f},C:{c}")
print (s1)
print ("A:%10d,B:%.2f,C:%s" % (a,b,c))
print ("A:{0},B:{2},C:{1}" .format(a,b,c))