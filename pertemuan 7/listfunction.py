
# Nama File: listfunction.py
# Deskripsi : listfunction
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: 30/10/2024


# +=========================================================================+ #
#                           REALISASI KONSTRUKTOR
# +=========================================================================+ #

#Konso: elemen, List -> List
def konso(e, L):
    return [e] + L

#Konso: List, elemen -> List
def konsi(L, e):
    return L + [e]

# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

print("Hasil Konso:", konso(1,[2,3,4,5]))
print("Hasil Konso:", konsi([1,2,3,4],5))