def impr_cuad(*args):
    for n in args:
        print("Numero " + str(n) + " , Cuadrado = " + str(n * n))
impr_cuad(*range(1, 101))