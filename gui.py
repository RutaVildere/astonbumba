from tkinter import *
from funkcijas import *
from tkinter import messagebox

root = Tk()
root.title("Astoņbumba")
root.geometry("350x350")
root.config(bg='#D1D1D1')

def loginScreen():
    for widgets in root.winfo_children():
        widgets.destroy()
    nameEntry = Entry(root)
    password = Label(root, text="Password")
    passField = Entry(root)
    login = Button(root, text="Ienākt", command=lambda: loginCheck(nameEntry.get(), passField.get()))
    name = Label(root, text="Vārds")
    name.grid(row=0, column=0, padx=(80, 10), pady=(100, 10))
    nameEntry.grid(row=0, column=1, pady=(100, 10))
    password.grid(row=1, column=0, padx=(80, 10), pady=10)
    passField.grid(row=1, column=1)
    login.grid(row=2, column=0, columnspan=2, padx=(80, 10), pady=10)


def userSpace(userID):
    for widgets in root.winfo_children():
        widgets.destroy()
    history = Button(root, text="Apskati vēsturi", command=lambda : historyWindow(userID))
    askQuestion = Button(root, text="Uzdod jautājumu", command= lambda : questionsWindow(userID))
    logout = Button(root, text="Izrakstīties", command=lambda : loginScreen())

    history.grid(row=0, column=0, padx=(120, 10), pady=(100, 10))
    askQuestion.grid(row=1, column=0, padx=(120, 10), pady=10)
    logout.grid(row=2, column=0,padx=(120, 10), pady=10)



def historyWindow(userID):
    for widgets in root.winfo_children():
        widgets.destroy()
    history_questions = checkHistory(userID)

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

    questionLabel.grid(row=0, column=0, padx=(50, 10), pady=10)
    questionsEntry.grid(row=0, column=1)
    answerLabel.grid(row=1,column=0, columnspan=2, padx=(50, 10), pady=10)
    askBtn.grid(row=2,column=0, columnspan=2, padx=(50, 10), pady=10)

def loginCheck(vards, parole):
    sucess = loginIntoAccount(vards, parole)
    sucess = '1'
    #if sucess:
    userSpace(sucess)


loginScreen()
root.mainloop()
