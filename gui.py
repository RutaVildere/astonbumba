from tkinter import *
from funkcijas import *
from tkinter import messagebox
root = Tk()
root.title("Astoņbumba")
name = Label(root, text="Vārds")
nameEntry = Entry(root)
password = Label(root, text="Password")
passField = Entry(root)
login = Button(root, text="Ienākt", command=lambda: loginCheck(nameEntry.get(), passField.get()))

name.grid(row=0, column=0)
nameEntry.grid(row=0, column=1)
password.grid(row=1, column=0)
passField.grid(row=1, column=1)
login.grid(row=2, column=0, columnspan=2)


def userSpace(userID):
    for widgets in root.winfo_children():
        widgets.destroy()
    history = Button(root, text="Apskati vēsturi", command= lambda : historyWindow(userID))
    history.grid(row=0, column=0)
def historyWindow(userID):
    for widgets in root.winfo_children():
        widgets.destroy()
    history_questions = checkHistory(userID)
    print(history_questions)
    if history_questions != "Empty":
        num = 0
        for i in history_questions:
            x = Label(root, text=i[0]+ i[1])
            x.grid(row=num, column=0)
            num+=1
    else:
        messagebox.showinfo("Nohistory", "Nohistory")


def loginCheck(vards, parole):
    sucess = loginIntoAccount(vards, parole)
    if sucess:
        userSpace(sucess)



root.mainloop()
