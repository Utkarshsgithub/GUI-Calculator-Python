from tkinter import *


def click(event):

    global scvalue

    text = event.widget.cget("text")

    print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()

root.geometry("500x800")

root.title("CALCULATOR - @utkarshcodes")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, padx=30, pady=10)

f = Frame(root, bg="orange", pady=5)

b = Button(f, text="9", padx=28, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 30 bold", padx=28, pady=18)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida 30 bold", padx=28, pady=18)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="orange", pady=5)

b = Button(f, text="6", padx=28, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 30 bold", padx=28, pady=18)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", font="lucida 30 bold", padx=28, pady=18)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="orange", pady=5)

b = Button(f, text="3", padx=28, pady=15, font="lucida 30 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 30 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", font="lucida 30 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="orange", pady=5)

b = Button(f, text="0", padx=28, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=21, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="/", font="lucida 30 bold", padx=28, pady=18)
b.pack(side=LEFT, padx=21, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="lucida 30 bold", padx=28, pady=18)
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="orange", pady=5)

b = Button(f, text="+", padx=28, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 30 bold", padx=28, pady=18)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 30 bold", padx=28, pady=18)
b.pack(side=LEFT, padx=21, pady=5)
b.bind("<Button-1>", click)

f.pack()

f.pack()

# root.config(bg="grey")

root.mainloop()
