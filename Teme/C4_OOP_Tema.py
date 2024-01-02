#run SHIFT + F10

#Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
    #   __init__ : instanțiem numărător și numitor
    #   __str__ : afisam "numărător/numitor"
    #   __add__ : returnam o noua fractie care reprezinta adunarea
    #   __sub__: returnam o nouă fracție care reprezinta scădearea
    #   inverse: returnează o nouă fracție (inversa fracției)

class Fractie:
    def __init__(self, numarator, numitor):
        #sus
        self.numarator = numarator
        #jos
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator} / {self.numitor}"

    #adunare
    def __add__(self, other):
        #sus
        nou_numarator = self.numarator * other.numitor + other.numarator * self.numitor
        #jos
        numitor_comun = self.numitor * other.numitor
        return Fractie(nou_numarator, numitor_comun)

    #scadere
    def __sub__(self, other):
        #sus
        nou_numarator = self.numarator * other.numitor - other.numarator * self.numitor
        #jos
        numitor_comun = self.numitor * other.numitor
        return Fractie(nou_numarator, numitor_comun)

    #incersa
    def inverse(self):
        return Fractie(self.numitor, self.numarator)

fract1 = Fractie(1, 2)
fract2 = Fractie(2, 5)

print(f"Fractie 1: {fract1}")
print(f"Fractie 2: {fract2}")

#adunare
suma = fract1 + fract2
print(f"Suma fractie este: {suma}")

#scadere
diferenta = fract1 - fract2
print(f"Scaderea fractiei este: {diferenta}")

#inversa
inversa_1 = fract1.inverse();
print(f"Inversa fractiei 1 este: {inversa_1}")
inversa_2 = fract2.inverse();
print(f"Inversa fractiei 1 este: {inversa_2}")


