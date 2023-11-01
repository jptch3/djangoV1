"""table de multiplication par 7"""
def multiplication(nb, limite):
    valeur= range(limite+1)
    for i in valeur : 
        print(i, "x", nb, "=", i*nb)
multiplication(5, 10)

class voiture :
    def __init__(self, compagnie, ddc, pays):
        self.compagnie = compagnie
        self.ddc = ddc
        self.pays = pays
    
    def changernom(self, newname):
        old= self.compagnie
        self.compagnie = newname
        return f'Le vieux nom est {old} pour le nouveau qui est {self.compagnie}'