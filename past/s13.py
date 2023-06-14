import tkinter as tk
from tkinter import ttk


# def greet():
#     print("hello", name.get())


# root = tk.Tk()
# root.geometry("400x80")
# root.resizable(False, False)
# name_label = ttk.Label(root, text='Name:', font=("Arial", 14))
# name_label.pack(side="left", padx=20)

# name = tk.StringVar()
# name_entry = ttk.Entry(root, textvariable=name,
#                        foreground="blue", font=("Arial", 14))
# name_entry.pack(side="left")

# greet_button = ttk.Button(
#     root, text="Greet", cursor="hand2", padding=20, command=greet)
# greet_button.pack(side="left", fill="both", expand=True)

# root.mainloop()


# root = tk.Tk()

# ttk.Label(root, text="Number 1", background="green",
#           foreground="white", anchor="center").pack(side="left",ipadx=10, ipady=10, fill="both", expand=True)
# ttk.Label(root, text="Number 2", background="red",
#           foreground="white", anchor="center").pack(side="left",ipadx=10, ipady=10,fill="both",expand=True)


# root.mainloop()


root = tk.Tk()

main = ttk.Frame(root)
main.pack(side="left")
ttk.Label(main, text="Label top", background="red").pack(
    side="left", expand=True, fill="both")
ttk.Label(main, text="Label top", background="blue").pack(
    side="left", expand=True, fill="both")
ttk.Label(main, text="Label top", background="green").pack(
    side="left", expand=True, fill="both")

main = ttk.Frame(root)
main.pack(side="left")
ttk.Label(main, text="Label top", background="red").pack(
    side="left", expand=True, fill="both")
ttk.Label(main, text="Label top", background="blue").pack(
    side="left", expand=True, fill="both")
ttk.Label(main, text="Label top", background="green").pack(
    side="left", expand=True, fill="both")


root.mainloop()
