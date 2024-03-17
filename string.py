# # 1. Write a function to swap the first and last characters in a string.
# # RU: Напишите функцию, чтобы поменять местами первый и последний символы в строке.
# def swap_first_last(string):   # поменять_первый_последный
#     return string[-1] + string[1:-1] + string[0]
# q = swap_first_last("Feruz")
# # print(q)


# # 2. Write a function to reverse a string.
# # RU: Напишите функцию, чтобы перевернуть строку.
# # allow => wolla
# def reverse_string(string):  # перевернуть_строку
#      return string[::-1]
# w = reverse_string("feruz").capitalize()
# # print(w)


# # # 3. Write a function to remove the nth index character from a n onempty string.
# # # RU: Напишите функцию, чтобы удалить символ с индексом n из непустой строки.
# def remove_nth_index(string, index):  # удалить_с_индексом
#     if len(string)<index or index<0:
#         print("Incorrect logic")
#         return
#     return string[:index] + string[index+1:]
# e = remove_nth_index("Welcome", 2)
# # print(e)


# # 4. Write a function to remove the characters which have odd index values of a given string.
# # RU: Напишите функцию, чтобы удалить символы, которые имеют нечетные индексы заданной строки.
# def remove_odd_index(string):  # удалить_нечетные_индексы
#     return string[::2]
# r = remove_odd_index("число")
# # print(r)


# # 5. Write a Python script that takes input from the user and displays
# # that input back in upper and lower cases.
# # RU: Напишите скрипт Python, который принимает ввод от пользователя и
# # отображает этот ввод в верхнем и нижнем регистрах.
# def upper_lower(string):  # верхний_нижний
#     return string.upper(), string.lower()
# t = upper_lower("значение")
# # print(t)


# # # 6. Write a function to find the second most frequent character in a given string.
# # # RU: Напишите функцию, чтобы найти второй наиболее часто встречающийся символ в данной строке.
# # # второй_наиболее_часто_встречающийся
# def second_most_frequent(string):
#     dict = {}
#     for i in string:
#         dict[i] = string.count(i)
#     return sorted(dict.items(), key=lambda x: x[1])[-2][0]
# y = second_most_frequent("словарь")
# # print(y)


# # 7. Write a function to convert a given string into a list of integers.
# # RU: Напишите функцию, чтобы преобразовать заданную строку в список целых чисел.
# def convert_to_list(string):  # преобразовать_в_список
#     return [int(i) for i in string]
# u = convert_to_list("12345")
# # print(u)


# # 8. Write a function to check if a given string is a palindrome.
# # RU: Напишите функцию, чтобы проверить, является ли заданная строка палиндромом.
# def is_palindrome(string):  # является_палиндромом
#     return string == string[::-1]
# i = is_palindrome("madam")
# # print(i)
# # 12321  => polindrome
# # 12345  => NOT polindrome
# # madam  => polindrome
# # qwert  => NOT polindrome


# # 9. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# # If the string length is less than 2, return the empty string instead.
# # RU: Напишите программу на Python, чтобы получить строку, состоящую из первых 2 и последних 2 символов заданной строки.
# # Если длина строки меньше 2, вместо этого верните пустую строку.
# def first_last_two(string):  # первые_2_последние_2
#     if len(string) < 2:
#         return ""
#     return string[:2] + string[-2:]
# o = first_last_two("Паралелепипед")
# # print(o)


# # 10. Write a Python program to get a string from a given string where all occurrences of its first char
# # have been changed to '$', except the first char itself.
# # RU: Напишите программу на Python, чтобы получить строку из заданной строки, где все вхождения ее первого символа
# # были заменены на '$', кроме самого первого символа.

# # INPUT:   =>  "This is test text"
# # OUTPUT:  =>  "This is $es$ $ex$"
# # изменить_первый_символ
# def change_first_char(symbol: str = "$") -> str:
#     string = input("Напишите любое слово: ")
#     first = string[0]
#     return first + string[1:].replace(first.lower(), symbol)
# p = change_first_char()
# # print(p)


# # 11. Write a Python program to get a single string from two given strings, separated by a space and
# # swap the first two characters of each string.
# # RU: Напишите программу на Python, чтобы получить одну строку из двух заданных строк, разделенных пробелом и
# # поменять местами первые два символа каждой строки.
# # "Wello  Helcome"
# # ---------------
# def swap_first_two(str1,str2):
#    return str2[:2]+str1[2:] + " " + str1[:2]+str2[2:]
# a = swap_first_two("Hello","City")
# # print(a)


