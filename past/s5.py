a = 4
b = 4
# if a >= b:
#     print("a is greater than b")
# if a <= b:
#     print("a is lower than b")

# if a == b:
#     print("a and b are equal")

# if a != b:
#     print("a and b are not equal")


# a =1
# if a==1:
#     print("1")
#     print("ok")

# print("some thing")


# a = 1
# b = 2
# c = 3

# if a < b and a < c:
#     print("a is lower than b and c")

# if a<b or a<c :
#     print("a is lower than b or c")


# a = True

# if a:
#     print("True")

# if not a:
#     print("other")


# a = True
# b = False

# if a and b:
#     print("one")

# if a or b:
#     print("two")


# a = 3
# b = 4

# c = a == b
# print(c)

# Truthy and Falsy
# if 1:
#     print("1")


# print(bool(1))
# print(bool(0))
# print(bool(-1))
# if 0:
#     print("zero")

# if ' ':
#     print("balalalal")

USERNAME = ('admin','root')
PASSWORD = 'root'

user_name = input('enter user name:> ')
password = input('enter password:> ')
if not user_name or not password:
    print("user name or password can`t be empty!!!!")
elif user_name.lower() not in USERNAME or password != PASSWORD:
    print("user name or pass is not correct!!!")
    print("Permission denied!!!")
else:
    print("login success")
    print('welcome')
