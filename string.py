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


# ====================================================================================================

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


# =======================================================================================c=============

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

# =======================================================================================c=============






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


# =======================================================================================c=============


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


# ======================================================================================c=============


# # 4. Напишите программу на Python, которая вычисляет площадь круга на основе радиуса, введенного пользователем. Пример вывода: г = 1,1 Площадь = 3,8013271108436504
# # from math import pi
# # r = float(input("Input the radius of the circle : "))
# # area = pi * r ** 2
# # print("The area of the circle with radius " + str(r) + " is: " + str(area))


# ====================================================================================================


# # 5. Напишите программу на Python, которая принимает имя и фамилию пользователя
# #  и печатает их в обратном порядке с пробелом между ними.
# # Prompt the user to input their first name and store it in the 'fname' variable

# # name = input("Ваше Имя : ")
# # surname = input("Ваша Фамилия : ")
# # print("Hello  " + name + " " + surname)


# ====================================================================================================


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


#====================================================================================================


# # 7. Напишите программу на Python, которая принимает имя файла от пользователя
# #  и печатает расширение файла.
# # Пример имени файла: abc.java
# # Выход: Java


# # filename = input("Input the Filename: ")
# # f_extns = filename.split(".")
# # print("The extension of the file is : " + repr(f_extns[-1]))


# ====================================================================================================


# # 8. Напишите программу на Python для отображения первого и последнего цветов
# #  из следующего списка.
# # color_list = ["Красный", "Зеленый", "Белый", "Черный"]
# # exit1 = color_list[-1]
# # exit2 = color_list[0]
# # result = exit2 + " " + exit1
# # print(result)


# ====================================================================================================


# # 9. Напишите программу на Python для отображения расписания экзаменов.
# #  (извлеките дату из экзамена_st_date).
# # экзамен_st_date = (11, 12, 2014 г.)
# # Пример вывода: Экзамен начнется с: 12.11.2014.


# ====================================================================================================


# # 10. Напишите программу на Python, которая принимает целое число (n) 
# # и вычисляет значение n+nn+nnn.
# # Выборочное значение n равно 5.
# # Ожидаемый результат : 615

# # a = int(input("Input an integer: "))

# # n1 = int("%s" % a)          
# # n2 = int("%s%s" % (a, a))   
# # n3 = int("%s%s%s" % (a, a, a))  

# # print(n1 + n2 + n3)


# ====================================================================================================


# # 11. Напишите программу Python для печати документов (синтаксис, описание и т. д.) встроенных функций Python.
# # Пример функции: abs()
# # Ожидаемый результат :
# # абс(число) -> число
# # Возвращает абсолютное значение аргумента.

# # print(abs.__doc__)


# ===================================================================================================


# # 12. Напишите программу на Python, которая печатает календарь на заданный месяц и год.
# # Примечание. Используйте модуль «календарь».

# import calendar

# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# # print(calendar.month(y, m))


# ====================================================================================================


# # 13. Напишите программу Python для печати следующего «здесь документа».
# # Пример строки:
# # строка, которую вам «не нужно» экранировать
# # Этот
# # это ....... многострочный
# # строка heredoc --------> пример


# ====================================================================================================


# # 14. Напишите программу на Python для расчета количества дней между двумя датами.
# # Примеры дат: (2014, 7, 2), (2014, 7, 11)
# # Ожидаемый результат: 9 дней

# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# # print(delta.days)


# ====================================================================================================


# # 15. Напишите программу на Python, чтобы получить объем сферы радиуса шесть.

# pi = 3.1415926535897931
# r = 6.0
# V = 4.0/3.0 * pi * r**3
# # print('The volume of the sphere is: ', V)


# # ====================================================================================================


# 16. Напишите программу на Python для вычисления разницы между заданным числом и 17.
# # Если число больше 17, верните удвоенную абсолютную разницу.


# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2
# # print(difference(22))
# # print(difference(14))


# # ====================================================================================================


# 7. Напишите программу на Python, чтобы проверить, находится ли число в пределах 100, 1000 или 2000.


# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# # print(near_thousand(1000))
# # print(near_thousand(900))
# # print(near_thousand(800))
# # print(near_thousand(2200))


# ====================================================================================================


# # 18. Напишите программу на Python для вычисления суммы трех заданных чисел.
# #  Если значения равны, верните тройную их сумму.

# def sum_thrice(x, y, z):
#     sum = x + y + z

#     if x == y == z:
#         sum = sum * 3
#     return sum
# # print(sum_thrice(1, 2, 3))
# # print(sum_thrice(3, 3, 3))


# ====================================================================================================


# # 19. Напишите программу на Python, чтобы получить вновь сгенерированную строку из заданной строки,
# # в начале которой добавлено «Is». Верните строку без изменений, если данная строка уже начинается с «Is».

# def new_string(text):
#     if len(text) >= 2 and text[:2] == "Is":
#         return text
#     else:
#         return "Is" + text
# # print(new_string("Array"))
# # print(new_string("IsEmpty"))


# ====================================================================================================


# # 20. Напишите программу на Python, которая возвращает строку, 
# # состоящую из n (неотрицательных целых) копий заданной строки.

# def larger_string(text, n):
#     result = ""
#     for i in range(n):
#         result = result + text
#     return result
# # print(larger_string('abc', 2))
# # print(larger_string('.py', 3))


# ====================================================================================================





# ====================================================================================================


# # 21. Напишите программу на Python, которая определяет, является ли заданное число (принятое от пользователя)
# #  четным или нечетным, и печатает соответствующее сообщение пользователю.


# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     # print("This is an odd number.")
# # else:
#     # print("This is an even number.")


# ====================================================================================================


# # 22. Напишите программу на Python для подсчета числа 4 в заданном списке.
    

