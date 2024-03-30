import tkinter

window = tkinter.Tk() #membuat window baru

Entry1 = tkinter.Entry(window)
labelPlus = tkinter.Label(window, text="+")
Entry2 = tkinter.Entry(window)
buttonHitung = tkinter.Button(window, text="Hitung !")
labelHasil = tkinter.Label(window, text="hasil : ")

def fungsiJumalah() :
    angka1 = Entry1.get()
    angka2 = Entry2.get()
    hasilHitung = int(angka1) + int(angka2)
    labelHasil.configure(text=f"hasil  : {hasilHitung}")

buttonHitung.configure(command=fungsiJumalah)

Entry1.pack()
labelPlus.pack()
Entry2.pack()
buttonHitung.pack()
labelHasil.pack()

window.mainloop()