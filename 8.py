#Напишите программу для поиска наибольшего общего делителя (НОД) двух чисел 
# с помощью алгоритма Евклида. Программа должна принимать два целых числа и возвращать их НОД.

a = int(input("Введите число:"))
b = int(input("Введите число:"))

while a!=0 and b!=0:
    if a>b:
        a = a%b
    else:
        b = b%a
print(a+b)



   #Гуглила сам алгоритм, остальное писала сама