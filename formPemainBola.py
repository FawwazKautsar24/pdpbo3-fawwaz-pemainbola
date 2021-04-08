from tkinter import *
# from PIL import ImageTK, Image

root = Tk()
root.title("Form Pemain Bola")
root.iconbitmap('ball.ico')

# Creating a Label Widget
# -- FRAME --
frame = LabelFrame( root, padx=50, pady=50 )
frame.pack( padx=10, pady=10 )
# -- FINAL FRAME --

# -- LABEL --
nama = Label( frame, text="Nama Lengkap" )
asalNegara = Label( frame, text="Asal Negara" )
usia = Label( frame, text="Usia" )
klub = Label( frame, text="Asal Klub" )
tipikalPemain = Label( frame, text="Tipikal Pemain" )
kakiTerkuat = Label( frame, text="Kaki Terkuat" )
posisiUtama = Label( frame, text="Posisi Utama" )

form = Label( frame, text="Football Form App", font=("Helvatic", 16), padx=50 )
desc = Label( frame, text="Form Pemain Sepak Bola", font=("Helvatic", 8) )

titikDua1 = Label( frame, text=" : ", padx=12, pady=10 )
titikDua2 = Label( frame, text=" : ", padx=12, pady=10 )
titikDua3 = Label( frame, text=" : ", padx=12, pady=10 )
titikDua4 = Label( frame, text=" : ", padx=12, pady=10 )
titikDua5 = Label( frame, text=" : ", padx=12, pady=10 )
titikDua6 = Label( frame, text=" : ", padx=12, pady=10 )
titikDua7 = Label( frame, text=" : ", padx=12, pady=10 )
# -- FINAL LABEL --

# -- INPUT --
inputNama = Entry( frame, width=40 )
inputAsalNegara = Entry( frame, width=40 )
inputUsia = Entry( frame, width=40 )
inputKlub = Entry( frame, width=40 )
# -- FINAL INPUT --

# -- DROPDOWN --
def show():
    myLabel = Label( frame, text=clicked.get() ).grid( row=4, column=2 )

# tipikal = sweeper, libero, playmarker, poacher, target man
options = [
    "                    -- select here --                    ",
    "Sweeper",
    "Libero",
    "Playmarker",
    "Poacher",
    "Target man"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(frame, clicked, *options)
# -- FINAL DROPDOWN --

# -- CHECKBOX --
varcheck = StringVar()
varcheck.set("")

kakiKiri = Checkbutton( frame, text="Kiri", variable=varcheck, onvalue="Kiri" )
kakiKanan = Checkbutton( frame, text="Kanan", variable=varcheck, onvalue="Kanan" )
kakiKeduanya = Checkbutton( frame, text="Kedua Kaki", variable=varcheck, onvalue="Kedua Kaki" )
# -- FINAL CHECKBOX --

# -- RADIO BUTTON
varradio = StringVar()
varradio.set("")

pilihPosisi1 = Radiobutton( frame, text="Penyerang", variable=varradio, value="Penyerang", command= lambda: clicked(varradio.get()) )
pilihPosisi2 = Radiobutton( frame, text="Gelandang", variable=varradio, value="Gelandang", command= lambda: clicked(varradio.get()) )
pilihPosisi3 = Radiobutton( frame, text="Bertahan", variable=varradio, value="Penyerang", command= lambda: clicked(varradio.get()) )

# namesPosisiUtama = [
#     ("Penyerang", "Penyerang"),
#     ("Gelandang", "Gelandang"),
#     ("Bertahan", "Bertahan")
# ]

# tampungPosisiUtama = StringVar()
# tampungPosisiUtama.set("Penyerang")

# for text, namePosisiUtama in namesPosisiUtama: 
#     pilihPosisi = Radiobutton( frame, text=text, variable=tampungPosisiUtama, value=namesPosisiUtama )
# -- FINAL RADIO BUTTON

# -- OPEN WINDOW --
def open():
    global my_img
    top = Toplevel()
    top.title("Form Pemain Detail")
    top.iconbitmap('ball.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/jerma_sus.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()
# FINAL OPEN WINDOW --

# -- BUTTON --
def myClick():
    global top
    top.title("Form Pemain Detail")
    top.iconbitmap('ball.ico')
    output1 = Label( top, text=inputNama.get() ).pack()
    output1 = Label( top, text=inputAsalNegara.get() ).pack()
    output1 = Label( top, text=inputUsia.get() ).pack()
    output1 = Label( top, text=inputKlub.get() ).pack()

def myClick2():
    output2 = Label( root, text="19079912 - Fawwaz Kautsar" ).pack()

openPhotoFile = Button( frame, text="OPEN PHOTO FILE", padx=22 )
submit = Button( frame, text="SUBMIT", padx=50, command=myClick )
seeAll = Button( frame, text="SEE ALL SUBMISSIONS", padx=10, command=open )
clear = Button( frame, text="CLEAR SUBMISSIONS", padx=12 )
about = Button( frame, text="ABOUT", padx=50, command=myClick2 )
exit = Button( frame, text="EXIT", padx=50, command=root.quit )
# -- FINAL BUTTON --



# Showing it onto the screen
nama.grid( row=0, column=0 )
asalNegara.grid( row=1, column=0 )
usia.grid( row=2, column=0 )
klub.grid( row=3, column=0 )
tipikalPemain.grid( row=4, column=0 )
kakiTerkuat.grid( row=5, column=0 )
posisiUtama.grid( row=6, column=0 )

titikDua1.grid( row=0, column=1 )
titikDua2.grid( row=1, column=1 )
titikDua3.grid( row=2, column=1 )
titikDua4.grid( row=3, column=1 )
titikDua5.grid( row=4, column=1 )
titikDua6.grid( row=5, column=1 )
titikDua7.grid( row=6, column=1 )

inputNama.grid( row=0, column=2, columnspan=3 )
inputAsalNegara.grid( row=1, column=2, columnspan=3 )
inputUsia.grid( row=2, column=2, columnspan=3 )
inputKlub.grid( row=3, column=2, columnspan=3 )

drop.grid( row=4, column=2, columnspan=3 )

kakiKiri.grid( row=5, column=2 )
kakiKanan.grid( row=5, column=3 )
kakiKeduanya.grid( row=5, column=4 )
kakiKiri.deselect()

# pilihPosisi.grid( row=6, column=2 )
pilihPosisi1.grid( row=6, column=2 )
pilihPosisi2.grid( row=6, column=3 )
pilihPosisi3.grid( row=6, column=4 )
pilihPosisi1.deselect()

openPhotoFile.grid( row=7, column=0, columnspan=5 )
submit.grid( row=8, column=0, columnspan=5 )

form.grid( row=0, rowspan=2, column=5 )
desc.grid( row=2, column=5 )

seeAll.grid( row=3, column=5 )
clear.grid( row=4, column=5 )
about.grid( row=5, column=5 )
exit.grid( row=8, column=5 )


root.mainloop()