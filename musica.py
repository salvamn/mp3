import getpass
import os
from typing import Union
from cl_cancion import Cancion

nombre_inicio_sesion_usuario = getpass.getuser()

# Modificar ruta si es necesario
ruta_clasica_windows = r"C:\Users\{}".format(nombre_inicio_sesion_usuario)
lista_carpetas_ruta = os.listdir(ruta_clasica_windows)


for archivo in os.listdir(ruta_clasica_windows):
    # La carpeta musica es la que viene con el sistema operativo
    if archivo in ["Music", "Musica"]:
        ruta_clasica_windows += f"\{archivo}"
        break


# Puedes agregar otras extensiones si lo necesitas
lista_canciones = [cancion for cancion in os.listdir(ruta_clasica_windows) if cancion.lower().endswith(".mp3")]

lista_objetos_canciones = []

for i, c in enumerate(iterable=lista_canciones, start=0):
    if c.lower().endswith(".mp3"):
        cancion = Cancion(i, ruta_clasica_windows, c)
        lista_objetos_canciones.append(cancion)






def canciones() -> Union[str, list]:
    """Esta funcion retornara una ruta y una lista de canciones."""
    return ruta_clasica_windows, lista_objetos_canciones
