n = input ("Введите целое число:")

while type (n) == str:
    try:
        n = int (n)
    except ValueError:
        print ("Неправильно ввели!")
        n = input ("Введите целое число: ")

print (n + 1)
