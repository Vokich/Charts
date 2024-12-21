from tkinter import *
from tkinter.ttk import Radiobutton
import matplotlib.pyplot as plt


window = Tk()
window.title("chart")
window.geometry("500x500")
x_list = []
y_list = []
axis_x_str = ""
axis_y_str = ""
title_str = ""
vid = 0
def rad1_press():
    global vid
    vid = 1
    print(vid)

def rad2_press():
    global vid
    vid = 2
    print(vid)

def rad3_press():
    global vid
    vid = 3
    print(vid)

def clicked():
    global title_txt
    title_str = title_txt.get()
    res = "Заголовок: {}".format(title_txt.get())
    title.configure(text=res)
    print(title_str)

def add_axis_x():
    global axis_x_str
    axis_x_str = txt_axis_x.get()
    res = "Ось Х: {}".format(txt_axis_x.get())
    axis_x.configure(text=res)
    print(axis_x_str)

def add_axis_y():
    global axis_y_str
    axis_y_str = txt_axis_y.get()
    res = "Ось Y: {}".format(txt_axis_y.get())
    axis_y.configure(text=res)
    print(axis_y_str)

def add_text(axis, text):
    if axis == 'x':
        res = "x: {}".format(text)
        x.configure(text=res)
        x_list.append(text)
        print(x_list)
    elif axis == 'y':
        res = "y: {}".format(text)
        y.configure(text=res)
        y_list.append(text)
        print(y_list)

def start():
    global vid
    if vid == 1:
        x_int_list = list(map(int, x_list))
        y_int_list = list(map(int, y_list))
        plt.xlabel(axis_x_str)
        plt.ylabel(axis_y_str)
        plt.title(title_str)
        plt.plot(x_int_list, y_int_list, color='green', marker='o', markersize=1)
        plt.show()
    elif vid == 2:
        x_str = x_list
        y_int_list = list(map(int, y_list))
        plt.xlabel(axis_x_str)
        plt.ylabel(axis_y_str)
        plt.title(title_str)
        plt.bar(x_str, y_int_list, label='значения', alpha=0.5)  # ГИСТОГРАММЫ
        plt.legend()
        plt.show()
    elif vid == 3:
        x_int_list = list(map(int, x_list))
        y_str = y_list
        plt.xlabel(axis_x_str)
        plt.ylabel(axis_y_str)
        plt.title(title_str)
        plt.pie(x_int_list, labels=y_str, autopct='%1.1f%%')
        plt.show()





view = Label(window, text="вид диаграммы:", font=("Arial Bold", 10))

rad1 = Radiobutton(window, text='Ломаная', value=1, command=rad1_press)
rad2 = Radiobutton(window, text='Гистограмма', value=2, command=rad2_press)
rad3 = Radiobutton(window, text='Круговая', value=3, command=rad3_press)

x = Label(window, text='x:')
y = Label(window, text='y:')
title = Label(window, text="Заголовок:")
title_txt = Entry(window, width=10)

x_txt = Entry(window, width=10)
y_txt = Entry(window, width=10)

add_btn_x_txt = Button(window, text='Добавить', command=lambda: add_text('x', x_txt.get()))
add_btn_y_txt = Button(window, text='Добавить', command=lambda: add_text('y', y_txt.get()))

btn = Button(window, text='Добавить', command=clicked)

axis_x = Label(window, text='Ось Х:')
axis_y = Label(window, text='Ось Y:')

txt_axis_x = Entry(window, width=10)
txt_axis_y = Entry(window, width=10)

btn_x = Button(window, text='Добавить', command=add_axis_x)
btn_y = Button(window, text='Добавить', command=add_axis_y)

start_btn = Button(window, text='Создать диаграмму', command=start)

x.grid(column=0, row=2)
y.grid(column=0, row=3)

rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)

view.grid(row=0, column=0)

x_txt.grid(column=1, row=2)
y_txt.grid(column=1, row=3)

title.grid(column=0, row=4)
title_txt.grid(column=1, row=4)

btn.grid(column=2, row=4)

axis_x.grid(column=0, row=5)
axis_y.grid(column=0, row=6)

txt_axis_x.grid(column=1, row=5)
txt_axis_y.grid(column=1, row=6)

btn_x.grid(column=2, row=5)
btn_y.grid(column=2, row=6)

start_btn.grid(column=2, row=7)

add_btn_x_txt.grid(column=2, row=2)
add_btn_y_txt.grid(column=2, row=3)

window.mainloop()
