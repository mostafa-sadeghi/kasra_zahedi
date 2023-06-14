# List Boxes

# import tkinter as tk
# from tkinter import ttk


# def handle_selection(event):
#     i = langs_select.curselection()
#     print(i)
#     for item in i:
#         print(langs_select.get(item))


# root = tk.Tk()
# programming_languages = ("c", "c++", "java", "javascript", "python", "golang")
# langs = tk.StringVar(value=programming_languages)
# langs_select = tk.Listbox(root, listvariable=langs,
#                           height=6, selectmode="extended")
# langs_select.pack()

# langs_select.bind("<<ListboxSelect>>", handle_selection)


# root.mainloop()


# spinbox

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

spinbox = tk.Spinbox(root, from_=0, to=50).pack()

root.mainloop()
