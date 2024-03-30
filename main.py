import tkinter

def button1Clik() :
    print("button 1 di klik")

window = tkinter.Tk()

#window.mainloop() : menampilkan window/jendela/tampilannya kaya notepad

#widget : komponen yang ada di dalam window (label, teks, tombol)
#pack() : menambahkan komponen ke window
#membuat widget
mynamelabel = tkinter.Label(
    window, 
    text= "nama saya ketty",
    background= "purple",
    font= ('arial', 15),
    cursor= 'star'
)
mynamelabel.pack()

kolomTekxtSebaris = tkinter.Entry(window)
kolomTekxtSebaris.pack()


button1 = tkinter.Button(window, text= "tekan aku!", command=button1Clik) #command= : menampilkan hasil jika di klik
button1.pack()

window.mainloop()

