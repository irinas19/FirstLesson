#Написать функцию is_prime , принимающую 1 аргумент — число от 0 до 1000, и возвращающую 
# True, если оно простое, и False - иначе. (функцию с определением простоты числа - написать самостоятельно)

def is_prime(n):
    if n == 0 or n == 1:
        return False
    i= 2
    while i < n:
        if n % i != 0:
            i +=1
            continue 
        else:
            return False 
    return True 
print(is_prime(int(input("Введите число от 0 до 1000: "))))

#Гуглила