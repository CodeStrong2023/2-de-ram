from Persona import Persona

print('uso de la clase Persona'.center(50, '-'))
if __name__ == '__main__':
  persona4 = Persona("Astor", "Pasquinelli", 14)
  persona4.mostrar_detalles()
  print(__name__)
  
  
print('eliminacion de objetos'.center(30, '-'))

del persona4