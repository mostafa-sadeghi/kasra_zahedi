# x = "0123456789"
# print("x=", x)

# print("xp[0] = ", x[0])
# print("xp[1] = ", x[1])
# print("xp[-1] = ", x[-1])

# Access 0-5
# print("x[:6] = ", x[:6])

#

# print("x[6:] = ", x[6:])
# print("x[6:9] = ", x[6:9])
# print("x[6:10] = ", x[6:10])
# print("x[-1:-5:-1] = ", x[-1:-5:-1])
# print("x[10:5:-1] = ", x[10:5:-1])

#


# a = "Hi"
# b = "There"
# c = "!"


# print(a + b)
# print(a + b + c)
# print(3 * a)
# print(a * 3)
# print((a*2)+(b*2))


# a= "Hi There"
# print(len(a))

# b = [3,4,7,4,3]
# print(len(b))


# for character in "this is a test":
#     print(character.upper(), end=" ")
months_list = []
months = "JanFebMarAprMay"

x = len(months)//3

for i in range(x):
    months_list.append(months[i*3:(i*3)+3])

print(months_list)

number_of_month = int(input('enter month number:>(0-4) '))
print("month name is", months_list[number_of_month])

#
