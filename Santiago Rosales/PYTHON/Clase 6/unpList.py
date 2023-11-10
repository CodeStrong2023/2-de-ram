#  unpacking a list

def show(name, lastName):
    print(name, lastName)
person = ["Gianni", "Pasquinelli"]
show(person[0], person[1]) # unpacking a list 
show(*person) # unpacking a list

person2 = ("Belén", "Cortese")
show(*person2) # unpacking a tuple

person3 = {"name": "Astor", "lastName": "Pasquinelli"}
show(**person3) # unpacking a dictionary


