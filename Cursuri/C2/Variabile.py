#rulare SHIFT + F10
#capitolul VARIABILE + Siruri de caractere

#Python foloseste notarea snake_case
#variabilele poate sa contina orice caracter dintre a-z, A-Z, 0-9 si semnul _(underscore)
# Python este un limbag case-sensitive

#legal variabile names:
myvar = "myvar"
my_var = "my_var"
_my_var = "_my_var"
myVar = "myVar"
MYVAR = "MYVAR "
myvar2 = "myvar2"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Illegal variable name:
#2myvar = "2myvar"      #eroare
#my-var = "my-var"      #eroare
#my var = "my var"      #eroare

#**********************************************************************************************************************#
#                                               Asignarea
#**********************************************************************************************************************#

my_var = 5                           #my_var va avea valoarea 3
print(my_var)

child_age = 5
print(id(child_age))            #arata ID-ul unic pt child_age

print('my_var: ', my_var)
my_var += 3                     #echivalent cu my_var = my_var + 3 (5 + 3 = 8)
print('my_var += 3 =>',my_var)
my_var *= 2                     #my_var = my_var(8) * 2    (8 * 2 = 16)
print('my_var *= 2 =>', my_var)
my_var >>= 4                    #my_var = my_var(16) >> 4   16 >> 4 = 1 0000 >> 4 = 00001(1 in decimal)
print('my_var >>= 4 =>', my_var)
my_var <<= 3                    #my_car = my_var(1) << 3    1 << 3 = 0001 << 3 = 1000(8 in decimal)
print('my_var <<= 3  =>', my_var)


#**********************************************************************************************************************#
#                                               Siruri de caractere
#**********************************************************************************************************************#

#tipul de date folosit pt siruri de caractere este string
#este definit intre ' ' sau " "

my_message = "Python  - Siruri de caractere"
print(my_message)

#in python nu exista notiunea de caracter
#un caracter poate fi reprezentat ca fiind un sir de caractere format dintr-un singur caracter
my_char = "a"
print(my_char)

#sir de caractere gol:
my_empty_string = ""
print(my_empty_string)


#ord() - se obtine codul ASCII al unui caracter
print(ord('a'))

#chr() - pentru a obtine caracterul reprezentat de un cod ASCII
print(chr(66))  # 66 - B

#**********************************************************************************************************************#
#Siruri de caractere - escaping
#Escape sequence   | Meaning
#   \newline       | Ignored
#   \\             | Backslash(\)
#   \'             | Single quote(')
#   \"             | Double quote(")
#   \a             | ASCII Bell(BEL)
#   \b             | ASCII Backspace(BS)
#   \f             | ASCII Formfeed(FF)
#   \n             | ASCII Linefeed(LF)
#   \r             | ASCII Carriage Return(CR)
#   \t             | ASCII Horizontal Tab(TAB)
#   \v             | ASCII Vertical Tab(VT)
#   \000           | ASCII character with octal value 000
#   \xhh           | ASCII character with hex value hh..

print("Python - \\")
print("Python - \'")
print("Python - \a")
print("Python - \b")
print("Python - \t s")

#folosirea caracterului newline \n
print("Somnoroase pasarele \nPe la cuiburi se aduna, \nSe ascund in ramurele \nNoapte buna!")

#folosirea ghilimelelor triple(simple sau duble)
print("""Somnoroase pasarele
Pe la cuiburi se aduna
Se ascund in ramurele - 
Noapte buna!""")

#raw string - putem afisa mesajul asa cum arata, fara a fi nevoiti sa facem escape caracterului \n
#pentru definirea unui raw string vom prefixa string-ul nostru cu caracterul r sau R
print(r"Somnoroase pasarele \nPe la cuiburi se aduna, \nSe ascund in ramurele \nNoapte buna!")
print(r"Python - \\")       #Python - \\
print(r"Python - \'")       #Python - \'
print(r"Python - \a")       #Python - \a
print(r"Python - \b")       #Python - \b
print(r"Python - \t s")     #Python - \t s

#**********************************************************************************************************************#
#Siruri de caractere - formatting
#format() - definirea placehorlderului se face intre {}
print("For only {price:.2f} dollars! {cheers_msg}".format(price = 49, cheers_msg = "Have a nice day!"))
print("For only {0:.2f} dollars!{1}".format(49, "Have a nice day!"))
print("For only {:.2f} dollars! {}".format(49, "Have a nice day!"))

print(F'For only {49:.2f} dollars! {"Have a nice day!"}')
