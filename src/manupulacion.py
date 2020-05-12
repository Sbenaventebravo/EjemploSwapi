
import logging
def cantidad_de_personajes(personajes):
    cantidad_final = -1
    cantidad = personajes.get("count", False)
    if cantidad:
        cantidad_final = cantidad
    else:
        logging.error("NO encontre la llave count")
    return cantidad_final
