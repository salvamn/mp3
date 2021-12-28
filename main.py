from tkinter import *
import tkinter as tk

from musica import canciones

from funciones_mp3 import reproducir_cancion
from funciones_mp3 import pausar_despausar
from funciones_mp3 import detener_cancion
from funciones_mp3 import detener_reproductor
from funciones_mp3 import siguiente_cancion
from funciones_mp3 import cancion_anterior
from funciones_mp3 import manejar_volumen
#-----------------------------------

ventana = Tk()
ventana.title("Salva Music Mp3")
ventana.resizable(False, False)
ventana.geometry("200x250")
ventana.config(background="#0178d4")


imagen_play = tk.PhotoImage(file=r"img\play.png")
imagen_pause = tk.PhotoImage(file=r"img\pause.png")
imagen_stop = tk.PhotoImage(file=r"img\stop.png")
imagen_atras = tk.PhotoImage(file=r"img\atras.png")
imagen_siguiente = tk.PhotoImage(file=r"img\siguiente.png")

ruta, lista_canciones = canciones()


btn_play = Button(ventana, image=imagen_play, command=reproducir_cancion)
btn_play.place(x=15, y=20)

btn_pause = Button(ventana, image=imagen_pause, command=pausar_despausar)
btn_pause.place(x=75, y=20)

btn_stop = Button(ventana, image=imagen_stop, command=detener_cancion)
btn_stop.place(x=135, y=20)



btn_atras = Button(ventana, image=imagen_atras, command=cancion_anterior)
btn_atras.place(x=15, y=80)

btn_siguiente = Button(ventana, image=imagen_siguiente, command=siguiente_cancion)
btn_siguiente.place(x=75, y=80)



def cambiar_volumen(n):
    manejar_volumen(n)

vol = IntVar()

volumen = Scale(ventana, label="Volumen", orient=HORIZONTAL, variable=vol, from_=0, to=100, command=cambiar_volumen)
volumen.set(50)
volumen.place(x=15, y=140)


nombre_cancion = Label(ventana, text="Cancion: ", bg="#0178d4", fg="White")
nombre_cancion.place(x=15, y=200)


if __name__ == "__main__":
    ventana.mainloop()
    detener_reproductor()