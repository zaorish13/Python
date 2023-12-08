#rulare program SHIFT + F10

#Hello world, sfantul clasic:))
print("Hello, World!")

#TIP DE DATA

print(type(5))              #interger
print(type(-500))           #integer

print(type(.25))            #float
print(type(-7.65))          #float
print(type(8.46315))        #float
print(type(-4e3))           #float

print(type(1j))             #complex
print(type(3+5j))           #complex

#**********************************************************************************************************************#
#Operatori aritmetici
#adunare(+)
print(5 + 2)                #int

#scadere(-)
print(5 - 7)                #int
print(3.2 - 5)              #rezulta float -1.79

#inmultire(*)
print(3 * 4)                #int
print(12.5 * 5j)            #complex 62.5j
print(2.5*(3+5j))           #complex (7.5 + 12.5j)

#modulo(%) - restul impartii unei valori la o alta valoare
print(7 % 4)                #3
#print(5 % 5j)              #eroare
#print(6 % (6 + 2j))        #eroare
print(3 % 11.5)             #3.0

#ridicare la putere(**)
print(2 ** 4)               #16
print(3.5 ** 3.2)           #55.08
print(5 ** -5)              #0.00032
print(5j ** 2)              #(-25+0j)
print(5j ** (2+3j))         #(-0.02... + 0.22...j)

#impartirea exacta(//) - Catul impartirii a doua valorii

print(7 // 4)               #1
print(-12.5 // 3.5)         #-4
#print(2 // 5j)             #eroare
#print(3j // 2)             #eroare
#print(25j // (2.3 + 6j))   #eroare

#**********************************************************************************************************************#
#Operatori de comparare BOOLEAN
    #True - daca rezultatul comparatiei are valoare de adevar
    #False - dca rezultatul comparatiei nu are valoare de adevar
#egalitate(==)
print(5 == 5)               #True
print((2 + 5j) == (1 + 6j)) #False
print(-3.5 == 5j)           #False

#inegalitate(!=)
print(7 != (12j))           #True
print(-3.5 != 5)            #True
print(7 != 7)               #False
print(5j != (1+6j))         #True

#mai mare(>)
print(-25 > -25.0000001)    #True
#print(5j > (1+6j))         #eroare nu compara in complex

#mai mic(<)
#print(5j < 5j)             #eroare nu compara in complex
#print(5j < 5)              #eroare nu compara complex cu int
print(5 < 5)                #False

#mai mare sau egal(>=)
#print(5j >= 5j)            #eroare nu se poate compara in complex
print(5 >= 9)               #False
#print(25 >= (1+1j))        #eroare nu se poate compara complex cu int

#mai mic sau egal(<=)
#print(5j <= 5j)            #eroare nu se poate compara in complex
print(5 <= .25)             #False

#**********************************************************************************************************************#
#Operatori logici - sunt folositi pentru combinarea rezultatelor obtinute in urma conditiilor

#and(SI LOGIC) - este evaluata ca True daca ambele conditii sunt indeplinite, altfel este evaluata ca False
print(4 > 5 and 6 > 6)      # 0 and 0 => 0(False)
print(4 > 5 and 6 == 6)     # 0 and 1 => 0(False)
print(4 < 5 and 6 > 6)      # 1 and 0 => 0(False)
print(4 < 5 and 5 < 7)      # 1 and 1 => 1(True)

#or(SAU LOGIC) - este evaluata ca True daca cel putin o conditie este adevarata, altfel este evaluata ca False
print(4 > 5 or 17 > 35.5)   # 0 or 0 => 0(False)
print(4 > 5 or 6 == 6)      # 0 or 1 => 1(True)
print(4 < 5 or 6 > 6)       # 1 or 0 => 1(True)
print(4 < 5 or 6 == 6)      # 1 or 1 => 1(True)

#not(NEGARE) - este evaluata ca True daca valoarea din stanga este mai mare decat valoarea din dreapta,
#              altfel este evaluata ca False
print(not(4 < 6 and 4 > 2))     #False
print(not(4 > 5 or 17 > 35.5))  #True

#**********************************************************************************************************************#
#Operatori de apartenenta - sunt folositi pentru verificarea existentei unei secvente in cadrul unui obiect
#in - este evaluata ca True daca secventa face parte din obiectm altfel este evaluata ca False
print(1 in [1, 2, 3])           #True
print(2 in [2j, 1+5j, 6+2j])    #False
print('a' in 'alfabet')         #True
print('Z' in 'Antimatter')      #False

#not in - este evaluata ca True daca secventa evaluata nu face parte din obiect, altfel este evaluata ca False
print(1 not in [1, 2, 3])           #False
print(2 not in [2j, 1+5j, 6+2j])    #True
print('a' not in 'alfabet')         #False
print('Z' not in 'Antimatter')      #True

#**********************************************************************************************************************#
#Operatori pe biti
#       Informatia intr-un calculator este reprezentata in baza 2
#       Inseamna ca orice informatie este reprezentata printr-o secventa pe biti ce pot avea fie valoarea 0, fie 1

#   &(AND) - seteaza fiecare bit cu valoarea 1 daca ambii biti au valoarea 1, altfel seteaza valoarea 0
#   a & b   &(AND)
#   0 & 0 = 0
#   1 & 0 = 0
#   0 & 1 = 0
#   1 & 1 = 1

print(10 & 6)           #2

#10 = 1010
# 6 = 0110
#10 & 6 = 1010 & 0110 = 0010(2 in decimal)

#   |(OR) - seteaza fiecare bit cu valoarea 1 daca cel putin unul din biti este 1, altfel seteaza valoarea 0
#   a | b   |(OR)
#   0 | 0 = 0
#   1 | 0 = 1
#   0 | 1 = 1
#   1 | 1 = 1

print(10 | 6)           #14

#10 = 1010
# 6 = 0010
#10 | 6 = 1010 | 0110 = 1110(14 in decimal)

#   ^(XOR) - seteaza fiecare bit cu 1 daca cel putin unul din biti este 1, altfel seteaza valoarea 0
#   a ^ b   ^(XOR)
#   0 ^ 0 = 0
#   1 ^ 0 = 1
#   0 ^ 1 = 1
#   1 ^ 1 = 0

print(10 ^  6)          #12
#10 = 1010
# 6 = 0010
#10 ^ 6 = 1010 ^ 0110 = 1100(12 in decimal)

# ~(NOT) - schimba valoare tuturor bitilor
# ~0 = 1
# ~1 = 0
print(~10)              #-11
#10 = 1010
#se foloseste complementul lui 2
#la valoarea 1010 se aduna 1 => 1011(-11 in decimal)
#~10 = ~1010 = 1011(-11 in decimal)

# <<(left shift) - adauga biti cu valoarea 0 la finalul secventei

print(10 << 2)          #40
#10 = 1010
#10 << 2 = 1010 << 2 = 101000

#32 16  8  4  2  1  *
# 1  0  1  0  0  0
#__________________
#32  0  8  0  0  0 = 40

# >>(right shift) - elimina biti de la finalul secventei

print(10 >> 2)          #2
#10 = 1010
#10 >> 2 = 1010 >> 2 = 0010


