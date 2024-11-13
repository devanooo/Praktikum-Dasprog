# Program     : listFunctions.py
# Deskripsi   : Fungsi-fungsi untuk operasi list.
# NIM/Nama    : 24060123120008/Irvino Kent Setiawan
# Tanggal     : 23/10/2024


# REALISASI KONSTRUKTOR
# Konso: elemen, List -> List
def Konso(e, L):
    return [e] + L

# Konsi: List, elemen -> List
def Konsi(L, e):
    return L + [e]


# REALISASI PREDIKAT
# IsEmpty: List -> boolean
def IsEmpty(L):
    return L == []

# IsOneElmt: List -> boolean
def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []


# REALISASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
def FirstElmt(L):
    return L[0]

def FirstElmt(L):
    if IsEmpty(L):
        return None
    else:
        return L[0]

# Last Elmt: List tidak kosong -> elemen
def LastElmt(L):
    return L[-1]

def LastElmt(L):
    if IsEmpty(L):
        return None
    else:
        return L[-1]

# Tail: List tidak kosong -> List


def Tail(L):
    if IsEmpty(L):
        return []
    else:
        return L[1:]

# Head: List tidak kosong -> List


def Head(L):
    if IsEmpty(L):
        return []
    else:
        return L[:-1]


# REALISASI OPERATOR
# NbElmt: List -> integer
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

# ElmtkeN: integer >= 0, List -> elemen


# IsMember: elemen, List -> boolean


# Copy: List -> List


# Inverse: List -> List
# udah

# Konkat: 2 List -> List


# SumElmt: List of integer -> integer
def SumElmnt(L):
    if IsEmpty(L):
        return 0
    else: FirstElmt(L) + SumElmnt(Tail(L))
print(SumElmnt([1,2,3]))
# AvgElmt: List of integer -> integer


# MaxElmt: List of integer -> integer


# MaxNB: List of integer -> <integer, integer>


# AddList: 2 List of integer -> List of integer


# IsPalindrom: List of character -> boolean


# APLIKASI
# print("Hasil Konso:", Konso(1, [2, 3, 4, 5]))
# print("Hasil Konsi:", Konsi([1, 2, 3, 4], 5))

# print("\nHasil FirstElmt:", FirstElmt([]))
# print("Hasil FirstElmt:", FirstElmt([1, 2, 3, 4, 5]))
# # print("Hasil LastElmt:", LastElmt([]))
# # print("Hasil LastElmt:", LastElmt([1, 2, 3, 4, 5]))

# # print("\nHasil Tail:", Tail([]))
# # print("Hasil Tail:", Tail([1, 2, 3, 4, 5]))
# # print("Hasil Head:", Head([]))
# print("Hasil Head:", Head([1, 2, 3, 4, 5]))

# print("\nHasil IsEmpty:", IsEmpty([]))
# print("Hasil IsEmpty:", IsEmpty([1, 2, 3, 4, 5]))
# print("Hasil IsOneElmt:", IsOneElmt([]))
# print("Hasil IsOneElmt:", IsOneElmt([1]))
# print("Hasil IsOneElmt:", IsOneElmt([1, 2, 3, 4, 5]))

# print("\nHasil NbElmt:", NbElmt([]))
# print("Hasil NbElmt:", NbElmt([0]))
# print("Hasil NbElmt:", NbElmt([1, 1, 1, 1, 1]))
# print("Hasil NbElmt:", NbElmt([1, 2, 3, 4, 5]))