# # def list_count_4(nums):
#     # count = 0
#     # for num in nums:
#     #     if num == 4:
#     #     count = count + 1
#     # return count
# # print(list_count_4([1, 4, 6, 7, 4]))  
# # print(list_count_4([1, 4, 6, 4, 7, 4])) 


# ====================================================================================================


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


# ====================================================================================================


# # 24. Напишите программу на Python, проверяющую, является ли пропущенная буква гласной или нет.

# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# # print(is_vowel('c'))  
# # print(is_vowel('e')) 

# ====================================================================================================


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


# ====================================================================================================


# 26. Напишите программу на Python для создания гистограммы из заданного списка целых чисел.

# def histogram(items):
#     for n in items:
#         output = ''
#         times = n    

#         while times > 0:
#             output += '*'
#             times = times - 1 
        
#         print(output)

# # histogram([2, 3, 6, 5])


# ====================================================================================================


# # 27. Напишите программу на Python, которая объединяет все элементы списка в строку и возвращает ее.

# def concatenate_list_data(lst):
#     result = '' 
#     for element in lst:
#         result += str(element) 

#     return result  
# print(concatenate_list_data([1, 5, 12, 2]))


# ====================================================================================================


# 28. Напишите программу на Python, которая будет печатать все четные
#  числа из заданного списка чисел в одном и том же порядке и прекращать
# печать всех чисел после 237 в последовательности.


# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
# ]
# for x in numbers:
#     if x == 237:
#         print(x) 
#         break 
#     elif x % 2 == 0:
#         print(x)  


# ====================================================================================================


# 29. Напишите программу на Python, которая печатает все цвета из color_list_1,
#  которых нет в color_list_2.
# Тестовые данные:
# color_list_1 = set(["Белый", "Черный", "Красный"])
# color_list_2 = set(["Красный", "Зеленый"])
# Ожидаемый результат:
# {'Черно-белый'}


# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print("Original set elements:")
# print(color_list_1)
# print(color_list_2)

# print("\nDifference of color_list_1 and color_list_2:")
# print(color_list_1.difference(color_list_2))

# print("\nDifference of color_list_2 and color_list_1:")
# print(color_list_2.difference(color_list_1))


#  ====================================================================================================


# 30. Напишите программу на Python, которая будет принимать основание и 
# высоту треугольника и вычислять его площадь.

# b = int(input("Input the base : "))
# h = int(input("Input the height : "))

# area = b * h / 2

# print("area = ", area)


# ====================================================================================================


# 31. Напишите программу на Python, которая вычисляет наибольший общий делитель
#  (НОД) двух положительных целых чисел.

# def gcd(x, y):
#     gcd = 1
    
#     if x % y == 0:
#         return y
    
#     for k in range(int(y / 2), 0, -1):
#         # Check if both x and y are divisible by k.
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break
    
#     return gcd

# print("GCD of 12 & 17 =", gcd(12, 17))
# print("GCD of 4 & 6 =", gcd(4, 6))
# print("GCD of 336 & 360 =", gcd(336, 360))

# ====================================================================================================


# 32. Напишите программу на Python, чтобы найти наименьшее общее кратное (НОК) двух положительных целых чисел.\

# def lcm(x, y):
#     if x > y:
#         z = x
#     else:
#         z = y
    
#     while True:
#         if (z % x == 0) and (z % y == 0):
#             lcm = z
#             break
#         z += 1
    
#     return lcm

# print(lcm(4, 6))
# print(lcm(15, 17))


#  ====================================================================================================


# 33. Напишите программу на Python для суммирования трех заданных целых чисел.
#  Однако если два значения равны, сумма будет равна нулю.

# def sum_three(x, y, z):
#     if x == y or y == z or x == z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum

# print(sum_three(2, 1, 2))
# print(sum_three(3, 2, 2))
# print(sum_three(2, 2, 2))


#  ====================================================================================================


# 34. Напишите программу на Python для суммирования двух заданных целых чисел. 
# Однако, если сумма находится между 15 и 20, она вернет 20.


# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum

# print(sum(10, 6))
# print(sum(10, 2))
# print(sum(10, 12))


 # ====================================================================================================

# 35. Напишите программу на Python, которая возвращает true, если два заданных 
# целочисленных значения равны или их сумма или разница равна 5.


# def test_number5(x, y):
#     if x == y or abs(x - y) == 5 or (x + y) == 5:
#         return True
#     else:
#         return False
# print(test_number5(2, 2))
# print(test_number5(27, 53))


 # ====================================================================================================

# 36. Напишите программу на Python для добавления двух объектов,
# если оба объекта являются целыми числами.

# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         return "Inputs must be integers!"
#     return a + b

# print(add_numbers(10, 20))    
# print(add_numbers(10, 20.23)) 
# print(add_numbers('5', 6))     
# print(add_numbers('5', '6'))


 # ====================================================================================================

# 37. Напишите программу на Python,
# которая отображает ваше имя, возраст и адрес в трех разных строках.

# def personal_details():
#     name, age = "Simon", 19
#     address = "Bangalore, Karnataka, India"
#     print("Name: {}\n Age: {}\n Address: {}".format(name, age, address))
# personal_details()


 # ====================================================================================================

# 38. Напишите программу на Python для решения (x + y) * (x + y).
# Тестовые данные: x = 4, y = 3
# Ожидаемый результат: (4 + 3) ^ 2) = 49

# x, y = 4, 3
# result = x * x + 2 * x * y + y * y
# print("({} + {}) ^ 2) = {}".format(x, y, result))


 # ====================================================================================================

# 39. Напишите программу на Python для расчета будущей стоимости
#  указанной основной суммы, процентной ставки и количества лет.
# Тестовые данные: amt = 10000, int = 3,5, годы = 7.

