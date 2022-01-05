from tkinter import EXCEPTION, messagebox
import pygame
from cl_cancion import Cancion

from musica import canciones


cancion = 0
ruta, lista_canciones = canciones()



def iniciar_mixer():
    pygame.mixer.init()



def reproducir_cancion_2(id_cancion: int):
    global cancion
    cancion = id_cancion

    iniciar_mixer() # inicializamos mixer
    
    nombre_cancion = lista_canciones[id_cancion].nombre

    if nombre_cancion != "":

        try:
            pygame.mixer.music.load(r"{}\{}".format(ruta, nombre_cancion))
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()
        except Exception:
            messagebox.showerror("Error", "Selecione una cancion")
            return


    
def siguiente_cancion():
    global cancion
    cancion += 1

    try: 
        reproducir_cancion_2(cancion)
    except IndexError:
        cancion = 0
        reproducir_cancion_2(cancion)



def cancion_anterior():
    global cancion
    cancion -= 1

    try:
        reproducir_cancion_2(cancion)
    except IndexError:
        cancion = len(lista_canciones)
        reproducir_cancion_2(cancion - 1)


def manejar_volumen(vol):
    verificar_inicializador = pygame.mixer.get_init()

    if verificar_inicializador == None:
        return

    if int(vol) >= 0 and int(vol) <= 9:
        pygame.mixer.music.set_volume(0.0)
    elif int(vol) >= 10 and int(vol) <= 19:
        pygame.mixer.music.set_volume(0.1)
    elif int(vol) >= 20 and int(vol) <= 29:
        pygame.mixer.music.set_volume(0.2)
    elif int(vol) >= 30 and int(vol) <= 39:
        pygame.mixer.music.set_volume(0.3)
    elif int(vol) >= 40 and int(vol) <= 49:
        pygame.mixer.music.set_volume(0.4)
    elif int(vol) >= 50 and int(vol) <= 59:
        pygame.mixer.music.set_volume(0.5)
    elif int(vol) >= 60 and int(vol) <= 69:
        pygame.mixer.music.set_volume(0.6)
    elif int(vol) >= 70 and int(vol) <= 79:
        pygame.mixer.music.set_volume(0.7)
    elif int(vol) >= 80 and int(vol) <=89:
        pygame.mixer.music.set_volume(0.8)
    elif int(vol) >= 90 and int(vol) <= 99:
        pygame.mixer.music.set_volume(0.9)
    elif int(vol) == 100:
        pygame.mixer.music.set_volume(1.0)


def detener_cancion():
    verificar_inicializador = pygame.mixer.get_init()

    if verificar_inicializador == None:
        messagebox.showerror("Error", "No hay nada para detener")
        return

    pygame.mixer.quit()
    messagebox.showinfo("Detener", "Se detuvo la cancion")


def detener_reproductor():
    verificar_inicializador = pygame.mixer.get_init()

    if verificar_inicializador == None:
        return
    
    pygame.mixer.stop()
    pygame.mixer.quit()


def pausar_cancion():
    pygame.mixer.music.pause()

def despausar():
    pygame.mixer.music.unpause()





def pausar_despausar():
    verificar_init = pygame.mixer.get_init()

    if verificar_init == None:
        messagebox.showerror("Error", "No hay cancion para despausar")
        return

    verificar = pygame.mixer.music.get_busy()
    
    if verificar:
        pausar_cancion()

    else:
        despausar()