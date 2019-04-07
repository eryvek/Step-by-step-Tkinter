from tkinter import *
import tkinter.messagebox

root=Tk()
tkinter.messagebox.showinfo("Message title","Anurag is the coolest guy on Earth")

answer = tkinter.messagebox.askquestion("Important...","Do you believe in the previous stated fact?")

while answer=="yes":
    print("But you are the dumbest person tbh ,lol")
    answer = tkinter.messagebox.askquestion("Important...", "Do you believe in the previous stated fact?")

print("changing your answer won't make you smart")
root.mainloop()