# amt = 10000
# int = 3.5
# years = 7
# future_value = amt * ((1 + (0.01 * int)) ** years)
# print(round(future_value, 2))


 # ====================================================================================================

# 40. Напишите программу на Python для расчета расстояния между точками
# (x1, y1) и (x2, y2).

# import math

# p1 = [4, 0]

# p2 = [6, 6]

# distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

# print(distance)


 # ====================================================================================================

# 41. Напишите программу на Python, проверяющую существование файла.

# import os.path

# print(os.path.isfile('main.txt'))

# isfile - проверяет есть ли такой файл в ...


 # ====================================================================================================

# 42. Напишите программу Python, чтобы определить, 
# работает ли оболочка Python в 32-битном или 64-битном режиме ОС.

# import struct
# print(struct.calcsize("P") * 8)


 # ====================================================================================================

# 43. Напишите программу на Python, чтобы получить название ОС, платформу и информацию о выпуске.

# import platform
# import os

# print("Name system:", os.name)

# print("\nName  OS :", platform.system())

# print("\nVersion system:", platform.release())


 # ====================================================================================================

# 44. Напишите программу Python для поиска пакетов сайта Python.


# import site

# print(site.getsitepackages())


 # ====================================================================================================

# 45. Напишите программу на Python, вызывающую внешнюю команду.


# from subprocess import call

# call(["ls", "-l"])


 # ====================================================================================================

# 46. ​​Напишите программу на Python для получения пути и имени файла, исполняемого в данный момент.

# import os
# print("Current File Name: ", os.path.realpath(__file__))


 # ====================================================================================================

# 47. Напишите программу на Python, чтобы узнать количество используемых процессоров.

# import multiprocessing

# cpu_count = multiprocessing.cpu_count()

# print(cpu_count)


 # ====================================================================================================

# 48. Напишите программу на Python для преобразования строки в число с плавающей запятой или целое число.

# n = "246.2458"
# print(float(n))
# print(int(float(n)))


 # ====================================================================================================


# 49. Напишите программу на Python для вывода списка всех файлов в каталоге.

# from os import listdir
# from os.path import isfile, join

# files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]

# print(files_list)


 # ====================================================================================================

# 50. Напишите программу на Python для печати без новой строки и пробела.

# for i in range(0, 10):
#     print('*', end="")
# print("\n")


 # ====================================================================================================

# 51. Напишите программу на Python для определения профилирования программ на Python.
# Примечание. Профиль — это набор статистических данных, описывающих, как часто и 
# как долго выполняются различные части программы. Эту статистику можно форматировать

# import cProfile
# def sum():
#    print(1 + 2)
# cProfile.run('sum()')


 # ====================================================================================================

# 52. Напишите программу на Python для печати в STDERR.

# from __future__ import print_function

# import sys
# def eprint(*args, **kwargs):

#     print(*args, file=sys.stderr, **kwargs)

# eprint("abc", "efg", "xyz", sep="--")

 # ====================================================================================================

# 53. Напишите программу на Python для доступа к переменным среды.

# import os

# print('*----------------------------------*')

# print(os.environ)

# print('*----------------------------------*')

# print(os.environ['HOME'])

# print('*----------------------------------*')

# print(os.environ['PATH'])

# print('*----------------------------------*')

 # ====================================================================================================

# 54. Напишите программу на Python, чтобы получить текущее имя пользователя.

# import getpass
# print(getpass.getuser())


 # ====================================================================================================

# 55. Напишите программу Python для поиска локальных IP-адресов, используя stdlib Python.

# import socket

# local_hostname = socket.gethostname()

# ip_addresses = socket.gethostbyname_ex(local_hostname)[2]

# filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]

# first_ip = filtered_ips[:1]

# print(first_ip[0])

 # ====================================================================================================

# 56. Напишите программу на Python, чтобы получить высоту и ширину окна консоли.

# import fcntl
# import termios
# import struct

# def terminal_size():

#     th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))

#     return tw, th

# print('Number of columns and Rows: ', terminal_size())

 # ====================================================================================================

# 57. Напишите программу на Python, чтобы получить время выполнения метода Python.

# import time

# def sum_of_n_numbers(n):
#     start_time = time.time()

#     s = 0

#     for i in range(1, n + 1):
#         s = s + i

#     end_time = time.time()

#     return s, end_time - start_time

# n = 5

# print("\nTime to sum of 1 to", n, "and required time to calculate is:", sum_of_n_numbers(n))


 # ====================================================================================================

# 58. Напишите программу на Python для суммирования первых n натуральных чисел.

# n = int(input("Input a number: "))

# sum_num = (n * (n + 1)) / 2

# print("Sum of the first", n, "positive integers:", sum_num)


 # ====================================================================================================

# 59. Напишите программу на Python для преобразования высоты (в футах и ​​дюймах) в сантиметры.

# print("Input your height: ")

# h_ft = int(input("Feet: "))

# h_inch = int(input("Inches: "))

# h_inch += h_ft * 12

# h_cm = round(h_inch * 2.54, 1)

# print("Your height is : %d cm." % h_cm)


 # ====================================================================================================

# 60. Напишите программу на Python для вычисления гипотенузы прямоугольного треугольника.

# from math import sqrt

# print("Input lengths of shorter triangle sides:")

# a = float(input("a: "))

# b = float(input("b: "))

# c = sqrt(a**2 + b**2)

# print("The length of the hypotenuse is:", c)

 # ====================================================================================================

# 61. Напишите программу на Python для преобразования расстояния (в футах) в дюймы, ярды и мили.

# d_ft = int(input("Input distance in feet: "))

# d_inches = d_ft * 12

# d_yards = d_ft / 3.0

