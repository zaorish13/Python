#rulare SHIFT + F10

#**********************************************************************************************************************#
#                                               Lista
#**********************************************************************************************************************#
#Lista este o structura de date ordonata si mutable(poate fi modificata)
#este definita folosind []
#Numerotarea acestora incepe de la 0 si se termina cu n-1
#accesarea elementelor din lista se face nu cumele listei precedat de inde-ul scris intre []
my_list = [8, 5, -3, 6, 20]
print(my_list)
my_list = [4+5j, "Python" , -20.75, True, my_list]

print(my_list)
#accesarea elementelor din lista se face nu cumele listei precedat de inde-ul scris intre []
print(my_list[2])           #-20.75

#elementele listei pot fi accesata si cu index negativ, astfel ultimul element va fi identat cu -1
print(my_list[-2])          #True

#len() - aflarea lungimii unei liste
print(len(my_list))         #5 elemente

#slice() - impartirea listei
# - putem specifica doar index-ul de start. Index pozitiv(de la inceputul listei) sau negativ(de la coada listei)
my_new_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_sliced_list = my_new_list[4:]    #index pozitiv
print(my_sliced_list)               #[4, 5, 6, 7, 8, 9, 10]
my_sliced_list = my_new_list[-5:]   #index negativ
print(my_sliced_list)               #[6, 7, 8, 9, 10]

#putem specifica doar index-ul de final. Index pozitiv sau negativ
my_sliced_list = my_new_list[:6]    #index pozitiv
print(my_sliced_list)               #[0, 1, 2, 3, 4, 5]
my_sliced_list = my_new_list[:-5]   #index negativ
print(my_sliced_list)               #[0, 1, 2, 3, 4, 5]

#putem specifica atat indexul de start cat si final. Elementul de pe indexul de final NU va fi inclus in lista noua
my_sliced_list = my_new_list[2:4]   # 2 = 2; 4 = 4
print(my_sliced_list)               #[2, 3]
my_sliced_list = my_new_list[-5:-2] # -5  = 6 ; -2 = 9
print(my_sliced_list)               #[6, 7, 8]
my_sliced_list = my_new_list[2:-5]  # 2 = 2; -5 = 6
print(my_sliced_list)               #[2, 3, 4, 5]
my_sliced_list = my_new_list[-5:8]  #-5 = 6; 8 = 8
print(my_sliced_list)               #[6, 7]
#folosim toata(:) lista si pas(2)
my_sliced_list = my_new_list[::2]
print(my_sliced_list)               #[0, 2, 4, 6, 8, 10]
#folosim doar index de start(1) si pas(2)
my_sliced_list=my_new_list[1::2]
print(my_sliced_list)               #[1, 3, 5, 7, 9]
#folosim index de start, final si pas
my_sliced_list = my_new_list[2:-3:4]
print(my_sliced_list)               #[2, 6]
#***************************************#
#index(element)
print(my_list)                      #[(4+5j), 'Python', -20.75, True, [8, 5, -3, 6, 20]]
print(my_list.index(-20.75))        #-20.75 se afla pe pozitia 2

#append(element_nou) - adauga un element la finalul listei
my_sliced_list.append(500)
print(my_sliced_list)               #[2, 6, 500]

#insert(index, element_nou) - insereaza pe pozitia index elementul nou
print(my_list)                      #[(4+5j), 'Python', -20.75, True, [8, 5, -3, 6, 20]]
my_list.insert(2, 500)
print(my_list)                      #[(4+5j), 'Python', 500, -20.75, True, [8, 5, -3, 6, 20]]

#remove(element)-sterge elementul dorit
print(my_list)                      #[(4+5j), 'Python', 500, -20.75, True, [8, 5, -3, 6, 20]]
my_list.remove('Python')
print(my_list)                      #[(4+5j), 500, -20.75, True, [8, 5, -3, 6, 20]]

#pop() - scoate din lista ultimul element
my_list.pop()
print(my_list)                      #[(4+5j), 500, -20.75, True]

#pop(index) - scoate din lista elementul de pe pozitia index
my_list.pop(3)                      #True
print(my_list)                      #[(4+5j), 500, -20.75]

#clear() - scoate din lista toate elemente
o_nou_lista = [2, 4, 65, 7, 8]
o_nou_lista.clear()
print(o_nou_lista)                  #[]

#copy() - copiaza lista intr-o alta lista. Sau mai poate fi folosita si functia list(my_list)
my_list1 = my_sliced_list.copy()
print(my_list1)                      # my_list1 va avea elementele din my_slice_list [2, 6, 500]

#reverse() - construieste lista avand elementele in ordine inversa(de la final la inceput)
my_list.reverse()                   #[(4+5j), 500, -20.75]
print(my_list)                      #[-20.75, 500, (4+5j)]

#sort() - sorteaza elementele din lista in ordine ascendenta(modificare se face in-place)
#print(my_list)                     #[-20.75, 500, (4+5j)]
#my_list.sort()
#print(my_list)                     #nu poate sorta daca sunt elemente de diferite tipuri, ex: complex, float, int
my_unsorted_list = [5, 8, 34, 5, 89, 4, 2, 5, 78, 89, 78, 78, 78,78]        #lista int
my_unsorted_list.sort()
print(my_unsorted_list)             #[2, 4, 5, 5, 5, 8, 34, 78, 78, 78, 78, 78, 89, 89]

#my_unsorted_list_complex = [5j, 1+4j, 5+6j, 12j]
#my_unsorted_list_complex.sort()
#print(my_unsorted_list_complex)

#count(element) - returneaza de cate ori se afla elementul element in lista
print(my_unsorted_list.count(78))   #78 - 5 ori

#concatenarea list_3 = list_1 + list_2
my_list_2 = my_list + my_list1
print(my_list_2)                    #[-20.75, 500, (4+5j), 2, 6, 500]
#concatenarea list_1.extend(list_2)
my_unsorted_list.extend(my_list_2)
print(my_unsorted_list)             #[2, 4, 5, 5, 5, 8, 34, 78, 78, 78, 78, 78, 89, 89, -20.75, 500, (4+5j), 2, 6, 500]
