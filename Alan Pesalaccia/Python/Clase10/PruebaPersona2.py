
from Persona2 import Persona2
print(" Creación de objetos ".center(50, "-"))
persona5 = Persona2("Juan", "Perez", 32)
persona5.mostrar_detalle()

print(__name__) # Esto nos muestra el nombre del módulo que estamos ejecutando

print(" Eliminación de objetos ".center(50, "-"))

del persona5 # Esto nos permite eliminar el objeto de la memoria con el método destructor __del__ de la clase Persona2