# d_miles = d_ft / 5280.0

# print("The distance in inches is %i inches." % d_inches)
# print("The distance in yards is %.2f yards." % d_yards)
# print("The distance in miles is %.2f miles." % d_miles)


 # ====================================================================================================

# 62. Напишите программу на Python для преобразования всех единиц времени в секунды.

# days = int(input("Input days: ")) * 3600 * 24

# hours = int(input("Input hours: ")) * 3600

# minutes = int(input("Input minutes: ")) * 60

# seconds = int(input("Input seconds: "))

# time = days + hours + minutes + seconds

# print("The amount of seconds:", time)


 # ====================================================================================================

# 63. Напишите программу на Python, чтобы получить абсолютный путь к файлу.

# def absolute_file_path(path_fname):
#     import os
#     return os.path.abspath(path_fname)
# print("Absolute file path: ", absolute_file_path("test.txt"))


 # ====================================================================================================

# 64. Напишите программу на Python, которая извлекает дату и время создания и изменения файла.

# import os.path, time

# print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))

# print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

 # ====================================================================================================

# 65. Напишите программу на Python, которая преобразует секунды в дни, часы, минуты и секунды.

# time = float(input("Input time in seconds: "))

# day = time // (24 * 3600)

# time = time % (24 * 3600)

# hour = time // 3600

# time %= 3600

# minutes = time // 60

# time %= 60

# seconds = time
 
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

 # ====================================================================================================

# 66. Напишите программу на Python для расчета индекса массы тела.

# height = float(input("Input your height in Feet: "))

# weight = float(input("Input your weight in Kilograms: "))

# bmi = weight / (height * height)
# rounded_bmi = round(bmi, 2)

# print("Your body mass index is: ", rounded_bmi)


 # ====================================================================================================

# 67. Напишите программу на Python для преобразования давления в килопаскалях в фунты на квадратный дюйм, миллиметр ртутного столба (мм рт. ст.) и атмосферное давление.

# kpa = float(input("Input pressure in kilopascals: "))

# psi = kpa / 6.89475729

# mmhg = kpa * 760 / 101.325

# atm = kpa / 101.325

# print("The pressure in pounds per square inch: %.2f psi"  % (psi))

# print("The pressure in millimeters of mercury: %.2f mmHg" % (mmhg))

# print("Atmosphere pressure: %.2f atm." % (atm))


 # ====================================================================================================

# 68. Напишите программу на Python для вычисления суммы цифр числа.

# num = int(input("Input a four-digit number: "))

# x = num // 1000

# x1 = (num - x * 1000) // 100

# x2 = (num - x * 1000 - x1 * 100) // 10

# x3 = num - x * 1000 - x1 * 100 - x2 * 10

# print("The sum of digits in the number is", x + x1 + x2 + x3)


 # ====================================================================================================

# 69. Напишите программу на Python для сортировки трех целых чисел без использования условных операторов и циклов.

# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# z = int(input("Input third number: "))

# a1 = min(x, y, z)

# a3 = max(x, y, z)

# a2 = (x + y + z) - a1 - a3

# print("Numbers in sorted order: ", a1, a2, a3)


 # ====================================================================================================

# 70. Напишите программу на Python для сортировки файлов по дате.

# import glob
# import os

# files = glob.glob("*.txt")

# files.sort(key=os.path.getmtime)

# print("\n".join(files))


  # ====================================================================================================

# 71. Напишите программу на Python, чтобы получить список каталогов, отсортированный по дате создания.

# from stat import S_ISREG, ST_CTIME, ST_MODE
# import os, sys, time

# dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

# data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))

# data = ((os.stat(path), path) for path in data)

# data = ((stat[ST_CTIME], path) for stat, path in data if S_ISREG(stat[ST_MODE]))

# for cdate, path in sorted(data):
#     print(time.ctime(cdate), os.path.basename(path)) 


  # ====================================================================================================

# 72. Напишите программу на Python, чтобы получить подробную информацию о математическом модуле.

# import math            
# math_ls = dir(math)
# print(math_ls)


  # ====================================================================================================

# 73. Напишите программу на Python для вычисления средних точек линии.

# print('\nCalculate the midpoint of a line :')

# x1 = float(input('The value of x (the first endpoint) '))
# y1 = float(input('The value of y (the first endpoint) '))

# x2 = float(input('The value of x (the first endpoint) '))
# y2 = float(input('The value of y (the first endpoint) '))

# x_m_point = (x1 + x2)/2

# y_m_point = (y1 + y2)/2
# print();

# print("The midpoint of the line is :")

# print( "The midpoint's x value is: ", x_m_point)

# print( "The midpoint's y value is: ", y_m_point)

  # ====================================================================================================

# 74. Напишите программу на Python для хеширования слова.

# soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]

# word = input("Input the word to be hashed: ")

# word = word.upper()

# coded = word[0]

# for a in word[1:len(word)]:
#     i = 65 - ord(a)
#     coded = coded + str(soundex[i])

# print()

# print("The coded word is: " + coded)

# print()

  # ====================================================================================================

# 75. Напишите программу на Python, чтобы получить информацию об авторских правах, и запишите информацию об авторских правах в коде Python.

# import sys

# print("\nPython Copyright Information")

# print(sys.copyright)

# print()

  # ====================================================================================================

# 76. Напишите программу на Python, чтобы получить аргументы командной строки (имя сценария, количество аргументов, аргументы), передаваемые в сценарий.

# import sys

# print("This is the name/path of the script:"), sys.argv[0]

# print("Number of arguments:", len(sys.argv))

# print("Argument List:", str(sys.argv))


  # ====================================================================================================

# 77. Напишите программу на Python, чтобы проверить, является ли система платформой с прямым порядком байтов или с прямым порядком байтов.

