# У Вас есть строка Вам нужно получить первую букву
# и заменить её во всех остальных местах кроме первого на любой знак

def change_first_char(symbol: str = "$") -> str:
    string = input("Напишите любое слово: ")
    first = string[0]
    return first + string[1:].replace(first.lower(), symbol)
p = change_first_char()
print(p)

