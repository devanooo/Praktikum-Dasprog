# Nama File: treeNaire_24060124140149.py
# Deskripsi : 
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: / /
from LISTTOTAL import *



# +=========================================================================+ #
#                    Definisi dan Spesifikasi Konstruktor
# +=========================================================================+ #

def makePN(A,PN):
    return [A,PN]
# +=========================================================================+ #
#                    Definisi dan Spesifikasi Selektor
# +=========================================================================+ #

def akar(PN):
    return PN[0]

def anak(PN):
    return PN[1]

# +=========================================================================+ #
#                    Definisi dan Spesifikasi Predikat
# +=========================================================================+ #

def isTreeEmpty(PN):
    return PN == []

def isOneElmnt(PN):
    return (isTreeEmpty(PN) == False) and (isTreeEmpty(anak(PN)) == True)

def NbNElmnt(PN):
    if isTreeEmpty(PN):
        return 0
    elif isOneElmnt(PN):
        return 1
    else: return 1 + NbNElmnt(anak(PN)[0]) + NbElmntChild(anak(PN)[1:])
    
def NbElmntChild(PN):
    if isTreeEmpty(PN):
        return 0
    else:
        return NbNElmnt(PN) + NbElmntChild(PN[1:])
    
def NbNDaun(PN):
    if isTreeEmpty(PN):
        return 0
    if isOneElmnt(PN):
        return 1
    else:
        return NbNDaunChild(anak(PN))
    
def NbNDaunChild(PN):
    if isTreeEmpty(PN):
        return 0
    
    return NbNDaun(PN[0]) + NbNDaunChild(PN[1:])


# +=========================================================================+ #
#                               Realisasi
# +=========================================================================+ #


# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

T = makePN(2,[])

print(makePN(2,[]))
print(isTreeEmpty(T))
print(isOneElmnt(T))

T2 = makePN('A', [makePN('B', [makePN('D', []), makePN('E', []), makePN('F', [])]), makePN('C', [makePN('G', [])]), makePN('H', [makePN('I', [])])])
print(T2)
print(NbNElmnt(T2))
print(NbNDaun(T2))