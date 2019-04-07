from tkinter import *
root = Tk()

photo = PhotoImage(file="anurag.jpg")#if file exist
label = Label(root,image=photo)
label.pack()

root.mainloop()