# import sys

# print()

# if sys.byteorder == "little":
#     print("Little-endian platform.")
# else:
#     print("Big-endian platform.")

# print()

  # ====================================================================================================

# 78. Напишите программу на Python, чтобы найти доступные встроенные модули.

# import sys
# import textwrap
# module_name = ', '.join(sorted(sys.builtin_module_names))
# print(textwrap.fill(module_name, width=70))

  # ====================================================================================================

# 79. Напишите программу на Python, чтобы получить размер объекта в байтах.

# import sys 

# str1 = "one"
# str2 = "four"
# str3 = "three"
# x = 0
# y = 112
# z = 122.56

# print("Size of ", str1, "=", str(sys.getsizeof(str1)) + " bytes")
# print("Size of ", str2, "=", str(sys.getsizeof(str2)) + " bytes")
# print("Size of ", str3, "=", str(sys.getsizeof(str3)) + " bytes")
# print("Size of", x, "=", str(sys.getsizeof(x)) + " bytes")
# print("Size of", y, "=", str(sys.getsizeof(y)) + " bytes")

# L = [1, 2, 3, 'Red', 'Black']

# print("Size of", L, "=", sys.getsizeof(L), " bytes")

# T = ("Red", [8, 4, 6], (1, 2, 3))

# print("Size of", T, "=", sys.getsizeof(T), " bytes")

# S = {'apple', 'orange', 'apple', 'pear'}

# print("Size of", S, "=", sys.getsizeof(S), " bytes")

# D = {'Name': 'David', 'Age': 6, 'Class': 'First'}

# print("Size of", D, "=", sys.getsizeof(S), " bytes")


  # ====================================================================================================

# 80. Напишите программу на Python, чтобы получить текущее значение предела рекурсии.

# import sys  
# print()  
# print("Current value of the recursion limit:")  
# print(sys.getrecursionlimit())  
# print()  


  # ====================================================================================================

# 81. Напишите программу на Python для объединения N строк.

# colors_list = ['Red', 'White', 'Black'] 
# colors = '-'.join(colors_list) 
# print("Colors: " + colors)

  # ====================================================================================================

# 82. Напишите программу на Python для вычисления суммы всех элементов контейнера (кортежа, списка, набора, словаря).

# s = sum([10, 20, 30])
# print("result:",s)

  # ====================================================================================================

# 83. Напишите программу на Python, проверяющую, все ли числа в списке больше определенного числа.

# num = [2, 3, 4, 5]
# print(all(x > 1 for x in num))
# print(all(x > 4 for x in num))

  # ====================================================================================================

# 84. Напишите программу на Python для подсчета количества вхождений определенного символа в строку.

# s = "The quick brown fox jumps over the lazy dog."
# print(s.count("o"))

  # ====================================================================================================

# 85. Напишите программу на Python, чтобы проверять, является ли путь к файлу файлом или каталогом.

# import os
# path = "abc.txt"
# if os.path.isdir(path):
#     print("\nIt is a directory")
# elif os.path.isfile(path):
#     print("\nIt is a normal file")
# else:
#     print("It is a special file (socket, FIFO, device file)")

  # ====================================================================================================

# 86. Напишите программу на Python, чтобы получить значение ASCII символа.

# print(ord('a'))
# print(ord('A'))
# print(ord('1'))
# print(ord('@'))

  # ====================================================================================================

# 87. Напишите программу на Python, чтобы получить размер файла.

# import os
# file_size = os.path.getsize("abc.txt")
# print("\nThe size of abc.txt is:", file_size, "Bytes")

  # ====================================================================================================

# 88. Учитывая переменные x=30 и y=20, напишите программу Python для вывода «30+20=50».

# x = 30
# y = 20
# print("\n%d+%d=%d" % (x, y, x+y))

  # ====================================================================================================

# 89. Напишите программу на Python, выполняющую действие, если условие истинно.
# Учитывая имя переменной, если значение равно 1, отобразите строку «Первый день месяца!» и ничего не делать, если значение не равно.

# n = 1
# if n == 1:
#   print("\nFirst day of a Month!")
# print()

  # ====================================================================================================

# 90. Напишите программу на Python, создающую копию собственного исходного кода.

# def file_copy(src, dest):
#     with open(src) as f, open(dest, 'w') as d:

# file_copy("untitled0.py", "z.py")

# with open('z.py', 'r') as filehandle:
#     for line in filehandle:
#         print(line, end = '')

  # ====================================================================================================

# 91. Напишите программу на Python для замены двух переменных.

# a = 30
# b = 20
# print("\nBefore swap a = %d and b = %d" %(a, b))
# a, b = b, a
# print("\nAfter swaping a = %d and b = %d" %(a, b))

  # ====================================================================================================

# 92. Напишите программу на Python для определения строки,
#  содержащей специальные символы в различных формах.

# print("\#{'}${\"}@/")
# print("\#{'}${\"}@/")
# print(r"""\#{'}${"}@/""")
# print('\#{\'}${"}@/')
# print('\#{'"'"'}${"}@/')
# print(r'''\#{'}${"}@/''')

  # ====================================================================================================

# 93. Напишите программу на Python, чтобы получить идентификатор, тип и значение объекта.

x = 34
print("\nIdentity: ", x)
print("\nType: ", type(x))
print("\nValue: ", id(x))


  # ====================================================================================================

# 94. Напишите программу на Python для преобразования 
#     байтов заданной строки в список целых чисел.

# S = "The quick brown fox jumps over the lazy dog."
# print("Original string:")
# print(S)
# nums = []
# print("\nConvert bytes of the said string to a list of integers:")
# for chr in S:
#     nums.append(ord(chr))
# print(nums)


  # ====================================================================================================

