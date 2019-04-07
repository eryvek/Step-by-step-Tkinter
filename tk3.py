from tkinter import *
root = Tk()

one = Label(root,text="One",fg="red",bg="white")
one.pack()

two = Label(root,text="Two",fg="green",bg="black")
two.pack(fill=X)

three = Label(root,text="Three",fg="blue",bg="grey")
three.pack(side=LEFT,fill=Y)

root.mainloop()