import tkinter as tk
from tkinter import ttk
root = tk.Tk()

questions = [
    {
        "title":"کدام گزینه با بقیه متفاوت می باشد؟",
        "option1": "Option1",
        "option2": "Option2",
        "option3": "Option3",
        "answer":"Option1"
     },
    {
        "title":"کدام گزینه صحیح می باشد؟",
        "option1": "Option11",
        "option2": "Option22",
        "option3": "Option33",
        "answer":"Option22"
     },
]
# def check_answer(user_answer,answer):
#     print("user_ans"+user_answer.get(), "answer"+answer)
#     if user_answer.get() == answer:
#         print("correct")
#     else:
#         print("not correct")

class Form:
    def __init__(self,root, question) -> None:
        self. title = ttk.Label(root, text=question["title"]).pack()
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
    Form(root, q)




# def create_form(questions):
#     op = []
#     ans = []
#     user_answer = tk.StringVar()
#     for i,question in enumerate(questions):
#         op.append(user_answer)
        
#         ttk.Label(root, text=question["title"]).pack()
#         option_one = ttk.Radiobutton(root, text=question["option1"],value=question["option1"],variable=op[i],\
#                                       width=20, command=lambda:check_answer(op[i],question["answer"]))
#         option_one.pack()

        # option_two = ttk.Radiobutton(root, text=question["option2"],value=question["option2"],variable=op[i],\
        #                               width=20, command=lambda:check_answer(op[i],question["answer"]))
        # option_two.pack()

        # option_three = ttk.Radiobutton(root, text=question["option3"],value=question["option3"],variable=op[i],\
        #                                 width=20, command=lambda:check_answer(op[i],question["answer"]))
        # option_three.pack()


# create_form(questions)



# def check_answer():
#     if user_answer.get() == answer:
#         print("correct")
#     else:
#         print("not correct")
# user_answer = tk.StringVar()
# ttk.Label(root, text="کدام گزینه با بقیه متفاوت می باشد؟").pack()
# answer = "سیب"
# option_one = ttk.Radiobutton(root, text="اسب",value="اسب",variable=user_answer, width=20, command=check_answer)
# option_one.pack()

# option_two = ttk.Radiobutton(root, text="الاغ",value="الاغ",variable=user_answer, width=20, command=check_answer)
# option_two.pack()

# option_three = ttk.Radiobutton(root, text="گاو",value="گاو",variable=user_answer, width=20, command=check_answer)
# option_three.pack()

# option_four = ttk.Radiobutton(root, text="سیب",value="سیب",variable=user_answer, width=20, command=check_answer)
# option_four.pack()

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
