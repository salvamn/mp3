import getpass
import os
from typing import Union

nombre_inicio_sesion_usuario = getpass.getuser()
ruta_clasica_windows = r"C:\Users\{}".format(nombre_inicio_sesion_usuario)
lista_carpetas_ruta = os.listdir(ruta_clasica_windows)


for archivo in os.listdir(ruta_clasica_windows):
    if archivo in ["Music", "Musica"]:
        ruta_clasica_windows += f"\{archivo}"
        break



lista_canciones = [cancion for cancion in os.listdir(ruta_clasica_windows) if cancion.lower().endswith(".MP3") or cancion.endswith(".mp3")]

def canciones() -> Union[str, list]:
    """Esta funcion retornara una ruta y una lista de canciones."""
    return ruta_clasica_windows, lista_canciones