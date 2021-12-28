from tkinter import *
import tkinter as tk

from musica import canciones

from funciones_mp3 import reproducir_cancion
from funciones_mp3 import pausar_despausar
from funciones_mp3 import detener_cancion
from funciones_mp3 import detener_reproductor
#-----------------------------------

ventana = Tk()
ventana.title("Salva Music Mp3")
ventana.resizable(False, False)
ventana.geometry("200x100")
ventana.config(background="#0178d4")


imagen_play = tk.PhotoImage(file=r"img\play.png")
imagen_pause = tk.PhotoImage(file=r"img\pause.png")
imagen_stop = tk.PhotoImage(file=r"img\stop.png")

global reproduciendo
cancion = 0
reproduciendo = False
ruta, lista_canciones = canciones()


btn_play = Button(ventana, image=imagen_play, command=lambda: reproducir_cancion(ruta, lista_canciones[1]))
btn_play.place(x=15, y=20)

btn_pause = Button(ventana, image=imagen_pause, command=pausar_despausar)
btn_pause.place(x=75, y=20)

btn_stop = Button(ventana, image=imagen_stop, command=detener_cancion)
btn_stop.place(x=135, y=20)





if __name__ == "__main__":
    ventana.mainloop()

    detener_reproductor()