# # 12. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string
# # already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# # RU: Напишите программу на Python, чтобы добавить 'ing' в конец заданной строки (длина должна быть не менее 3).
# # Если заданная строка уже заканчивается на 'ing', вместо этого добавьте 'ly'.
# # Если длина строки заданной строки меньше 3, оставьте ее без изменений.
# # def add_ing(string):  # добавить_ing
# #     if len(string) < 3:
# #         return string
# #     if string[-3:] == 'ing':
# #         return string + 'ly'
# #     return string + 'ing'
# def add_ing(string):
#     if len(string) <3:
#         return string
#     if string[-3:] == "ing":
#         return string + "ly"
#     return string + "ing"
# s = add_ing("substring")
# # print(s)


# # 13. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# # If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# # RU: Напишите программу на Python, чтобы найти первое появление подстрок «не» и «плохо» в заданной строке.
# # Если «не» следует за «плохо», замените всю подстроку «не» ... «плохо» на «хорошо». Вернуть полученную строку.
# def replace_not_poor(string):  # заменить_не_плохо
#     not_index = string.find('not')
#     poor_index = string.find('poor')
#     if not_index != -1 and poor_index != -1 and poor_index > not_index:
#         return string.replace(string[not_index:poor_index+4], 'good')
#     else:
#         return string
# d = replace_not_poor("This is not poor")
# # print(d)


# # 14. Write a Python function to create an HTML string with tags around the word(s)
# # RU: Напишите функцию Python для создания HTML-строки с тегами вокруг слова (слов).
# def add_tags(tag, string):  # добавить_теги
#     return f'<{tag}>{string}</{tag}>'
# result = add_tags('b', 'This is text')  # Пример: тег 'b' для жирного текста
# # print(result)


# # 15. Write a Python function to insert a string in the middle of a string.
# # RU: Напишите функцию Python для вставки строки посередине строки.
# # вставить_строку_посередине
# def insert_string_middle(string, string_to_insert):
#     return string[:len(string)//2] + string_to_insert + string[len(string)//2:]
# g = insert_string_middle("midles","x")
# # print(g)


# # 16. Write a Python function to get a string made of 4 copies of the last two characters of a specified string
# # RU: Напишите функцию Python, чтобы получить строку, состоящую из 4 копий последних двух символов заданной строки
# def last_two(string):  # последние_два
#     return string[-2:] * 4
# h = last_two("last")
# # print(h)


# # 17. Write a Python function to get a string made of the first three characters of a specified string.
# # If the length of the string is less than 3, return the original string.
# # RU: Напишите функцию Python, чтобы получить строку, состоящую из первых трех символов заданной строки.
# # Если длина строки меньше 3, вернуть исходную строку.
# def first_three(string):  # первые_три
#     if len(string) < 3:
#         return string
#     return string[:3]
# j = first_three("first")
# # print(j)


# # 18. Write a Python function to get the first half of a specified string of even length.
# # RU: Напишите функцию Python, чтобы получить первую половину заданной строки четной длины.
# def first_half_even(string):  # первая_половина_четная
#     if len(string) % 2 == 0:
#         return string[:len(string)//2]
#     return string
# k = first_half_even("результаты")
# # print(k)


# # 19. Write a Python program to concatenate two strings and return the result.
# # If the length of the strings are not same then remove the characters from the longer string.
# # RU: Напишите программу на Python для объединения двух строк и верните результат. Если длины строк не одинаковы,
# # то удалите символы из более длинной строки.
# def concat_strings(str1, str2):  # объединить_строки
#     if len(str1) == len(str2):
#         return str1 + str2
#     elif len(str1) > len(str2):
#         return str1[:len(str2)] + str2
#     else:
#         return str1 + str2[:len(str1)]
# l = concat_strings("test","tes")
# # print(l)


# # 20. Write a Python function to convert a given string to all uppercase if it contains
# # at least 2 uppercase characters in the first 4 characters.
# # RU: Напишите функцию Python для преобразования заданной строки в верхний регистр, если она содержит
# # не менее 2 заглавных символов в первых 4 символах.
# def convert_upper(string):  # преобразовать_в_верхний_регистр
#     if sum(1 for char in string[:4] if char.isupper()) >= 2:
#         return string.upper()
#     return string
# z = convert_upper("APple") 
# # print(z)


