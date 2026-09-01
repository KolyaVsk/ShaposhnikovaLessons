a = int(input("Делимое: "))
b = int(input("Делитель: "))

if b!=0:
    c = a / b
    print (f"Частное: {c:.2f}")
else:
    print ("Zero division")
print ("End")