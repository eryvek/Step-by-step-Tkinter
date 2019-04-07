from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red",bg="purple")
button2 = Button(topFrame, text="Button 2", fg="blue",bg="green")
button3 = Button(topFrame, text="Button 3", fg="green",bg="red")
button4 = Button(bottomFrame, text="Button 4", fg="purple",bg="blue")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)

root.mainloop()
