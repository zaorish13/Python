#rulare SHIFT + F10

# Declararea listei
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista)

# Afisarea unei alte liste ordonata ascendent
lista_ordonata_ascendent = sorted(lista);
print("Lista ordonata ascendent: ", lista_ordonata_ascendent)

# Afișarea unei liste ordonată descendent
lista_ordonata_descendent = lista.copy()
lista_ordonata_descendent.sort(reverse=True)
print("Lista ordonata descendent: ", lista_ordonata_descendent)

# Afișarea numerelor cu indici pari din listă
nr_indici_pari = lista[::2]
print("Numere cu indici pari: ", nr_indici_pari)

# Afișarea numerelor cu indici impari din listă
nr_indici_impari = lista[1::2]
print("Numere cu indici impari: ", nr_indici_impari)

# Afisarea elementelor multipli ai lui 3
lista_multipli_3 = [x for x in lista if x % 3 == 0]
print("Elementele multipli ai lui 3:", lista_multipli_3)
