class Cancion(object):
    id: int
    ruta: str
    nombre: str
    extension = "mp3"

    def __init__(self, id: int, ruta: str, nombre: str) -> None:
        self.id = id
        self.ruta = ruta
        self.nombre = nombre
    
    def __str__(self) -> str:
        return f"{self.id} {self.nombre} {self.extension}"