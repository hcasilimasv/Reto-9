def pot(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * pot(x, n - 1)
    else:
        return 1 / pot(x, -n)
bas = float(input("Escriba la base del numero "))
exp = int(input("Escriba el exponente del numero"))
resul = pot(bas, exp)
print(f"{bas} elevado a la {exp} es igual a {resul}")