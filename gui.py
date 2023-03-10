from tkinter import *

root = Tk()
root.title("Astoņbumba")
name = Label(root, text="Vārds")
nameEntry = Entry(root)
password = Label(root, text="Password")
passField = Entry(root)


name.grid(row=0, column=0)
nameEntry.grid(row=0, column=1)
password.grid(row=1, column=0)
passField.grid(row=1, column=1)

root.mainloop()