# # 21. Write a Python program to remove a newline in Python.
# # RU: Напишите программу на Python, чтобы удалить перевод строки в Python.
# def remove_newline(string):  # удалить_перевод_строки
#     return string.replace('\n','')
# x = remove_newline("Hello\nWorld\n")
# # print(x)


# # 22. Write a Python program to remove existing indentation from all of the lines in a given text.
# # RU: Напишите программу на Python для удаления существующего отступа из всех строк в заданном тексте.
# def remove_indentation(string):  # удалить_отступ
#     return string.strip()
# c = remove_indentation("   test   ")
# # print(c)


# # 23. Write a Python program to count and display the vowels of a given text.
# # RU: Напишите программу Python, чтобы подсчитать и отобразить гласные заданного текста.
# def count_vowels(string):  # подсчитать_гласные
#     vowles = 'aeiou'
#     return sum(1 for char in string if char in vowles)
# v = count_vowels("aeiow")
# # print(v)


# # 24. Swapkeys
# def swap_cases(string):  # поменять_регистр
#     return string.swapcase()
# b = swap_cases("CASES")
# # print(b)


# # ====================================================================================================
# # 25. Write a function in Python to check duplicate letters.
# # It must accept a string, i.e., a sentence. The function should return
# # True if the sentence has any word with duplicate letters, else return False.
# # RU: Напишите функцию на Python для проверки повторяющихся букв.
# # Он должен принимать строку, то есть предложение. Функция должна возвращать
# # True, если в предложении есть слово с повторяющимися буквами, иначе возвращать False.
# # проверить_повторяющиеся_буквы
# def check_duplicate_letters(string) -> bool:
#     for letter in string:
#         if string.count(letter) > 1:
#             return True
#     return False
# n = check_duplicate_letters("test")
# # print(n)


# def check_duplicate_letters(string):
#     for letter in string:
#         if string.count(letter) > 1:
#             return True
#     return False
# n = check_duplicate_letters("text")

#     # return bool([letter for letter in string if string.count(letter) > 1])


# # ====================================================================================================
# # 26. Write a function that takes a sentence as argument, then takes last word's first letter and
# # repeats 5 times in the beginning of the sentence and at the end.
# # RU: Напишите функцию, которая принимает предложение в качестве аргумента, затем берет первую букву
# # последнего слова и повторяет 5 раз в начале предложения и в конце.
# def repeat_first_l_of_last_word(sentence):
#     first_l = sentence.split(" ")[-1][0]
#     return first_l*5 + sentence + first_l*5
#     # last_w_first_l = sentence[sentence.rindex(" "):][1]
#     # return sentence.center(len(sentence)+10, last_w_first_l)
# m = repeat_first_l_of_last_word("Hello world")
# # print(m)


# # def repeat_first_l_of_last_word(sentence):
# #     first_l = sentence.split(" ")[-1][0]
# #     return first_l*5 + sentence + first_l*5
# # m = repeat_first_l_of_last_word("Hello City")
# # print(m)

# # "wwwwwHello worldwwwww"
# # ====================================================================================================


# # 26. Напишите код на Python для создания переводчика азбуки Морзе.
# # Вы можете взять строку с буквенно-цифровыми символами в нижнем или верхнем регистре.
# # Строка также может содержать любые специальные символы, являющиеся частью кода Морзе.
# # Специальные символы могут включать запятые, двоеточия, апострофы, восклицательные знаки,
# # точки и вопросительные знаки. Код должен возвращать код Морзе, эквивалентный строке.
# # def morse_code(string):
# #     morse_code_dict = {
# #         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
# #         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
# #         'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
# #         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
# #         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
# #         'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
# #         '4': '....-', '5': '.....', '6': '-....', '7': '--...',
# #         '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
# #         '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
# #         '(': '-.--.', ')': '-.--.-'
# #     }
# #     return ' '.join(morse_code_dict[i.upper()] for i in string)
# # morse = morse_code("Hello, World!")
# # print(morse)
# # ====================================================================================================


# # 27. Написать функцию для определения 13-й пятницы. Функция может принимать два параметра:
# # и оба будут числами. Первым параметром будет число, обозначающее месяц,
# #, а второй будет четырехзначным годом. Ваша функция должна анализировать параметры,
# # и он должен возвращать True, если в месяце есть пятница с 13-м числом, иначе возвращается False.
# # def detect_13th_friday(month, year):
# #     import datetime
# #     return datetime.datetime(year, month, 13).weekday() == 4
# # friday = detect_13th_friday(3,2020)
# # print(friday)