# 95. Напишите программу на Python, проверяющую, является ли строка числовой.

# str = 'a123'
# try:
#     i = float(str)
# except (ValueError, TypeError):
#     print('\nNot numeric')
# print()


  # ====================================================================================================

# 96. Напишите программу на Python для печати текущего стека вызовов.

# import traceback
# print()
# def f1():
#     return abc()
# def abc():
#     traceback.print_stack()
# f1()
# print()

  # ====================================================================================================

# 97. Напишите программу на Python, чтобы вывести список специальных переменных, используемых в языке.

# s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
# print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )


  # ====================================================================================================

# 98. Напишите программу на Python для получения системного времени.

# import time
# print(time.ctime())


  # ====================================================================================================

# 99. Напишите программу на Python для очистки экрана или терминала.

# import os
# import time
# os.system("ls")
# time.sleep(2)
# os.system('clear')


  # ====================================================================================================

# 100. Напишите программу на Python, чтобы получить имя хоста, на котором выполняется процедура.

# import socket
# host_name = socket.gethostname()
# print("Host name:", host_name)

  # ====================================================================================================

# 101. Напишите программу на Python для доступа и вывода содержимого URL-адреса на консоль.

# from http.client import HTTPConnection
# conn = HTTPConnection("example.com")
# conn.request("GET", "/")
# result = conn.getresponse()
# contents = result.read()
# print(contents)

  # ====================================================================================================

# 102. Напишите программу на Python для получения вывода системной команды.

# import subprocess
# returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
# print(returned_text)

  # ====================================================================================================

#  103. Напишите программу на Python для извлечения имени файла по заданному пути.

# import os
# print(os.path.basename('/users/system1/student1/homework-1.py'))

  # ====================================================================================================

# 104. Напишите программу на Python, чтобы получить эффективный идентификатор группы, эффективный идентификатор пользователя, реальный идентификатор группы и список дополнительных идентификаторов групп, связанных с текущим процессом.
# Примечание. Доступность: Unix.

# import os
# print("Effective group id: ", os.getegid())
# print("Effective user id: ", os.geteuid())
# print("Real group id: ", os.getgid())
# print("List of supplemental group ids: ", os.getgroups())


  # ====================================================================================================

# 105. Напишите программу на Python, чтобы получить среду пользователя.

# import os
# print(os.environ)

  # ====================================================================================================

# 106. Напишите программу на Python для разделения пути разделителем расширений.

# import os.path
# for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
#     print('"%s" :' % path, os.path.splitext(path))

  # ====================================================================================================

# 107. Напишите программу на Python для получения свойств файла.

# import os.path
# import time

# print('File         :', __file__)
# print('Access time  :', time.ctime(os.path.getatime(__file__)))
# print('Modified time:', time.ctime(os.path.getmtime(__file__)))
# print('Change time  :', time.ctime(os.path.getctime(__file__)))
# print('Size         :', os.path.getsize(__file__))

  # ====================================================================================================

# 108. Напишите программу на Python, чтобы найти путь к файлу или каталогу, когда вы встретите имя пути.

# import os.path
# for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
#     print('File        :', file)
#     print('Absolute    :', os.path.isabs(file))
#     print('Is File?    :', os.path.isfile(file))
#     print('Is Dir?     :', os.path.isdir(file))
#     print('Is Link?    :', os.path.islink(file))
#     print('Exists?     :', os.path.exists(file))
#     print('Link Exists?:', os.path.lexists(file))


  # ====================================================================================================

# 109. Напишите программу на Python, чтобы найти путь к файлу или каталогу, когда вы встретите имя пути.

# num = float(input("Input a number: "))

# if num > 0:
#    print("It is a positive number")
# elif num == 0:
#    print("It is zero")
# else:
#    print("It is a negative number")

  # ====================================================================================================

# 110. Напишите программу на Python, позволяющую получать из списка числа, кратные пятнадцати, с помощью анонимной функции.

# num_list = [45, 55, 60, 37, 100, 105, 220]
# result = list(filter(lambda x: (x % 15 == 0), num_list))
# print("Numbers divisible by 15 are", result)


  # ====================================================================================================

# 111. Напишите программу на Python для создания списков файлов из текущего каталога с использованием подстановочных знаков.

# import glob
# file_list = glob.glob('*.*')

# print(file_list)

# print(glob.glob('*.py'))

# print(glob.glob('./[0-9].*'))

  # ====================================================================================================

# 112. Напишите программу на Python для удаления первого элемента из указанного списка.

# color = ["Red", "Black", "Green", "White", "Orange"]
# del color[0]
# print(color)

 
  # ====================================================================================================

# 113. Напишите программу на Python, которая вводит число и генерирует сообщение об ошибке, если это не число.

# while True:
#     try:
#         a = int(input("Input a number: "))
#         break
#     except ValueError:
#         print("\nThis is not a number. Try again...")


  # ====================================================================================================

# 114. Напишите программу на Python для фильтрации положительных чисел из списка.


# nums = [34, 1, 0, -23, 12, -88]
# new_nums = list(filter(lambda x: x > 0, nums))
# print("Positive list: ", new_nums)

  # ====================================================================================================

# def  remove_nth_index(str,index): 
#     return str[:index] + str[index + 1:] 
# print(remove_nth_index("He l lo", 2))
 
  # ====================================================================================================

# 115. Напишите программу на Python для вычисления произведения списка целых чисел (без использования цикла for).

# from functools import reduce
# nums = [10, 20, 30]
# nums_product = reduce((lambda x, y: x * y), nums)
# print("\nProduct of the said numbers: ", nums_product)


  # ====================================================================================================

# 116. Напишите программу на Python для печати символов Юникода.

# str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
# print(str)
 
  # ====================================================================================================

