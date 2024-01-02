#rulare SHIFT + F10

#1   Să se scrie o funcție care primește un număr nedefinit de parametrii și
    #să se calculeze suma parametrilor care reprezintă numere întregi sau reale.

def your_function(*args, **kwargs):

    suma = 0
    for parametru in args:
        if isinstance(parametru, (int, float)):
            suma = suma + parametru

    return suma

print(your_function(1, 5, -3, 'abx', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1 = 2))

#2   Să se scrie o funcție recursivă care primește ca parametru o lista cu numere întregi și returnează:

#suma totala a numerelor
def suma_numerelor(lista):
    if not lista:
        return 0, 0, 0

    total = lista[0]
    suma_para = 0
    suma_impara = 0

    if total % 2 == 0:
        suma_para = total
    else:
        suma_impara = total
    suma_totala, subtotal_suma_para, subtotal_suma_impara = suma_numerelor(lista[1:])
    return total + suma_totala, suma_para + subtotal_suma_para, suma_impara + subtotal_suma_impara


lista_mea = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total_sum, suma_para, suma_impara = suma_numerelor(lista_mea)

print(f'Suma totala: {total_sum}')
print(f'Suma para: {suma_para}')
print(f'Suma impara: {suma_impara}')


#3 Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg,
# altfel returnează valoarea 0.

def citeste_intreg():
    try:
        valoare = int(input('Introduceti un numar: '))
        return valoare
    except ValueError:
        return 0

rezultat = citeste_intreg()
print(f'Valoarea introdusa este: {rezultat}')
