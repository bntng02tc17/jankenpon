import tkinter
import random

hasil_akhir = "naruto"

def batu():
    a = "batu"
    jankenpon(a)
def gunting():
    a = "gunting"
    jankenpon(a)
def kertas():
    a = "kertas"
    jankenpon(a)

def jankenpon(a):
    b = random.choice(["gunting","batu", "kertas"])
    if (a == "batu"):
        if(b == "batu"):
            hasil = "seri"
        elif(b == "kertas"):
            hasil = "kalah"
        else:
            hasil = "menang"
    elif(a == "gunting"):
        if(b == "gunting"):
            hasil = "seri"
        elif(b == "batu"):
            hasil = "kalah"
        else:
            hasil = "menang"
    else:
        if(b == "kertas"):
            hasil = "Seri"
        elif(b == "gunting"):
            hasil = "kalah"
        else:
            hasil = "menang"
    labelHasil["text"] = hasil
    labelAnda["text"] ="pilihan Anda: " + a
    labelLawan['text'] ="pilihan Lawan: " + b


jendela = tkinter.Tk()
jendela.title("Jankenpon")
tombolBatu = tkinter.Button(jendela,text="batu", command = batu)
tombolBatu.pack()
tombolKertas = tkinter.Button(jendela,text="kertas", command = kertas)
tombolKertas.pack()
tombolGunting = tkinter.Button(jendela,text="gunting", command = gunting)
tombolGunting.pack()
labelAnda = tkinter.Label(jendela,text="", foreground = "green")
labelAnda.pack()
labelLawan = tkinter.Label(jendela,text="", foreground = "red")
labelLawan.pack()
labelHasil = tkinter.Label(jendela,text="belum ada hasil", background="yellow")
labelHasil.pack()
jendela.geometry("350x250")
jendela.mainloop()