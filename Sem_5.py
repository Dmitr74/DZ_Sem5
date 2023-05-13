""" Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8  """


""" def exponent(A, B):
    exp = 1
    for i in range(1, B + 1):
        exp = exp * A
    return exp


A = int(input("Please, insert any number: "))
B = int(input("Please, insert the exponent of this number: "))
C = exponent(A, B)
print(C) """


""" Задача6. Дана строка (возможно пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB.
Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28. И сгенерирует ошибку, если на вход
пришла невалидная строка.   """


def counting(new_list):
    count = 1
    list = []
    for i in range(0, len(new_list)-1):
        if new_list[i] == new_list[i+1]:
            count = count + 1
        else:
            list.append(new_list[i])
            if count > 1:
                list.append(count)
                count = 1
            else:
                count = 1
    if  new_list[-1] == new_list[-2]:
        list.append(new_list[-2])
        list.append(count)
    else:
        list.append(new_list[-1]) 
    return list


new_list = str(input("Please, insert the combination of latin letters: "))
new_set = set(new_list)
latin_set = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
res = new_set.difference(latin_set)
if len(res) == 0: 
    print("Inserted symbols are right! Forward!")
    print(counting(new_list))
else:
    print("Sorry, you are was wrong! Try again...")