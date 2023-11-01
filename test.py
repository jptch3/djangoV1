"""table de multiplication par 7"""
def multiplication(nb, limite):
    valeur= range(limite+1)
    for i in valeur : 
        print(i, "x", nb, "=", i*nb)
multiplication(5, 10)


