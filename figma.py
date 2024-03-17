# У Вас есть строка Вам нужно получить первую букву
# и заменить её во всех остальных местах кроме первого на любой знак
def change_first_char(symbol: str = "$") -> str:
    string = input("Напишите любое слово: ")
    first = string[0]
    return first + string[1:].replace(first.lower(), symbol)
p = change_first_char()
print(p)


# Напишите функцию, чтобы найти второй наиболее часто встречающийся символ в данной строке.
def second_most_frequent(string):
    dict = {}
    for i in string:
        dict[i] = string.count(i)
    return sorted(dict.items(), key=lambda x: x[1])[-2][0]
y = second_most_frequent("философия")
print(y)


# Напишите программу на Python что бы добавить 'ing' в конец заданной строки (длина должна быть не менее 3).
# Если заданная строка уже заканчивается на 'ing', вместо этого добавьте "ly".
# Если длина строки заданной строки меньше 3, оставьте её без изменений. 
def add_ing(string):
    if len(string) < 3:
        return string
    if string[-3:] == "ing":
        return string + "ly"
    return string + "ing"
s = add_ing("substring")
print(s)


# Напишите функцию на Python для проверки повторяющихся букв.
# Он должен принимать строку, то есть предложение. Функция должна возвращать True, если в предложении есть слово с 
# повторяющимися буквами, иначе возвращать False. 
# True, если в предложении есть слово с повторяющимися буквами, иначе возвращать False. 
def check_duplicate_letters(string) -> bool:
    for letter in string:
        if string.count(letter) > 1:
            return True
    return False
n = check_duplicate_letters("test")
print(n)

# Функция проверяет если аргумент больше чем условие, то есть больше чем 1 повторение
# значит в ней есть повторы букв он даст True