# # ====================================================================================================



# # 28. Написать функцию для поиска доменного имени по IP-адресу. Функция примет
# # IP-адрес, сделайте запрос DNS и верните имя домена, которое соответствует этому IP-адресу, пока
# # с использованием записей PTR DNS. Вы можете импортировать библиотеку сокетов Python.
# # def find_domain_name(ip_address):
# #     import socket
# #     return socket.gethostbyaddr(ip_address)[0]
# # random_ip = "198.71.233.138"  # www.w3schools.com
# # print(find_domain_name(random_ip))


# # ====================================================================================================
# # 29. Напишите на Python функцию для преобразования десятичной дроби в шестнадцатеричную. Он должен принимать строку ASCII.
# # символов в качестве входных данных. Функция должна возвращать значение каждого символа в виде шестнадцатеричной строки.
# # Вам необходимо разделить каждый байт пробелом и вернуть все альфа-шестнадцатеричные символы в нижнем регистре.
# # def convert_to_hex(string):
# #     return ' '.join(hex(ord(char))[2:] for char in string)
# # hex = convert_to_hex("text")
# # print(hex)


# # ====================================================================================================
# # 30. Напишите функцию на Python для анализа строки так, чтобы она принимала параметр — закодированную строку.
# # Эта закодированная строка будет содержать имя, фамилию и идентификатор. Вы можете разделить значения
# # в строке любым количеством нулей. Идентификатор не будет содержать нулей. Функция должна вернуть
# # словарь Python со значениями имени, фамилии и идентификатора. Например, если ввод будет
# # "John000Doe000123". Тогда функция должна вернуть:
# # { "first_name": "John", "last_name": "Doe", "id": "123" }
# # def encoded_string(string):
# #     first_name, last_name, id = string.split("000") 
# #     return {"first_name": first_name, "last_name": last_name, "id": id}
# # encoded = encoded_string("Alex000Harrison000154")
# # print(encoded)


# # ====================================================================================================
# # 31. Напишите код на Python, чтобы узнать, является ли данная строка S допустимым регулярным выражением или нет.
# # def is_valid_regex(string):
# #     import re
# #     try:
# #         re.compile(string)
# #         return True
# #     except re.error:
# #         return False
# # valid = is_valid_regex("validation")
# # print(valid)


# # ====================================================================================================

# # 32. Create a function that takes a text and repeats the middle
# # letter three times
# # RU: Создайте функцию, которая принимает текст и повторяет
# # среднюю букву три раза
# # Welcome   =>   Welcccome
# # def repeat_middle(sentence):
# #     middle = len(sentence) // 2  # 3.5 => 3
# #     start = sentence[:middle]
# #     end = sentence[middle+1:]
# #     print(start + sentence[middle]*3 + end)
# # repeat = repeat_middle("text")


# # =======================================================================================c=============

# # 33. Create a function that repeats first and last half of the text n times
# # RU: Создайте функцию, которая повторяет первую и вторую половину текста n раз
# # "Welcome"  =>  "WelWelWelWelcomecomecomecome"


# # def repeat_half_text(text, n):
# #     half_length = len(text) // 2
# #     first_half = text[:half_length]
# #     second_half = text[half_length:]
# #     repeated_text = (first_half * n) + (second_half * n)
# #     return repeated_text

# # Пример использования
# # result = repeat_half_text("Welcome", 3)
# # print(result)  # Вывод: "WelWelWelWelcomecomecomecome"

# # =======================================================================================c=============






# # 1. Напишите программу Python для печати следующей строки в определенном формате (см. выходные данные).
# # Пример строки: «Мерцай, мерцай, маленькая звездочка, Как мне интересно, кто ты! Высоко над миром,
# # Как алмаз в небе. Мерцай, мерцай, маленькая звездочка, Как мне интересно, кто ты»

# # def print_formatted_string(sentence):
#     # Разделяем фразы по запятым и убираем пробелы в начале и конце каждой фразы
#     # phrases = sentence.split(",")
#     # phrases = [phrase.strip() for phrase in phrases]

#     # Определенный формат печати с пробелами перед каждой фразой
#     # for i, phrase in enumerate(phrases):
#     #     if i == 0: 
#     #         print(phrase)
#     #     else:
#     #         print("    " + phrase)

