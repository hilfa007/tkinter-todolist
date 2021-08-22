import datetime as dt
from tkinter import *
from tkinter import messagebox

global task_list

def newTask():
    task = entry.get()
    if task != "":
        list.insert(END,task + '\n')
        task_list.append(task + '\n')
        entry.delete(0,"end")
        with open('taskfile.txt', 'a') as f:
            f.write(task)
            f.write("\n")
        f.close()
    else:
        messagebox.showwarning("warning","please enter some task...")

def delTask():

    selection=list.curselection()
    value = list.get(selection[0])
    list.delete(selection[0])

    ind = task_list.index(value)
    del task_list[ind]

    with open('taskfile.txt','w') as f:
        for i in task_list:
            f.writelines(i)
            print(i)

    f.close()





window = Tk()
window.minsize(width=250,height=400)
window.maxsize(width=250,height=400)
window.title("ToDo List")
window.configure(bg="light pink")

frame = Frame(window)
frame.pack(pady=10)

label = Label(window,text="have a good day!",font="times",bg="light pink",bd=2)
label.pack(side=TOP)

list = Listbox(frame,height=8,width=25,bd=3, activestyle="none")
list.pack(side=LEFT,fill=BOTH)

task_list=[]
with open('taskfile.txt','r') as f:
    task_list = f.readlines()
    for item in task_list:
        list.insert(END,item)


scroll = Scrollbar(frame)
scroll.pack(side=RIGHT,fill=BOTH)
list.config(yscrollcommand=scroll.set)
scroll.config(command=list.yview)

entry = Entry(window,font=('times',15),bd=4)
entry.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=20)

add_task = Button(button_frame,text="Add",font=('times','14'),padx=10,pady=5,bd=3,command=newTask)
add_task.pack(fill=BOTH,expand=True,side=LEFT)

del_task = Button(button_frame,text="delete",font=('times','14'),padx=10,pady=5,bd=3,command=delTask)
del_task.pack(fill=BOTH,expand=True,side=RIGHT)

w = Label(window, text=f"{dt.datetime.now():%a, %b %d %Y}", font=("times", 14),bg="pink")
w.pack()


window.mainloop()