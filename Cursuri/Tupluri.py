#rulare SHIFT + F10

#**********************************************************************************************************************#
#                                               TUPLURI
#**********************************************************************************************************************#

#ocupa mai putin spatiu decat o lista
print(().__sizeof__())          #tupla              24biti
print([].__sizeof__())          #lista              40biti
print({}.__sizeof__())          #dictionar          48biti
#este o structura de date ordonata si nu poate fi modificata
#permite elemente duplicate
#definita prin ()
#permite sliceing, concatenarea(+) ca listele
#nu permite: adaugarea sau stergerea

my_tuple = (1, 7, -3, 'a', 2+3j, True, None, False)
print(my_tuple)                 #(1, 7, -3, 'a', (2+3j), True, None, False)
print(my_tuple.count('a'))      #1
print(my_tuple.index('a'))      #3

#ex pt folosirea tuplului este definirea lunilor din an
months_of_year = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
print(months_of_year)

#**********************************************************************************************************************#
#                                               DICTIONARE
#**********************************************************************************************************************#

#este o structura de date neordonata, poate fi schimbata si indexata
#reprezentarea se face cheie:valoare
#este definita folosind {}
#cheile sunt unice si pot exista valori duplicate
my_dictionary = {
    "key_1": 12,
    "Key_2": 4+5j,
    "Key_3": 12,
    3: True,
    4: None,
    5+2j: '',
    ("key_5", 6):[1, 2, 3],
    -8: ('First', 'Second', 'Third')
}
print(my_dictionary)

#accesarea se face prin:
#cheie, dar daca nu exista cheia in dictionar va genera eroare
print(my_dictionary["key_1"])       #12
#print(my_dictionary["key_4"])      #eroare

#.get() - se poate defini o valoare default daca cheia nu exista. Metoda va intoarce NONE daca cheia nu exista
print("my_dictionary.get(\"key_1\"): ", my_dictionary.get("key_1"))   #12
print("my_dictionary.get(\"key_4\"): ",my_dictionary.get("key_4"))   #None

#**********************************#
#           Metode                 #
#**********************************#
#clear() - goleste dictionarul
my_dict = {
    "key_1": "My value"
}
print(my_dict)                          #{'key_1': 'My value'}
my_dict_1 = my_dict.clear()
print("my_dict.clear() = ", my_dict_1)    #{}

#copy() - returneaza o copie a dictionarului
print(my_dict.copy())
print(my_dictionary.copy())

#keys() - returneaza un dict_keys continand toate valorile dintr-un dictionar
print(my_dictionary.keys())
#dict_keys(['key_1', 'Key_2', 'Key_3', 3, 4, (5+2j), ('key_5', 6), -8])

#values() - returneaza un dict_items continand toate elementele dictionarului
#Un astfel de element reprezinta un tuplu de forma(cheie, valoare)
print(my_dictionary.items())
#dict_items([('key_1', 12), ('Key_2', (4+5j)), ('Key_3', 12), (3, True), (4, None), ((5+2j), ''), (('key_5', 6), [1, 2, 3]), (-8, ('First', 'Second', 'Third'))])

#pop(key) - scoate din dictionar cheia key
my_dictionary_1 = my_dictionary.copy()
print(my_dictionary_1)
my_dictionary_1.pop(-8)
print(my_dictionary_1)
#{'key_1': 12, 'Key_2': (4+5j), 'Key_3': 12, 3: True, 4: None, (5+2j): '', ('key_5', 6): [1, 2, 3]}

#popiten() - scoate din dictionar ultimul element introdus
my_dictionary_1.popitem()
print(my_dictionary_1)
#{'key_1': 12, 'Key_2': (4+5j), 'Key_3': 12, 3: True, 4: None, (5+2j): ''}

#**********************************************************************************************************************#
#                                               SETURI
#**********************************************************************************************************************#

#este o colectie de date neordobata, nu poate fi modificata si neindexata
#este definita prin {}
#elementele sunt unice
#accesarea unui element din set nu este posibila, dar poate fi parsat
#pt eliminare se folosesc metodele remove() sau discard(), poate fi folosita si metoda pop()
#metoda clear() este folosita pt golirea setului
#pt concatenarea se foloseste metoda union() sau update()
#alte metode uzuale sunt intersestion(), issubset(), issuperset()
