# Nama File: kondisional.py
# Deskripsi : 
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: / /

# +=========================================================================+ #
#                           Definisi dan Spesifikasi
# +=========================================================================+ #

# max2(a,b) = 2 integer -> integer
# {max2(a,b) menentukan bilangan terbesar antara a dan b ,sebuah integer}

# max(a,b) : 2integer -> integer 
# {max(a,b)} 

# max3(a,b,c) : 3 integer -> integer
# {pilih}

# max3lagi(a,b,c) : 3 integer -> integer

# max3lagi2(a,b,c) : 3 integer -> integer
# +=========================================================================+ #
#                               Realisasi
# +=========================================================================+ #

def max2(a,b):
    if a >= b:
        return a
    else :
        return b
    
def max(a,b):
    return(a if a >= b else b)

def max3(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > b and c > a:
        return c

def max3lagi(a,b,c):
    if a > b:
        if a > c:
            return a
        else: 
            return c
    else:
        if b > c:
            return b
        else :
            return c

def max3lagi2(a,b,c):
    if a > b:
        return(a if a > c else c)
    else : 
        return(b if b > c else c)

# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

print("===max2===") 
print("Maksimum dari 10 dan 7 adalah", max2(10,7))
print("Maksimum dari 20 dan 20 adalah", max2(20,20))
print("Maksimum dari 3 dan 5 adalah", max2(3,5))

print("\n==max==")
print("Maksimum dari 10 dan 7 adalah", max(10,7))
print("Maksimum dari 20 dan 20 adalah", max(20,20))
print("Maksimum dari 3 dan 5 adalah", max(3,5))

print("\n==max3==")
print("Maksimum dari 10,7,15 adalah", max3(10,7,15))
print("Maksimum dari 20,20,20 adalah", max3(20,20,20))
print("Maksimum dari 3,5,200 adalah", max3(5,200,190))

print("\n==max3lagi==")
print("Maksimum dari 10,7,15 adalah", max3lagi(10,7,15))
print("Maksimum dari 20,20,20 adalah", max3lagi(20,20,20))
print("Maksimum dari 3,5,200 adalah", max3lagi(5,200,190))

print("\n==max3lagi==")
print("Maksimum dari 10,7,15 adalah", max3lagi2(10,7,15))
print("Maksimum dari 20,20,20 adalah", max3lagi2(20,20,20))
print("Maksimum dari 3,5,200 adalah", max3lagi2(5,200,190))

