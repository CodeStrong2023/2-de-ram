
def sum_args(*args):
    total = 0
    for arg in args:
        total += int(arg)
    print(f"El total de la suma de argumentos es {total}")


sum_args(1,2,4,34,43,66,33,2)