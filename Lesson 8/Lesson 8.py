#try:
 #   a = int(input("Делимое: "))
  #  b = int(input("Делитель: "))
#except ValueError:
#    print("Необходимо ввести число")
try:
    a = int(input("Делимое: "))
    b = int(input("Делитель: "))
    c = a / b
    print (f"Частное: {c:.2f}")
except ZeroDivisionError:
    print ("Zero division")
# except NameError:
#    print("Нет значений переменных")
except (ValueError, NameError):
    print("Надо вводить числа")
else:
    print ("Не было ошибок")
finally:                                      # Cрабатывает всегда
    print ("Выполнюсь в любом случае")