# 117. Напишите программу на Python, чтобы доказать, что две строковые переменные с одинаковым значением указывают на одну и ту же ячейку памяти.

# str1 = "Python"
# str2 = "Python"
# print("\nMemory location of str1 =", hex(id(str1)))
# print("Memory location of str2 =", hex(id(str2)))

 
  # ====================================================================================================

# 118. Напишите программу на Python для создания массива байтов из списка.

# nums = [10, 20, 56, 35, 17, 99]
# values = bytearray(nums)
# for x in values:
#     print(x)

 
  # ====================================================================================================

# 119. Напишите программу на Python для округления числа с плавающей запятой до заданного количества десятичных знаков.

# order_amt = 212.374
# print('\nThe total order amount comes to %f' % order_amt)
# print('The total order amount comes to %.2f' % order_amt)


  # ====================================================================================================

# 120. Напишите программу на Python для форматирования указанной строки и ограничения ее длины.

# str_num = "1234567890"
# print("Original string:", str_num)
# print('%.6s' % str_num)
# print('%.9s' % str_num)
# print('%.10s' % str_num)


 
  # ====================================================================================================

# 121. Напишите программу на Python, чтобы определить, определена переменная или нет.

# try:
#   x = 1
# except NameError:
#   print("Variable is not defined....!")
# else:
#   print("Variable is defined.")

# try:
#   y
# except NameError:
#   print("Variable is not defined....!")
# else:
#   print("Variable is defined.")
  
 
  # ====================================================================================================

# 122. Напишите программу на Python, чтобы очистить переменную, не уничтожая ее.

# Выборочные данные: n=20
# д = {"х":200}
# Ожидаемый результат: 0
# {}

# n = 20
# d = {"x": 200}
# l = [1, 3, 5]
# t = (5, 7, 8)
# print(type(n)())
# print(type(d)())
# print(type(l)())
# print(type(t)())
 
  # ====================================================================================================

# 123. Напишите программу на Python для определения наибольшего и наименьшего целых чисел, чисел long и чисел с плавающей запятой.

# import sys
# print("Float value information: ", sys.float_info)
# print("\nInteger value information: ", sys.int_info)
# print("\nMaximum size of an integer: ", sys.maxsize)

 
  # ====================================================================================================

# 124. Напишите программу на Python, чтобы проверять, имеют ли несколько переменных одинаковое значение.

# x = 20
# y = 20
# z = 20
# if x == y == z == 20:
#     print("All variables have the same value!")

 
  # ====================================================================================================

# 125. Напишите программу на Python для суммирования всех счетчиков в коллекции.

# import collections
# num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
# result = sum(collections.Counter(num).values())
# print(result)

 
  # ====================================================================================================

# 126. Напишите программу на Python, чтобы получить фактический объект модуля для данного объекта.

# from inspect import getmodule
# from math import sqrt
# print(getmodule(sqrt))

 
  # ====================================================================================================

# 127. Напишите программу на Python, проверяющую, помещается ли целое число в 64 бита.

# int_val = 30

# if int_val.bit_length() <= 63:
#     print((-2 ** 63).bit_length())
#     print((2 ** 63).bit_length())

 
  # ====================================================================================================

# 128. Напишите программу на Python, проверяющую наличие в строке строчных букв.

# str1 = 'A8238i823acdeOUEI'
# print(any(c.islower() for c in str1))

 
  # ====================================================================================================

# 129. Напишите программу на Python для добавления ведущих нулей в строку.

# str1 = '122.22'
# print("Original String: ", str1)
# print("\nAdded trailing zeros:")
# str1 = str1.ljust(8, '0')
# print(str1)
# str1 = str1.ljust(10, '0')
# print(str1)
# print("\nAdded leading zeros:")
# str1 = '122.22'
# str1 = str1.rjust(8, '0')
# print(str1)
# str1 = str1.rjust(10, '0')
# print(str1) 

 
  # ====================================================================================================

# 130. Напишите программу на Python, которая использует двойные кавычки для отображения строк.

# import json
# data = {'Alex': 1, 'Suresh': 2, 'Agnessa': 3}

# json_string = json.dumps(data)
# print(json_string)

 
  # ====================================================================================================

# 131. Напишите программу на Python для разделения строки переменной длины на переменные.

# var_list = ['a', 'b', 'c']
# x, y, z = (var_list + [None] * 3)[:3]
# print(x, y, z)
# var_list = [100, 20.25]
# x, y = (var_list + [None] * 2)[:2]
# print(x, y)

 
  # ====================================================================================================

# 132. Напишите программу на Python для вывода домашнего каталога без абсолютного пути.

# import os.path
# print(os.path.expanduser('~'))

 
  # ====================================================================================================

# 133. Напишите программу на Python для расчета времени выполнения программы (разницы между началом и текущим временем).

# from timeit import default_timer
# def timer(n):
#     start = default_timer()
   
#     for row in range(0, n):
#         print(row)
    
#     print(default_timer() - start)

# timer(5)
# timer(15)

 
  # ====================================================================================================

# 134. Напишите программу на Python для ввода двух целых чисел в одну строку.

# x, y = map(int, input().split())
# print("The value of x & y are: ", x, y)

 
  # ====================================================================================================


# 135. Напишите программу на Python для печати переменной без пробелов между значениями.
# Выборочное значение: x =30
# Ожидаемый результат: значение x равно «30».

# x = 30
# formatted_string = 'Value of x is "{}"'.format(x)
# print(formatted_string)

 
  # ====================================================================================================

# 136. Напишите программу на Python для поиска файлов и пропуска каталогов в заданном каталоге.

# import os
# print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/students', f))])

 
  # ====================================================================================================

# 137. Напишите программу на Python для извлечения одной пары ключ-значение из словаря в переменные.

