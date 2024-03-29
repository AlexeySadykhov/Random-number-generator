from random import randint
from tkinter import Tk, Frame, Label, Entry, Button, Listbox, END
from tkinter import messagebox as mb
from tkinter import filedialog as fd


def generate():
    try:
        min_n = int(e_from.get())
        max_n = int(e_to.get())
        count_n = int(e_numb.get())
        if min_n > max_n or count_n <= 0:
            mb.showerror(
                "Error",
                "Arguments must be rational")
        else:
            listbox.delete(0, END)
            for i in range(count_n):
                listbox.insert(0, randint(min_n, max_n))
    except ValueError:
        mb.showerror(
            "Error",
            "Arguments must be digits")


def clear():
    e_from.delete(0, END)
    e_to.delete(0, END)
    e_numb.delete(0, END)
    listbox.delete(0, END)


def export():
    data = listbox.get(0, END)
    if not data:
        mb.showerror("Error",
                     "List is empty")
    else:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html"),
                       ("ALL files", "*.*")))
        file = open(file_name, "w")
        for item in data:
            file.write(f"{str(item)}\n")
        file.close()


window = Tk()
window.title("Random number generator")
window.geometry("332x359")
window.resizable(width=False, height=False)

frame1 = Frame(master=window, width=150, height=150, bg="pink")
frame1.place(x=0, y=0)
frame2 = Frame(master=window, width=150, height=209, bg="purple")
frame2.place(x=0, y=150)
l_int = Label(master=frame1, text="Interval",
              fg="white", bg="black")
l_int.place(x=30, y=10)
l_from = Label(master=frame1, text="From:",
               fg="white", bg="black")
l_from.place(x=10, y=50)
l_to = Label(master=frame1, text="To:",
             fg="white", bg="black")
l_to.place(x=10, y=90)
e_from = Entry(master=frame1, width=5)
e_from.place(x=70, y=50)
e_to = Entry(master=frame1, width=5)
e_to.place(x=70, y=90)
l_numb = Label(master=frame2, text="Number of digits:",
               fg="white", bg="black")
l_numb.place(x=10, y=10)
e_numb = Entry(master=frame2, width=12)
e_numb.place(x=10, y=50)
btn_gen = Button(master=frame2, text="Generate", width=10,
                 command=generate)
btn_gen.place(x=10, y=100)
btn_clear = Button(master=frame2, text="Clear", width=10,
                   command=clear)
btn_clear.place(x=10, y=130)
btn_exp = Button(master=frame2, text="Export list", width=10,
                 command=export)
btn_exp.place(x=10, y=160)
listbox = Listbox(master=window, height=21)
listbox.place(x=150, y=0)

window.mainloop()
