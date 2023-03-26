# numbers = [1,2,3,4,5,6]
# numbers[0] = 100
# print("numbers: ", numbers)
# numbers.append(500)
# print("numbers: ", numbers)

# numbers = (1,2,3,4,5,6)
# print(type(numbers))
# numbers[0] = 100 # error

# favorite_sports = ["football", "tennis", "pingpong"]
# # dictionary
# favorite_sports = {}
# print(type(favorite_sports))


# favorite_sports = {
#     'reza': 'football',
#     'sara': 'pingpong',
#     'artin': 'basketball'
# }

# print(favorite_sports['artin'])

# # write a program that takes id, name, family from input and put these informations into a dictionary called student

# favorite_sports['roze'] = "pingpong"
# print(favorite_sports)

# del favorite_sports['sara']
# print(favorite_sports)


# students = [{'id': 1, 'name': 'roze', 'grade': 'A'},
#             {'id': 2, 'name': 'reza', 'grade': 'B'}]

# print(students[0]['name'])

# write a program that takes id, name and age of three students and put them in a list called students
# and print all student's name and age seperately

# students = []
# id = int(input('enter student`s id:> '))
# name = input('enter student`s name:> ')
# age = int(input('enter student`s age:> '))
# student = {}

# student['id'] = id
# student['name'] = name
# student['age'] = age

# students.append(student)
# id = int(input('enter student`s id:> '))
# name = input('enter student`s name:> ')
# age = int(input('enter student`s age:> '))
# student = {}

# student['id'] = id
# student['name'] = name
# student['age'] = age

# students.append(student)

# print(students)
# print(f'{students[0]["name"]} has {students[0]["age"]} years old')
# print(f'{students[1]["name"]} has {students[1]["age"]} years old')


import turtle
s = turtle.Screen()
s.bgcolor('cyan')
p = turtle.Pen()
p.fillcolor('green')
p.begin_fill()
p.pensize(3)
p.pencolor('red')
p.shape('turtle')  # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
p.shapesize(3)
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.end_fill()
s.exitonclick()

# square
# pentagon
