import datetime as dt
from tkinter import *
from tkinter import messagebox


def newTask():
    task = entry.get()
    if task != "":
        list.insert(END,task)
        entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","please enter some task...")

def delTask():
    list.delete(ANCHOR)

window = Tk()
window.minsize(width=250,height=400)
window.maxsize(width=250,height=400)
window.title("ToDo List")
window.configure(bg="pink")

frame = Frame(window)
frame.pack(pady=10)

label = Label(window,text="have a good day!",font="times",bg="pink")
label.pack(side=TOP)

list = Listbox(frame,height=8,width=25,bd=1, activestyle="none")
list.pack(side=LEFT,fill=BOTH)

task_list = [" workout"," study"," paint"," shopping"," learn something new"]
for item in task_list:
    list.insert(END,item)
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT,fill=BOTH)
list.config(yscrollcommand=scroll.set)
scroll.config(command=list.yview)

entry = Entry(window,font=('times',15))
entry.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=20)

add_task = Button(button_frame,text="Add",font=('times','14'),padx=10,pady=5,command=newTask)
add_task.pack(fill=BOTH,expand=True,side=LEFT)

del_task = Button(button_frame,text="delete",font=('times','14'),padx=10,pady=5,command=delTask)
del_task.pack(fill=BOTH,expand=True,side=RIGHT)

w = Label(window, text=f"{dt.datetime.now():%a, %b %d %Y}", font=("times", 14),bg="pink")
w.pack()


window.mainloop()