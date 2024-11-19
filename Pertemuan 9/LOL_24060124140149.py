# Nama File: LOL_24060124140149.py
# Deskripsi : List Of list 
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: 13/11/2024

from listfunction import *
from set_24060124140149 import *

# +=========================================================================+ #
#                         Definisi dan spesifikasi Selektor
# +=========================================================================+ #

#FirstList : list of list tidak kosong -> list
def FirstList(S):
    if Isempty(S):
        return None
    else:
        return S[0]
#LastList : list of list tidak kosong -> list
def LastList(S):
    if Isempty(S):
        return None
    else:
        return S[-1]
# TailList : List of list tida kosong -> 
def TailList(S):
    if Isempty(S):
        return []
    else: 
        return S[1:]
# HeadList : list of list tidak kosong -> list of lisg
def HeadList(S):
    if Isempty(S):
        return[]
    else:
        return S[:-1]


# +=========================================================================+ #
#               Definisi Spesifikasi Konstruktor
# +=========================================================================+ #

def KonsLo(L,S):
    return [L] + S

def KonsLi(S,L):
    return S + [L]

# +=========================================================================+ #
#                           Definisi dan Spesifikasi Predikat
# +=========================================================================+ #

# IsAtom : Elemen -> boolean
def IsAtom(L):
    return type(L) != list

# IsList : list of list -> boolean
def IsList(L):
    return type(L) == list

# IsMemberS: elemen, list of list -> boolean
def IsmemberS(x,S):
    if FirstList(S) == x:
        return True
    elif Isempty(S):
        return False
    else:
        return IsmemberS(x,TailList(S))

# +=========================================================================+ #
#               Definisi Spesifikasi Operator
# +=========================================================================+ #

# Rember: elemen, list of list -> list of list
def RemberL(x,L):
    if IsMember(x,L) == False:
        return L
    if Isempty(L):
        return L
    else:
        if FirstList(L) == x:
            return RemberL(x,Tail(L))
        elif IsList(FirstList(L)) and IsMember(x,FirstList(L)):
            return KonsLo(RemberL(x,FirstList(L)),RemberL(x,TailList(L)))
        else:
            return KonsLo(FirstList(L),RemberL(x,TailList(L)))    

# Max: list of list -> elemen
def Max(S):
    if Isempty(S):
        return S
    if isoneelemet(S):
        if IsAtom(FirstElmnt(S)):
            return FirstElmnt(S)
        else:
            return Max(FirstElmnt(S))
    else:
        if IsAtom(FirstElmnt(S)) and IsAtom(FirstElmnt(Tail(S))):
            if FirstElmnt(S) >= FirstElmnt(Tail(S)):
                return Max(konso(FirstElmnt(S),Tail(Tail(S))))
            else:
                return Max(Tail(S))
        elif not IsAtom(FirstElmnt(S)) and not IsAtom(FirstElmnt(Tail(S))):
            return Max(konso(Max(FirstElmnt(S) + FirstElmnt(TailList(S))),Tail(Tail(S))))
        elif IsAtom(FirstElmnt(S)) and not IsAtom(FirstElmnt(Tail(S))):
            return Max(konso(Max(konso(FirstElmnt(S),FirstElmnt(Tail(S)))),Tail(Tail(S))))
        else:
            return Max(konso(Max(konso(FirstElmnt(Tail(S)),FirstElmnt(S))),Tail(Tail(S))))

# NBElmtAtom(S): list of list -> integer
def NBElmtAtom(S):
    if Isempty(S):
        return 0
    else:
        if IsAtom(FirstElmnt(S)):
            return 1 + NBElmtAtom(Tail(S))
        else:
            return NBElmtAtom(Tail(S))

# NBElmtList(S): list of list -> integer
def NBElmtList(S):
    if Isempty(S):
        return 0
    else:
        if not IsAtom(FirstElmnt(S)):
            return 1 + NBElmtList(Tail(S))
        else:
            return NBElmtList(Tail(S))
        

# SumLoL: list of list -> integer
def SumLoL(S):
    if Isempty(S):
        return 0
    else:
        if IsAtom(FirstElmnt(S)):
            return FirstElmnt(S) + SumLoL(Tail(S))
        else:
            return SumLoL(FirstElmnt(S)) + SumLoL(Tail(S))
    

# MaxNBElmtList(S): list of list -> integer
def MaxNBElmtList(S):
    if Isempty(S):
        return 0
    else:
        if IsAtom(FirstElmnt(S)):
            return MaxNBElmtList(TailList(S))
        else:
            return max(NBElmtAtom(FirstElmnt(S)),MaxNBElmtList(Tail(S)))
        

# MaxSumElmt(S): list of list -> integer
def MaxSumElmt(S):
    if Isempty(S):
        return 0
    else:
        if IsAtom(FirstElmnt(S)):
            return max(FirstElmnt(S),MaxSumElmt(Tail(S)))
        else:
            return max(SumLoL(FirstElmnt(S)),MaxSumElmt(Tail(S)))
        

# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

print(KonsLo(1, [[1,2,3],[4,5,6]]))
print(KonsLo([1,2,2], [[1,2,3],[4,5,6]]))

print(KonsLi([[1,2,3],[4,5,6]],1))
print(KonsLi([[1,2,3],[4,5,6]], [1,2,2]))

print(FirstList([[1,2,3],[4,5,6]]))
print(FirstList([]))
print(LastList([]))
print(LastList([[1,2,3],[4,5,6]]))
print(TailList([[1,2,3],[4,5,6],1,2,[]]))
print(HeadList([[1,2,3],[4,5,6],1,2,[]]))

print(Isempty([]))
print(Isempty([1]))
print(IsAtom([1]))
print(IsAtom(1))

print("MaxsUm",MaxSumElmt([1,3,[1],2,[12,300],4,[12],313,6]))
print("MaxsUm",MaxSumElmt([1,3,[1],2,[12,300],4,[12],3,6]))
print("MaxNbekemnohnlist",MaxNBElmtList([1,3,[1],2,[12],4,[12],5,6]))
print("SumLOL",SumLoL([1,3,[1],2,[12],4,5,6]))
print("NBelementlist",NBElmtList([1,3,[1],2,[12],4,5,6]))
print("NBelementatom",NBElmtAtom([1,3,[1],2,[12],4,5,6]))
print("max",Max([1,3,[1],2,[12]]))
print("ismembers",IsmemberS([3],[1,2,3,[3]]))
print("rember",rember([3],[1,3,[1],2,[3]]))
