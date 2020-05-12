from src.conexion import obtener_personajes, obtener_naves
from src.manupulacion import cantidad_de_personajes
from src.render import imprimir_catidad_de_personajes

if __name__ == "__main__":
    personajes = obtener_naves()
    cantidad = cantidad_de_personajes(personajes)
    imprimir_catidad_de_personajes(cantidad)