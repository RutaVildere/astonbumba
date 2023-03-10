import tkinter as tk
from funkcijas import *

window = tk.Tk()
window.title('Astoņbumba')
window.geometry("350x350")
window.config(bg='#D1D1D1')

def atbilde():
    for widgets in window.winfo_children():
        widgets.destroy()
    j = tk.Label(text="iegūtā atbilde uz jautājumu",
                 bg='#D1D1D1',
                 fg='#74308D',
                 font=('Calibri', 14)).place(anchor="c",
                                             relx=0.5,
                                             rely=0.2)  #vel jaievieto attēls
    #jāsataisa lai atbilde ir random ģenerēta un izvadīta

    atgriezties = tk.Button(window,
                            text="Atgriezties",
                            command=izvele,
                            width=10,
                            bg='#D1D1D1',
                            fg='#FFFFFF',
                            highlightthickness=0,
                            activebackground='#3d3737',
                            activeforeground='#737373',
                            font=('Calibri', 11)).place(anchor="c",
                                                        relx=0.8,
                                                        rely=0.9)


def jautajums():
    for widgets in window.winfo_children():
        widgets.destroy()
    j = tk.Label(text="Uzdod savu jautājumu",
                 bg='#D1D1D1',
                 fg='#74308D',
                 font=('Calibri', 14)).place(anchor="c", relx=0.5, rely=0.2)
    parole2 = tk.Entry(window, validate="key",
                       font=('Calibri', 10)).place(anchor="c",
                                                   relx=0.5,
                                                   rely=0.4,
                                                   width=150)
    a = tk.Button(window,
                  text="Uzzināt atbildi!",
                  command=atbilde,
                  width=15,
                  bg='#D1D1D1',
                  fg='#FFFFFF',
                  highlightthickness=0,
                  activebackground='#3d3737',
                  activeforeground='#737373',
                  font=('Calibri', 11)).place(anchor="c", relx=0.7, rely=0.7)


def liet_vesture():
    for widgets in window.winfo_children():
        widgets.destroy()
    v = tk.Label(text="Tava vēsture",
                 bg='#D1D1D1',
                 fg='#74308D',
                 font=('Calibri', 14)).place(anchor="c", relx=0.5, rely=0.2)
    atpakal = tk.Button(window,
                        text="Atpakal",
                        command=izvele,
                        width=10,
                        bg='#D1D1D1',
                        fg='#FFFFFF',
                        highlightthickness=0,
                        activebackground='#3d3737',
                        activeforeground='#737373',
                        font=('Calibri', 11)).place(anchor="c",
                                                    relx=0.8,
                                                    rely=0.9)


def izvele():
    for widgets in window.winfo_children():
        widgets.destroy()
    vesture = tk.Button(window,
                        text="Apskatīt vēsturi",
                        command=liet_vesture,
                        width=15,
                        bg='#D1D1D1',
                        fg='#FFFFFF',
                        highlightthickness=0,
                        activebackground='#3d3737',
                        activeforeground='#737373',
                        font=('Calibri', 11)).place(anchor="c",
                                                    relx=0.5,
                                                    rely=0.3)
    jaut = tk.Button(window,
                     text="Uzdot savu jautājumu",
                     command=jautajums,
                     width=25,
                     bg='#D1D1D1',
                     fg='#FFFFFF',
                     highlightthickness=0,
                     activebackground='#3d3737',
                     activeforeground='#737373',
                     font=('Calibri', 11)).place(anchor="c",
                                                 relx=0.5,
                                                 rely=0.5)
    iziet = tk.Button(window,
                      text="Iziet no profila",
                      width=15,
                      bg='#D1D1D1',
                      fg='#FFFFFF',
                      highlightthickness=0,
                      activebackground='#3d3737',
                      activeforeground='#737373',
                      font=('Calibri', 11)).place(anchor="c",
                                                  relx=0.5,
                                                  rely=0.7)


