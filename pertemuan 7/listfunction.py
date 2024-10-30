
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
#                           REALISASI PREDIKAT
# +=========================================================================+ #
def Isempty(L):
    return L == []
        
def isoneelemet(L):
    if Isempty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []
# +=========================================================================+ #
#                           REALISASI SELEKTOR
# +=========================================================================+ #
def FirstElmnt(L):
    if Isempty(L):
        return None
    else : 
        return L[0]
def LastElmnt(L):
    if Isempty(L):
        return None
    else :return L[-1]
def Tail(L):
    if Isempty(L):
        return []
    else : return L[1:]
def Head(L):
    if Isempty(L):
        return []
    else : return L[:-1]
# +=========================================================================+ #
#                           REALISASI OPERATOR
# +=========================================================================+ #
# NbElmnt: List -> Integer
def NbElmnt(L):
    if Isempty(L):
        return 0
    else : 
        return 1 + NbElmnt(Tail(L))
# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

# print("Hasil Konso:", konso(1,[2,3,4,5]))
# print("Hasil Konso:", konsi([1,2,3,4],5))

# print("\nHasil IsEmpty :", Isempty([]))
# print("Hasil IsEmpty :", Isempty([1,2,3,4,5]))
# print("Hasil IsOneElement :", isoneelemet([]))
# print("Hasil IsOneElement :", isoneelemet([1]))
# print("Hasil IsOneElement :", isoneelemet([1,2,3,4,5]))

# print("\nHasil FirstElement :",FirstElmnt([])) 
# print("Hasil FirstElement :",FirstElmnt([1,2,3,4,5])) # - > 1
# print("\nHasil LastElement :",LastElmnt([])) 
# print("Hasil LastElement :",LastElmnt([1,2,3,4,5])) # - > 5

# print("\nHasil Tail: ",Tail([0]))
# print("Hasil Tail: ",Tail([1,2,3,4,5]))
# print("Hasil Head: ",Head([0]))
# print("Hasil Head: ",Head([1,2,3,4,5]))

# print("\nHasil NbElmnt: ",NbElmnt([]))
# print("Hasil NbElmnt: ",NbElmnt([0]))
# print("Hasil NbElmnt: ",NbElmnt([1,1,1,1,1]))
# print("Hasil NbElmnt: ",NbElmnt([1,2,3,4,5]))