# # Пример использования
# # example_string = "Мерцай, маленькая звездочка!"
# # print_formatted_string(example_string)


# # =======================================================================================c=============


# # 2. Напишите программу на Python, чтобы узнать, какую версию Python вы используете.
# # import sys  
# # print("Python version")
# # print(sys.version)
# # print("Version info.")
# # print(sys.version_info)


# # 3. Напишите программу на Python для отображения текущей даты и времени.Текущая дата и время
# # import datetime
# # now = datetime.datetime.now()
# # print("Current date and time : ")
# # print(now.strftime("%Y-%m-%d %H:%M:%S"))


# # =======================================================================================c=============


# # 4. Напишите программу на Python, которая вычисляет площадь круга на основе радиуса, введенного пользователем. Пример вывода: г = 1,1 Площадь = 3,8013271108436504
# # from math import pi
# # r = float(input("Input the radius of the circle : "))
# # area = pi * r ** 2
# # print("The area of the circle with radius " + str(r) + " is: " + str(area))


# # ====================================================================================================


# # 5. Напишите программу на Python, которая принимает имя и фамилию пользователя
# #  и печатает их в обратном порядке с пробелом между ними.
# # Prompt the user to input their first name and store it in the 'fname' variable

# # name = input("Ваше Имя : ")
# # surname = input("Ваша Фамилия : ")
# # print("Hello  " + name + " " + surname)


# # ====================================================================================================


# # 6. Напишите программу на Python, которая принимает от пользователя последовательность чисел,
# # разделенных запятыми, и генерирует список и кортеж этих чисел.Примеры данных: 3, 5, 7, 23
# # Выход :
# # Список: ['3', '5', '7', '23']
# # Кортеж: («3», «5», «7», «23»)

# # values = input("Input some comma-separated numbers: ")
# # list = values.split(",")
# # tuple = tuple(list)
# # print('List : ', list)
# # print('Tuple : ', tuple)


# # ====================================================================================================


# # 7. Напишите программу на Python, которая принимает имя файла от пользователя
# #  и печатает расширение файла.
# # Пример имени файла: abc.java
# # Выход: Java


# # filename = input("Input the Filename: ")
# # f_extns = filename.split(".")
# # print("The extension of the file is : " + repr(f_extns[-1]))


# # ====================================================================================================


# # 8. Напишите программу на Python для отображения первого и последнего цветов
# #  из следующего списка.
# # color_list = ["Красный", "Зеленый", "Белый", "Черный"]
# # exit1 = color_list[-1]
# # exit2 = color_list[0]
# # result = exit2 + " " + exit1
# # print(result)


# # ====================================================================================================


# # 9. Напишите программу на Python для отображения расписания экзаменов.
# #  (извлеките дату из экзамена_st_date).
# # экзамен_st_date = (11, 12, 2014 г.)
# # Пример вывода: Экзамен начнется с: 12.11.2014.


# # ====================================================================================================


# # 10. Напишите программу на Python, которая принимает целое число (n) 
# # и вычисляет значение n+nn+nnn.
# # Выборочное значение n равно 5.
# # Ожидаемый результат : 615

# # a = int(input("Input an integer: "))

# # n1 = int("%s" % a)          
# # n2 = int("%s%s" % (a, a))   
# # n3 = int("%s%s%s" % (a, a, a))  

# # print(n1 + n2 + n3)


# # ====================================================================================================


# # 11. Напишите программу Python для печати документов (синтаксис, описание и т. д.) встроенных функций Python.
# # Пример функции: abs()
# # Ожидаемый результат :
# # абс(число) -> число
# # Возвращает абсолютное значение аргумента.

# # print(abs.__doc__)


# # ====================================================================================================


# # 12. Напишите программу на Python, которая печатает календарь на заданный месяц и год.
# # Примечание. Используйте модуль «календарь».

# import calendar

# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# # print(calendar.month(y, m))


# # ====================================================================================================


# # 13. Напишите программу Python для печати следующего «здесь документа».
# # Пример строки:
# # строка, которую вам «не нужно» экранировать
# # Этот
# # это ....... многострочный
# # строка heredoc --------> пример


# # ====================================================================================================


# # 14. Напишите программу на Python для расчета количества дней между двумя датами.
# # Примеры дат: (2014, 7, 2), (2014, 7, 11)
# # Ожидаемый результат: 9 дней

# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# # print(delta.days)


# # ====================================================================================================


