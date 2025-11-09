# -*- coding: UTF-8 -*-

from tkinter import *
from HomeworkRegister import *
from sys import exit

Number = 0

def getNumber():
    global Number
    if number.get().isdigit() and int(number.get()) >0:
        Number = int(number.get())
        get_number.destroy()
    else:
        get_number.title("请输入正整数")

def yes_button():
    
    Split = split.get()[0:1] if split.get() != "" else " "
    yes.config(state="disabled")
    example.finish(done.get('1.0', END), split=Split)
    undone.config(state="normal")
    undone.delete('1.0', END)
    undone.insert("1.0", example.show_unsubmitted(endless=True))
    undone.config(state="disabled")
    yes.config(state="normal")
    

get_number = Tk()
get_number.title("请输入全班人数")
get_number.geometry("300x50")
get_number.resizable(False, False)
get_number.protocol("WM_DELETE_WINDOW", lambda: exit())
number = Entry(get_number)
yes = Button(get_number, text="确认", command=getNumber)
number.pack()
yes.pack()
get_number.mainloop()

example = HomeworkRegister(list(i for i in range(1, Number + 1)))

root = Tk()
root.title("Teacher Tools")
root.geometry("500x250")
root.config(bg="skyblue")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", lambda: exit())

tips = Label(root, text="已交名单", bg="skyblue")
done = Text(root, exportselection=1, width=70, height=5)
yes = Button(root, text="确认", bg="skyblue", command=yes_button)
tips2 = Label(root, text="未交名单", bg="skyblue")
undone = Text(root, exportselection=1, width=70, height=5, bg="skyblue", state="disabled")
get_split = Label(root, text="请输入分隔符(默认为空格):")
split = Entry(root, exportselection=0)

tips.place(relx=0.5, rely=0.05, anchor=CENTER)
done.place(relx=0.5, rely=0.1, anchor=N)
yes.place(relx=0.5, rely=0.45, anchor=CENTER)
tips2.place(relx=0.5, rely=0.6, anchor=S)
undone.place(relx=0.5, rely=0.95, anchor=S)
get_split.place(relx=0, rely=0.45, anchor=W)
split.place(relx=0, rely=0.55, anchor=W)

root.mainloop()