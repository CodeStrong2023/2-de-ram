
def listar_terminos(**terminos): 
    for key, value in terminos.items():
        print(f"{key} : {value}")
        

listar_terminos()
listar_terminos(IDE = "Integrated Develoment Enviorment", PK = "Primary Key")
listar_terminos(name = "Luis")