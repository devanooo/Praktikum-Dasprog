# Nama File: treeNaire_24060124140149.py
# Deskripsi : Tree 
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: Rabu, 20 November 2024s

from LISTTOTAL import *

# DEFINSI DAN SPESIFIKASI KONSTRUKTOR
def MakePN(A,PN):
    return [A,PN]

# DEFINISI DAN SPESIFIKASI SELEKTOR
def akar(PN):
    return PN[0]

def anak(PN):
    return PN[1]

# DEFINISI DAN SPESIFIKASI 
def IsTreeNEmpty(PN):
    return PN == []

def IsOneElmt(PN):
    return (IsTreeNEmpty(PN) == False) and (IsTreeNEmpty(anak(PN)) == True)

def NBElmtChild(PN):
    if IsTreeNEmpty(PN):
        return 

def NBNElmt(PN):
    if IsTreeNEmpty(PN):
        return 0
    elif IsOneElmt(PN):
        return 1
    else:
        return 1 + NBNElmt(anak(PN)[0]) + NBNElmtChild(anak(PN)[1:])

def NBNElmtChild(PN):
    if IsTreeNEmpty(PN):
        return 0
    else:
        return NBNElmt(PN[0]) + NBNElmtChild(PN[1:])

def NBNDaun(PN):
    if IsTreeNEmpty(PN):
        return 0
    elif IsOneElmt(PN) and IsTreeNEmpty(anak(PN)):
        return 1
    else:
        return NBNDaunChild(anak(PN))
    
def NBNDaunChild(PN):
    if IsTreeNEmpty(PN):
        return 0
    else:
        return NBNDaun(PN[0]) + NBNDaunChild(PN[1:])

# APLIKASI
T = MakePN(2, [])
print(MakePN(2, []))
print(IsTreeNEmpty(T))
print(IsOneElmt(T))
T2 = MakePN('A', [MakePN('B', [MakePN('D', []), MakePN('E', []), MakePN('F', [])]), MakePN('C', [MakePN('G', [])]), MakePN('H', [MakePN('I', [])])])
print(T2)
print(NBNElmt(T2))
print(NBNDaun(T2))