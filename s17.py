# def my_func(x):
#     if x > 0:
#         print(x)

# res = my_func(2)
# print(res)
# my_func(2)


# def login(user_name, password):
#     global status
#     if user_name == 'admin' and password == '123':
#         return True


# def go_to_profile(state):
#     if state == True:
#         print("you can access the page...")


# user_name = input('Enter the username: ')
# password = input('Enter the password: ')
# p = login(user_name, password)
# go_to_profile(p)


# def my_func(x):
#     return x % 2 == 0

# print(my_func(5))
# x = 4
# print((lambda i: i % 2 == 0)(x))

# res = (lambda : "hello")()
# print(res)

import tkinter as tk
from tkinter import ttk


def show():
    print(state.get())


root = tk.Tk()
state = tk.StringVar()

check_button = ttk.Checkbutton(
    root, text="pizza", variable=state, command=show, onvalue="on", offvalue="off")
check_button.pack()

root.mainloop()
