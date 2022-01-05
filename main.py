from tkinter import *
import tkinter as tk
from tkinter import messagebox

from win32api import GetSystemMetrics

from musica import canciones

from funciones_mp3 import pausar_despausar
from funciones_mp3 import detener_cancion
from funciones_mp3 import detener_reproductor
from funciones_mp3 import siguiente_cancion
from funciones_mp3 import cancion_anterior
from funciones_mp3 import manejar_volumen
from funciones_mp3 import reproducir_cancion_2
#-----------------------------------

ancho_pantalla = int((GetSystemMetrics(0) - 500) / 2)
alto_pantalla = int((GetSystemMetrics(1) - 255) / 2)

print(f"W: {ancho_pantalla}")
print(f"H: {alto_pantalla}")

ventana = Tk()
ventana.geometry(f"500x255+{ancho_pantalla}+{alto_pantalla}")
ventana.config(background="black")
ventana.iconbitmap(r"img\icono.ico")
ventana.title("SMN")
ventana.resizable(False,False)
ventana.config(highlightbackground="#00FA19", highlightcolor="#00FA19", highlightthickness=0)
# ventana.overrideredirect(True)

ruta, lista_canciones = canciones()

#-----------------------------------------------

frame_lista_canciones = Frame(ventana, background="#333") # Frame para el Listbox

contenedor_canciones = Listbox(
    frame_lista_canciones, # frame
    width=77, # Ancho
    height=10, # Alto
    background="#333", # Color del fondo 
    foreground="#00FA19", # Color de las letras
    borderwidth=0, # Borde
    highlightbackground="#00FA19", # ¿?
    highlightcolor="#00FA19",
    selectmode=SINGLE) # Modo selecion de un elemento

sb = Scrollbar(
    frame_lista_canciones, 
    orient="vertical",
    bd=0,
    activebackground="black",	
    highlightbackground="black"
    ) # Scrollbar para el listbox

sb.config(command=contenedor_canciones.yview)
contenedor_canciones.config(yscrollcommand=sb.set)

frame_lista_canciones.place(x=10, y=20)
contenedor_canciones.pack(side=LEFT)
sb.pack(side=RIGHT, fill=Y)

for c in lista_canciones:
    contenedor_canciones.insert(END, c)

#-----------------------------------------------

def selecionar_cancion_listbox():
    # retorna una tupla con el indice del elemento -> (0,)
    cancion = contenedor_canciones.curselection()

    if len(cancion) >= 1:
        # recibe un argumento tipo index y devuelve el nombre del elemento selecionado
        nombre_cancion = contenedor_canciones.get(cancion[0])
        contenedor_canciones.selection_clear(0, END) # deselecionamos el item
        # cancion_reproduciendose["text"] = nombre_cancion

        if cancion[0] >= 0:
            return lista_canciones[cancion[0]].id  
        else:
            return lista_canciones[cancion[0]].id  
            # messagebox.showerror("Error", "Selecione una cancion.")



img_play = tk.PhotoImage(file=r"img\play2.png")
img_pause = tk.PhotoImage(file=r"img\pause2.png")
img_stop = tk.PhotoImage(file=r"img\stop2.png")
img_prev = tk.PhotoImage(file=r"img\prev.png")
img_next = tk.PhotoImage(file=r"img\next.png")

btn_reproducir_cancion = Button(
    ventana, 
    image=img_play, 
    background="#333", 
    command=lambda: reproducir_cancion_2(selecionar_cancion_listbox()))

btn_pausar_camcion = Button(ventana, image=img_pause, background="#333", command=pausar_despausar)
btn_detener_cancion = Button(ventana, image=img_stop, background="#333", command=detener_cancion)
btn_anterior_cancion = Button(ventana, image=img_prev, background="#333", command=cancion_anterior)
btn_siguiente_cancion = Button(ventana, image=img_next, background="#333", command=siguiente_cancion)

btn_reproducir_cancion.place(x=10, y=190)
btn_pausar_camcion.place(x=70, y=190)
btn_detener_cancion.place(x=130, y=190)
btn_anterior_cancion.place(x=190, y=190)
btn_siguiente_cancion.place(x=250, y=190)


def cambiar_volumen(n):
    manejar_volumen(n)

vol = IntVar()

volumen = Scale(
    ventana, 
    label="Volumen", 
    orient=HORIZONTAL,
    variable=vol, 
    from_=0, 
    to=100,
    background="#333",
    foreground="#00FA19",
    bd=0,
    relief=RAISED,
    highlightbackground="#00FA19",
    length=175,
    command=cambiar_volumen)
volumen.set(100)
volumen.place(x=310, y=190)

cancion_reproduciendose = Label(ventana, foreground="#00FA19", background="black")
cancion_reproduciendose.place(x=10, y=280)





if __name__ == "__main__":
    ventana.mainloop()
    detener_reproductor()