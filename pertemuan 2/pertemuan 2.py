def kuadrat(x):
    return x*x

def isorigin(x,y):
    return (x==0 and y==0)

def max2(a,b):
    return((a+b) + abs (a-b)) //2

def max3(a,b,c):
    return max2(max2(a,b),c)

print(kuadrat(2))
print(isorigin(2,3))
print(isorigin(0,0))
print(max2(1,2))
print(max3(3,6,7))


angka = 1230
desimal = 3.14
karakter = 'a'
teks = "makan ayam goreng enak"
bool = True
masukan = input("Masukkan Text : ")

print(angka)
print(desimal)
print(karakter)
print(teks, bool)
print(masukan, "Berhasil dicetak")