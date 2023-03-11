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
    askQuestion = Button(root, text="Uzdod jautājumu", command= lambda : questionsWindow(userID))

    history.grid(row=0, column=0)
    askQuestion.grid(row=1, column=0)


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

def askedQuestion(question, userID, ans):
    q = question.get()
    if len(q) != 0:
        question.delete(0, END)
        answer = answers()
        ans.config(text=answer)
        addToHistory(q, answer, userID)

    pass
def questionsWindow(userID):
    for widgets in root.winfo_children():
        widgets.destroy()
    questionLabel = Label(root, text="Uzdod savu jautājumu: ")
    questionsEntry = Entry(root)
    answerLabel = Label(root, text="")
    askBtn = Button(root, text="Jautāt!", command= lambda :askedQuestion(questionsEntry, userID, answerLabel))

    questionLabel.grid(row=0, column=0)
    questionsEntry.grid(row=0, column=1)
    answerLabel.grid(row=1,column=0, columnspan=2)
    askBtn.grid(row=2,column=0, columnspan=2)

def loginCheck(vards, parole):
    sucess = loginIntoAccount(vards, parole)
    sucess = '1'
    #if sucess:
    userSpace(sucess)



root.mainloop()
