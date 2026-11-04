# 1. Napisati program kojim se prevodi temperatura iz Celzijusove skale u Farenhajtovu skalu,
# ako je odgovarajuca formula oblika T [◦F] = T [◦C] · 1.80 + 32. Na ulazu se unosi vrednost
# temperature u stepenima Celzijusa (realan broj) a ispisuje se vrednost temperature u stepenima
# Farenhajta.

def temperature_F(celsius):
    return celsius * 1.8 + 32

print(temperature_F(10))
print(temperature_F(-10))


# 2. Napisati program koji za uneti redni broj dana u nedelji (od 1 do 7) ispisuje naziv tog
# dana (ponedeljak - nedelja). Ukoliko je unet broj koji nije izmed¯u 1 i 7, ispisati Pogresan
# unos.

weekdays = ['Ponedeljak', 'Utorak', 'Sreda', 'Cetvrtak', 'Petak', 'Subota', 'Nedelja']

def weekday(rn):
    if rn >= 8 or rn < 1 :
         return 'Pogresan unos'
    return weekdays[rn-1]

print(weekday(1))    
print(weekday(6))
print(weekday(12))
print(weekday(-2))
print(weekday(3))


# 3. Napisati program koji racuna najveci negativni element u listi.

lista = [-3, 0, -1, 8, -9, 7, 15, -8, 16, -7]
lista_pozitivnih = [2, 10, 12, 4, 82]

def max_negative(lista):
    n = len(lista)
    max = min(lista)
   # print(max)
    for i in range(0, n) :
        if lista[i] < 0 and max < lista[i] :
            max = lista[i]
    if max >= 0 :
        return None
    else :
        return max   

max_negative(lista)
#max_negative(lista_pozitivnih)


# 5. Napisati program koji racuna broj parnih elemenata date liste.

lista1 = [2, 12, 9, -7, 3, 13, 18, 22, 41, 14, 11]
lista_neparnih = [1, 13, 17, 9, 3, 7]

def even(a):
    n = len(a)
    brojac = 0
    for i in range(0, n) :
        if a[i] % 2 == 0 :
            brojac = brojac + 1
    return brojac

even(lista1)
#even(lista_neparnih)


# 6. Napisati program koji racuna sume elemenata liste celih brojeva koji su deljivi sa 2 odnosno sa 3.

lista2 = [1, 2, 3, 4, 6, 7, 9, 12]

def sume_23(l):
    n = len(l)
    sum_2 = 0
    sum_3 = 0
    for i in range(0, n) :
        if l[i] % 2 == 0 and l[i] % 3 == 0 :
            sum_2 = sum_2 + l[i]
            sum_3 = sum_3 + l[i]
        elif l[i] % 2 == 0 and l[i] % 3 != 0 :
            sum_2 = sum_2 + l[i]
        elif l[i] % 2 != 0 and l[i] % 3 == 0 :
            sum_3 = sum_3 + l[i]
    return (sum_2, sum_3)

print(sume_23(lista2))