# d = {'Red': 'Green'}
# (c1, c2), = d.items()
# print(c1)
# print(c2)

 
  # ====================================================================================================

# 138. Напишите программу на Python для преобразования true в 1 и false в 0.

# x = 'true'

# x = int(x == 'true')
# print(x)

# x = 'abcd'
# x = int(x == 'true')
# print(x)

 
  # ====================================================================================================

# 139. Напишите программу на Python для проверки IP-адреса.

# import socket

# addr = '127.0.0.2561'

# try:
#     socket.inet_aton(addr)
#     print("Valid IP")

# except socket.error:
#     print("Invalid IP")

 
  # ====================================================================================================

# 140. Напишите программу на Python для преобразования целого числа в двоичное, сохраняющее ведущие нули.
# Пример данных: x=12
# Ожидаемый результат: 00001100.
# 0000001100

# x = 12
# print(format(x, '08b'))
# print(format(x, '010b'))

 
  # ====================================================================================================

# 141. Напишите программу на Python для преобразования десятичных чисел в шестнадцатеричные.
# Пример десятичного числа: 30, 4.
# Ожидаемый результат: 1e, 04

# x = 30
# print(format(x, '02x'))

# x = 4
# print(format(x, '02x'))
 
  # ====================================================================================================

# 142. Напишите программу на Python, проверяющую, за каждой последовательной последовательностью нулей следует последовательная последовательность единиц одинаковой длины в данной строке. Вернуть истину/ложь.
# Исходная последовательность: 01010101.
# Проверьте, за каждой последовательной последовательностью нулей следует последовательная последовательность единиц в указанной строке:
# Истинный
# Исходная последовательность: 00
# Проверьте, за каждой последовательной последовательностью нулей следует последовательная последовательность единиц в указанной строке:
# ЛОЖЬ
# Исходная последовательность: 000111000111.
# Проверьте, за каждой последовательной последовательностью нулей следует последовательная последовательность единиц в указанной строке:
# Истинный
# Исходная последовательность: 00011100011.
# Проверьте, за каждой последовательной последовательностью нулей следует последовательная последовательность единиц в указанной строке:
# ЛОЖЬ

# def test(str1):
#     while '01' in str1:
#         str1 = str1.replace('01', '')
    
#     return len(str1) == 0

# str1 = "01010101"

# print("Original sequence:", str1)

# print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
# print(test(str1))

# str1 = "00"
# print("\nOriginal sequence:", str1)
# print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
# print(test(str1))
# str1 = "000111000111"
# print("\nOriginal sequence:", str1)
# print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
# print(test(str1))
# str1 = "00011100011"
# print("\nOriginal sequence:", str1)
# print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
# print(test(str1))
 
  # ====================================================================================================

# 143. Напишите программу на Python, чтобы определить, работает ли оболочка Python в 32-битном или 64-битном режиме операционной системы.

# import struct
# print(struct.calcsize("P") * 8)

 
  # ====================================================================================================

# 144. Напишите программу на Python, чтобы проверять, является ли переменная целым числом или строкой.

# print(isinstance(25, int) or isinstance(25, str))
# print(isinstance([25], int) or isinstance([25], str))
# print(isinstance("25", int) or isinstance("25", str))

# Функция isinstance() проверяет, является ли объект экземпляром указанного класса или его подкласса.

  # ====================================================================================================

# 145. Напишите программу на Python, чтобы проверить, является ли переменная списком, кортежем или набором.

#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
# x = ('tuple', False, 3.2, 1)

# if type(x) == list:
#     print('x is a list')
# elif type(x) == set:
#     print('x is a set')
# elif type(x) == tuple:
#     print('x is a tuple')    
# else:
#     print('Neither a list nor a set nor a tuple.')

 
  # ====================================================================================================

# 146. Напишите программу на Python, чтобы найти расположение исходных кодов модулей Python.

# import imp

# print("Location of Python os module sources:")
# print(imp.find_module('os'))
# print("\nLocation of Python sys module sources:")
# print(imp.find_module('datetime'))

 
  # ====================================================================================================

# 147. Напишите функцию Python, проверяющую, делится ли число на другое число. Примите от пользователя два целочисленных значения.

# def multiple(m, n):
#     return True if m is n == 0 else False

# print(multiple(20, 5))  
# print(multiple(7, 2))  

 
  # ====================================================================================================

# 148. Напишите функцию Python для поиска максимального и минимального чисел из последовательности чисел.
# Примечание. Не используйте встроенные функции.

# def max_min(data):
#     l = data[0]
#     s = data[0] 
    
#     for num in data:
#         if num > l:
#             l = num  
#         elif num < s:
#             s = num 
    
#     return l, s

# print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
 
  # ====================================================================================================

# 149. Напишите функцию Python, которая принимает положительное целое число и возвращает сумму куба всех положительных целых чисел, меньших указанного числа.

# def sum_of_cubes(n):
#     n -= 1
#     total = 0
    
#     while n > 0:
#         total += n * n * n
#         n -= 1
    
#     return total

# print("Sum of cubes smaller than the specified number: ", sum_of_cubes(3))

 
  # ====================================================================================================

# 150. Напишите функцию Python, чтобы проверять, присутствует ли в
#  последовательности целочисленных значений отдельная пара чисел, 
# произведение которых нечетно.

# def odd_product(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j:
#                 product = nums[i] * nums[j]
#                 if product & 1:
#                     return True
#     return False

# dt1 = [2, 4, 6, 8]
# dt2 = [1, 6, 4, 7, 8]
# dt3 = [1, 3, 5, 7, 9]

# print(dt1, odd_product(dt1))
# print(dt2, odd_product(dt2))
# print(dt3, odd_product(dt3))

 
  # ====================================================================================================



