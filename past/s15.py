import tkinter as tk
from tkinter import ttk

# root = tk.Tk()
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)


# frame_1 = ttk.Frame(root)
# frame_1.grid(row=0, column=0, sticky="NSEW")
# frame_1.columnconfigure(0, weight=1)
# frame_1.columnconfigure(1, weight=1)
# frame_1.rowconfigure(0, weight=1)


# name_label = ttk.Label(frame_1, text="Name:", padding=10)
# name_label.grid(row=0, column=0, sticky="NSEW")

# name_entry = ttk.Entry(frame_1)
# name_entry.grid(row=0, column=1, sticky="NSEW")

# exercise : اضافه کردن ردیف نام خانوادگی
# و ردیف دکمه

# root.mainloop()


######################################################
# pip install pillow
# about label widget
from PIL import Image, ImageTk
import random
GREETINGS = ("Hello", "Hi","Welcome")
root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Our App")

my_variable = tk.StringVar()

# label = ttk.Label(root, textvariable=my_variable, padding=20, compound="left")
# label.pack()
# label.config(font=("Arial",20))

# image = Image.open("orangee.png")
# photo = ImageTk.PhotoImage(image)
# label.config(image=photo)


# my_variable.set(random.choice(GREETINGS))
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.rowconfigure(0, weight=1)

# Text Widget
# text = tk.Text(root, height=8, width=12)
# text.insert("1.0","M")
# text.insert("1.3","G")
# text.insert("1.1","JJJJJJJJJJJJ")
# text.insert("")
# print(text.get("1.0","end"))
# text.grid(row=0,column=0,sticky="e")
# text_scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
# text_scroll.grid(row=0, column=1, sticky="nsw")
# text["yscrollcommand"] = text_scroll.set


# اضافه کردن فریم
# دو ویجت بالا را درون فریم قرار بده

root.mainloop()

# یک صفحه لاگین به همراه عکس های مناسب طراحی کن