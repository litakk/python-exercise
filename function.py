
# def == define == Создать

# def name() arg1, *args, 
# *kwergs - создает на ходу аргументы 




# def test(a:int, b:int) -> int:
#     """This is test text"""
#     return a + b


# r = test(1,2)
# print("Result: ", r)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def test(a:int, b:int, c:int) -> int:
#     """This is test text"""
#     return b + c 


# r = test(1,2, 3)
# print("Result: ", r)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def test(a:int, b:int, c:int, *d) -> int:
#     """This is test text"""
#     return a + b + c + sum(d) 


# r = test(1, 1, 1)
# print("Result: ", r)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def test(a:int, b:int, c:int, *d) -> int: # *d - rest - всё остольное
#     """This is test text"""
#     return a + b + c + sum(d) 


# r = test(1, 1, 1, 1, 1, 1)
# print("Result: ", r)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def test(a:int, b:int, c:int, *d, e:int=10) -> int:
#     """This is test text"""
#     return a + b + c + sum(d) + e


# r = test(1, 1, 1, e=5)
# print("Result: ", r)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def test(a:int, b:int, c:int, *d, e:int=10) -> int:
#     """This is test text"""
#     return a + b + c + sum(d) + e


# r = test(1, 1, 1, 1, 1, 1, 1, 1, e=10)
# print("Result: ", r)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def test(a:int, b:int, c:int, *d, e:int=10) -> int:
#     """This is test text"""
#     return a + b + c + sum(d) + e


# r = test(1, 1, 1, 1, 1, 1, 1, 1)
# print("Result: ", r)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def test(a:int, *b, c:int=10) -> int:
#     """This is test text"""
#     return a + b[0]

# r = test("1", "5")
# print("Result: ", r)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def test(a:int, *b:list[int], c:int=10) -> int:
#     """This is test text"""
#     return a + sum(b) + c

# r = test(1, 5, 5)
# print("Result: ", r)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# LAMBDA
# func_name = lambda arg1, arg2: arg1 + arg2
# print(func_name(1,2)) 

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# PASS - не выдаст ошибку 
# def show_message(*children):
#     pass

# NotImplementedError() 
# example
# if 2 == 2:
#   pass
# else:
#   pass
# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# main = input("Введите сообщение")
# удалить середину и первую и последнюю букву сделать заглавными

# def function(str):
#     q = input("Сообщение: ")
#     middle = len(str) //2
#     return str[:middle] + str[middle+1:]
# print("Welcome")

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# Create a function that asks a text from user
# By getting text from user, delete the middle letter
# of the text and make first-last letters uppercase
# RU: Создайте функцию, которая запрашивает текст у пользователя
# Получая текст от пользователя, удалите среднюю букву
# текста и сделайте первую и последнюю буквы заглавными
# def text_manipulation():
#     x = input("Enter something: ")
#     MIDDLE = len(x) // 2
#     return x[0].upper() + x[1:MIDDLE] + x[MIDDLE+1:-1] + x[-1].upper()

# r = text_manipulation()
# print(r)


# def function(str):
#     MIDDLE = len(str) // 2
#     return str[0].upper() + str[1:MIDDLE] + str[MIDDLE+1:-1] + str[-1].upper()
# print(function("helko"))

# # Определить функцию с именем function с параметром str
# функция защиты (str):
# Находим средний индекс входной строки
# MIDDLE = len(str) // 2
# Возвращаем новую строку, образованную:
# Использование заглавной буквы первого символа входной строки
# Объединение символов от второго символа до среднего индекса (не включающее)
# Объединение символов от среднего индекса плюс один индекс до 8-го
#  (при условии, что длина строки не менее 8)
# Наконец, объединение с последним символом входной строки, написанным с заглавной буквы
# return str[0].upper() + str[1:MIDDLE] + str[MIDDLE+1:8] + str[8].upper()

# Выводим результат вызова функции с вводом "приветики"
# print(function("приветики"))

# В этом коде функция принимает строку в качестве входных данных, 
# находит средний индекс строки, затем создает измененную строку,
#  записывая первый и последний символы с заглавной буквы 
# и сохраняя символы между первым и последним неизмененными.
#  Однако логика нарезки, похоже, адаптирована для конкретной длины строки,
#  равной 8, и может не работать должным образом для строк разной длины.

# Конечно! Давайте разберем код, который манипулирует входной строкой, 
# чтобы удалить ее среднюю часть.

# Выражение str[1:MIDDLE] принимает фрагмент входной строки, 
# начиная со второго символа (индекс 1) до среднего индекса, но не включая его.
#  Это эффективно удаляет среднюю часть строки, сохраняя при этом первый символ.


# Аналогично, выражение str[MIDDLE+1:8] принимает фрагмент входной строки, 
# начиная с символа, следующего за средним индексом, до восьмого индекса. 
# Предполагается, что длина входной строки составляет не менее 8 символов. 
# Эта часть эффективно удаляет оставшуюся среднюю часть струны.


# Следовательно, когда вы объединяете str[1:MIDDLE] + str[MIDDLE+1:8] вместе, 
# это эффективно удаляет среднюю часть строки.


# Таким образом, результатом этой манипуляции является новая строка, 
# в которой первый и последний символы написаны с заглавной буквы,
#  а средняя часть удалена.


# "" '' '''  '''



# import collections
# num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
# result = sum(collections.Counter(num).values())
# print(result)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# Проверьте перед тем как вызвать функцию еще раз 

# def count_down(number:int) -> None:
#     """Будет выводить числа от number до 0"""
#     print(number)

#     if number > 0:
#         return count_down(number - 1)
# count_down(10)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def count_up(max_number:int, counter:int=1) -> None:
#     """Будет вводить числа от 1 до max_number"""
#     print("⭐" * counter)

#     if counter < max_number:
#         return count_up(max_number, counter+1)
    
# count_up(10)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def count_up(max_number:int, counter:int=1) -> None:
#     """Будет вводить числа от 1 до max_number"""
#     print(counter)

#     if counter < max_number:
#         return count_up(max_number, counter+1)

# count_up(10)

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# Factorial - 5 - 5*4*3*2*1 = 120


# def factorial(number:int) -> int:
#     if number == 1:
#         return 1
    
#     return number * factorial(number - 1)
# print(factorial(5))

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# def fib(max:int) -> list[int]:
#  a, b = 0, 1
# while a < 100:
#     print(a, end=', ')
#     a, b = b, a + b

# - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  - - -  

# 1 in [1,2,3]

# def elements():
#     list = [1,2,3,4,5]
#     new_list = []

#     for i in list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list

# r = elements()
# print("Результат всего задания Алишер Ака))) :" + str(r))

# def te():
#     i = input("Введите сообщение: ")



# def count_vowels(string):
#     qqq = 'aeiou'
#     return "".join([i for i in string if i not in qqq])
# v = count_vowels("q w e r t y u i o p")
# print(v)

