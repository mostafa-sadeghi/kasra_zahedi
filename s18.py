import tkinter as tk
from tkinter import ttk
root = tk.Tk()

questions = [
    {
        "title":"کدام گزینه با بقیه متفاوت می باشد؟",
        "option1": "گاو",
        "option2": "اسب",
        "option3": "سیب",
        "answer":"سیب"
     },
    {
        "title":"کدام گزینه صحیح می باشد؟",
        "option1": "درخت",
        "option2": "گل",
        "option3": "توپ",
        "answer":"توپ"
     },
]


class Question:
    def __init__(self,root, question):
        self.title = ttk.Label(root, text=question["title"]).pack()
        self.user_ans = tk.StringVar()
        self.option_one = ttk.Radiobutton(root, text=question["option1"],value=question["option1"],variable=self.user_ans ,\
                                      width=20, command=lambda:self.check_answer(self.user_ans ,question["answer"]))
        self.option_one.pack()

        self.option_two = ttk.Radiobutton(root, text=question["option2"],value=question["option2"],variable=self.user_ans ,\
                                      width=20, command=lambda:self.check_answer(self.user_ans ,question["answer"]))
        self.option_two.pack()

        self.option_three = ttk.Radiobutton(root, text=question["option3"],value=question["option3"],variable=self.user_ans ,\
                                      width=20, command=lambda:self.check_answer(self.user_ans ,question["answer"]))
        self.option_three.pack()

    def check_answer(self, user_answer,answer):
        print("user_ans"+user_answer.get(), "answer"+answer)
        if user_answer.get() == answer:
            print("correct")
        else:
            print("not correct")

for q in questions:
    Question(root, q)






#  عمل بالا را برای سه سوال انجام بده و نمره کاربر را درون یک برچسب نمایش بده


#  combobox
# def handle_selection(event):
#     print(day.get())


# day = tk.StringVar()
# weekday = ttk.Combobox(root, textvariable=day)
# weekday.pack()
# weekday["values"] = ("Mon","Tue","Wed","Thur","Fri","Sat","Sun")
# weekday.bind("<<ComboboxSelected>>",handle_selection)

root.mainloop()
