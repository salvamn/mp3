from tkinter import messagebox
import pygame



def iniciar_mixer():
    pygame.mixer.init()

def reproducir_cancion(ruta: str, cancion: str):
    iniciar_mixer()
    pygame.mixer.music.load(r"{}\{}".format(ruta, cancion))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()





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

    

    