def register():
    for widgets in window.winfo_children():
        widgets.destroy()
    hello = tk.Label(text="Izveido savu lietotāja profilu",
                     bg='#D1D1D1',
                     fg='#74308D',
                     font=('Calibri', 14)).place(anchor="c",
                                                 relx=0.4,
                                                 rely=0.2)
    vards = tk.Label(text="Vārds",
                     bg='#D1D1D1',
                     fg='#74308D',
                     font=('Calibri', 10)).place(anchor="c",
                                                 relx=0.2,
                                                 rely=0.35)
    uzvards = tk.Label(text="Uzvārds",
                       bg='#D1D1D1',
                       fg='#74308D',
                       font=('Calibri', 10)).place(anchor="c",
                                                   relx=0.2,
                                                   rely=0.4)

    vards = tk.Entry(window, validate="key",
                     font=('Calibri', 10)).place(anchor="c",
                                                 relx=0.5,
                                                 rely=0.35,
                                                 width=150)
    parole = tk.Entry(window, validate="key",
                      font=('Calibri', 10)).place(anchor="c",
                                                  relx=0.5,
                                                  rely=0.4,
                                                  width=150)

    epasts = tk.Label(text="Ēpasts",
                      bg='#D1D1D1',
                      fg='#74308D',
                      font=('Calibri', 10)).place(anchor="c",
                                                  relx=0.2,
                                                  rely=0.45)
    par_reg = tk.Label(text="Ievadi paroli",
                       bg='#D1D1D1',
                       fg='#74308D',
                       font=('Calibri', 10)).place(anchor="c",
                                                   relx=0.15,
                                                   rely=0.5)
    par_reg_2 = tk.Label(text="Ievadi paroli",
                         bg='#D1D1D1',
                         fg='#74308D',
                         font=('Calibri', 10)).place(anchor="c",
                                                     relx=0.15,
                                                     rely=0.55)

    epasts = tk.Entry(window, validate="key",
                      font=('Calibri', 10)).place(anchor="c",
                                                  relx=0.5,
                                                  rely=0.45,
                                                  width=150)
    parole1 = tk.Entry(window, validate="key",
                       font=('Calibri', 10)).place(anchor="c",
                                                   relx=0.5,
                                                   rely=0.5,
                                                   width=150)
    parole2 = tk.Entry(window, validate="key",
                       font=('Calibri', 10)).place(anchor="c",
                                                   relx=0.5,
                                                   rely=0.55,
                                                   width=150)

    atpakal = tk.Button(window,
                        text="Atpakal",
                        command=lietotajs,
                        width=10,
                        bg='#D1D1D1',
                        fg='#FFFFFF',
                        highlightthickness=0,
                        activebackground='#3d3737',
                        activeforeground='#737373',
                        font=('Calibri', 11)).place(anchor="c",
                                                    relx=0.8,
                                                    rely=0.9)
    jaut_vesture = tk.Button(window,
                             text="Ienākt",
                             command=izvele,
                             width=10,
                             bg='#D1D1D1',
                             fg='#FFFFFF',
                             highlightthickness=0,
                             activebackground='#3d3737',
                             activeforeground='#737373',
                             font=('Calibri', 11)).place(anchor="c",
                                                         relx=0.8,
                                                         rely=0.7)


def ienakt():
    for widgets in window.winfo_children():
        widgets.destroy()
    hello = tk.Label(text="Lietotājvārds",
                     bg='#D1D1D1',
                     fg='#74308D',
                     font=('Calibri', 10)).place(anchor="c",
                                                 relx=0.3,
                                                 rely=0.3)
    hello = tk.Label(text="Parole",
                     bg='#D1D1D1',
                     fg='#74308D',
                     font=('Calibri', 10)).place(anchor="c",
                                                 relx=0.37,
                                                 rely=0.5)
    vards = tk.Entry(window, validate="key",
                     font=('Calibri', 10)).place(anchor="c",
                                                 relx=0.7,
                                                 rely=0.3,
                                                 width=150)
    parole = tk.Entry(window, validate="key",
                      font=('Calibri', 10)).place(anchor="c",
                                                  relx=0.7,
                                                  rely=0.5,
                                                  width=150)
    jaut_vesture = tk.Button(window,
                             text="Ienākt",
                             command=izvele, loginIntoAccount() ,
                             width=10,
                             bg='#D1D1D1',
                             fg='#FFFFFF',
                             highlightthickness=0,
                             activebackground='#3d3737',
                             activeforeground='#737373',
                             font=('Calibri', 11)).place(anchor="c",
                                                         relx=0.8,
                                                         rely=0.6)
    atpakal = tk.Button(window,
                        text="Atpakal",
                        command=lietotajs,
                        width=10,
                        bg='#D1D1D1',
                        fg='#FFFFFF',
                        highlightthickness=0,
                        activebackground='#3d3737',
                        activeforeground='#737373',
                        font=('Calibri', 11)).place(anchor="c",
                                                    relx=0.8,
                                                    rely=0.9)


def lietotajs():
    for widgets in window.winfo_children():
        widgets.destroy()


hello = tk.Label(text="Esi sveicināts!",
                 bg='#D1D1D1',
                 fg='#74308D',
                 font=('Calibri', 14)).place(anchor="c", relx=0.5, rely=0.3)

ienakt = tk.Button(window,
                   text="Ienākt profilā",
                   command=ienakt,
                   width=12,
                   bg='#D1D1D1',
                   fg='#FFFFFF',
                   highlightthickness=0,
                   activebackground='#3d3737',
                   activeforeground='#737373',
                   font=('Calibri', 11)).place(anchor="c", relx=0.5, rely=0.5)

regis = tk.Button(window,
                  text="Reģistrēties",
                  command=register,
                  width=10,
                  bg='#D1D1D1',
                  fg='#FFFFFF',
                  highlightthickness=0,
                  activebackground='#3d3737',
                  activeforeground='#737373',
                  font=('Calibri', 11)).place(anchor="c", relx=0.5, rely=0.6)

tk.mainloop()
