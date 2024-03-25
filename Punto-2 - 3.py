def pot(x, n):
    exp = 1
    for _ in range(n):
        exp *= x
    return exp
cal_pot = lambda *args: pot(*args)
x = float(input("Escriba un numero real"))
n = int(input("Escriba un numero natural"))
resultado = cal_pot(x, n)
print("El resultado de " + str(x) + " elevado a " + str(n) + " es " + str(resultado))