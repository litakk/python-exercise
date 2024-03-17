
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