# # 15. Напишите программу на Python, чтобы получить объем сферы радиуса шесть.

# pi = 3.1415926535897931
# r = 6.0
# V = 4.0/3.0 * pi * r**3
# # print('The volume of the sphere is: ', V)


# # ====================================================================================================


# # 16. Напишите программу на Python для вычисления разницы между заданным числом и 17.
# # Если число больше 17, верните удвоенную абсолютную разницу.


# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2
# # print(difference(22))
# # print(difference(14))


# # ====================================================================================================


# # 7. Напишите программу на Python, чтобы проверить, находится ли число в пределах 100, 1000 или 2000.


# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# # print(near_thousand(1000))
# # print(near_thousand(900))
# # print(near_thousand(800))
# # print(near_thousand(2200))


# # ====================================================================================================


# # 18. Напишите программу на Python для вычисления суммы трех заданных чисел.
# #  Если значения равны, верните тройную их сумму.

# def sum_thrice(x, y, z):
#     sum = x + y + z

#     if x == y == z:
#         sum = sum * 3
#     return sum
# # print(sum_thrice(1, 2, 3))
# # print(sum_thrice(3, 3, 3))


# # ====================================================================================================


# # 19. Напишите программу на Python, чтобы получить вновь сгенерированную строку из заданной строки,
# # в начале которой добавлено «Is». Верните строку без изменений, если данная строка уже начинается с «Is».

# def new_string(text):
#     if len(text) >= 2 and text[:2] == "Is":
#         return text
#     else:
#         return "Is" + text
# # print(new_string("Array"))
# # print(new_string("IsEmpty"))


# # ====================================================================================================


# # 20. Напишите программу на Python, которая возвращает строку, 
# # состоящую из n (неотрицательных целых) копий заданной строки.

# def larger_string(text, n):
#     result = ""
#     for i in range(n):
#         result = result + text
#     return result
# # print(larger_string('abc', 2))
# # print(larger_string('.py', 3))


# # ====================================================================================================





# # ====================================================================================================


# # 21. Напишите программу на Python, которая определяет, является ли заданное число (принятое от пользователя)
# #  четным или нечетным, и печатает соответствующее сообщение пользователю.


# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     # print("This is an odd number.")
# # else:
#     # print("This is an even number.")


# # ====================================================================================================


# # 22. Напишите программу на Python для подсчета числа 4 в заданном списке.
    

# # def list_count_4(nums):
#     # count = 0
#     # for num in nums:
#     #     if num == 4:
#     #     count = count + 1
#     # return count
# # print(list_count_4([1, 4, 6, 7, 4]))  
# # print(list_count_4([1, 4, 6, 4, 7, 4])) 


# # ====================================================================================================


# # 23. Напишите программу на Python, чтобы получить n (неотрицательное целое число)
# # копий первых двух символов заданной строки. Вернуть n копий всей строки, если длина меньше 2.


# def substring_copy(text, n):
#   flen = 2
#   if flen > len(text):
#     flen = len(text)
#   substr = text[:flen]
#   result = ""
#   for i in range(n):
#     result = result + substr
#   return result
# # print(substring_copy('abcdef', 2)) 
# # print(substring_copy('p', 3))  


# # ====================================================================================================


# # 24. Напишите программу на Python, проверяющую, является ли пропущенная буква гласной или нет.

# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# # print(is_vowel('c'))  
# # print(is_vowel('e')) 

# # ====================================================================================================


# # 25. Напишите программу на Python, которая проверяет, содержится ли указанное значение в группе значений.
# # Тестовые данные:
# # 3 -> [1, 5, 8, 3]: верно
# # -1 -> [1, 5, 8, 3]: ложь

# def is_group_member(group_data, n):
#     for value in group_data:
#         if n == value:
#             return True  
#     return False  

# # print(is_group_member([1, 5, 8, 3], 3)) 
# # print(is_group_member([5, 8, 3], -1))   


# # ====================================================================================================


# # 26. Напишите программу на Python для создания гистограммы из заданного списка целых чисел.

# def histogram(items):
#     for n in items:
#         output = ''
#         times = n    

#         while times > 0:
#             output += '*'
#             times = times - 1 
        
#         print(output)

# # histogram([2, 3, 6, 5])


# # ====================================================================================================


# # 27. Напишите программу на Python, которая объединяет все элементы списка в строку и возвращает ее.

# x = list(1,5,15,2)
# j = x.join()
# print(j)