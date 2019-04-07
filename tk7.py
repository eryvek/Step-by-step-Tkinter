from tkinter import  *

def doNothing():
    print("Clicked...")

root = Tk()

#     *********(Menubar*************
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New project...",command=doNothing)
fileMenu.add_command(label="New",command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)

#     *********(Toolbar*************
toolbar = Frame(root)
insertBut = Button(toolbar,text="Insert",command=doNothing)
insertBut.pack(side=LEFT,padx=2,pady=0)
printBut = Button(toolbar,text="Print",command=doNothing)
printBut.pack(side=LEFT,padx=2,pady=0)

toolbar.pack(side=TOP,fill=X)

#     *********Statusbar*************
status = Label(root,text="This is status...",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)


root.mainloop()

