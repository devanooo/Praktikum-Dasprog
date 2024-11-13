# Nama File: set_24060124140149.py
# Deskripsi : Program yang bersii implementasi operasi-operasi himpunan
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: Rabu, 6 November 2024

from  listfunction import *

# +=========================================================================+ #
#       Realisasi Operasi list yang diperlukan untuk Himpunan
# +=========================================================================+ #

# Rember: elemen,list -> list
def rember(x,L):
    if Isempty(L):
        return []
    elif not IsMember(x,L):
        return L
    else:
        if FirstElmnt(L) == x:
                return Tail(L)
        else:
            return konso(FirstElmnt(L),rember(x,Tail(L)))
        
# Rember2: elemen,list -> list
def rember2(x,L):
    if Isempty(L):
        return []
    elif not IsMember(x,L):
        return L
    else:
        if LastElmnt(L) == x:
            return Head(L) 
        else:
            return konsi(rember2(x,Head(L)),LastElmnt(L))
        


# MultiRember: elemen, list -> list
def MultiRember(x,L):
    if Isempty(L):
        return []
    elif not IsMember(x,L):
        return L
    else: 
        if FirstElmnt(L) == x:
            return MultiRember(x,Tail(L))
        else:
            return konso(FirstElmnt(L),MultiRember(x,Tail(L)))



# makeset: List -> Set
def makeset(L):
    if Isempty(L):
        return []
    else: 
        if IsMember(FirstElmnt(L),Tail(L)):
            return makeset(Tail(L))
        else:
            return konso(FirstElmnt(L),makeset(Tail(L)))
# makeset2: List -> Set
def makeset2(L):
    if Isempty(L):
        return[]
    else:
        if IsMember(FirstElmnt(L), Tail(L)):
            return makeset(MultiRember(FirstElmnt,Tail(L)))
        else:
            return konso(FirstElmnt(L),makeset2(Tail(L)))
        


# konsoset: elemen,set -> set
def konsoset(e,H):
    if not IsMember(e,H):
        return konso(e,H)
    else:
        return H


# +=========================================================================+ #
#                               Realisasi Predikat
# +=========================================================================+ #
# IsSet2: List -> Boolean
def IsSet2(L):
    return NbElmnt(L) == NbElmnt(makeset2(L))

# IsSet: List -> Boolean
def IsSet(L):
    if Isempty(L):
        return True
    else:
        if IsMember(FirstElmnt(L),Tail(L)):
            return False
        else:
            return IsSet2(Tail(L))


# IsSubset: 2 Set -> Boolean
def IsSubset(H1,H2):
    if Isempty(H1):
        return True
    elif IsSet(H1) == False or IsSet(H2) == False:
        return False
    else:
        if IsMember(FirstElmnt(H1),H2):
            return IsSubset(Tail(H1),H2)
        else: 
            return False


# IsEqualSet1: 2 Set -> Boolean
def IsEqualSet1(H1,H2):
    if Isempty(H1) :
        return True
    elif (not Isempty(H1) and Isempty(H2)) or (Isempty(H1) and not Isempty(H2)):
        return False
    elif not IsSet(H1) or not IsSet(H2):
            return False
    else:
        if IsMember(FirstElmnt(H1),H2):
            return IsEqualSet1(Tail(H1),H2) 
        else: 
            return False

# IsEqualSet2: 2 Set -> Boolean
def IsEqualSet2(H1,H2):
    return IsSubset(H1,H2) and IsSubset(H2,H1)


# Isintersect : 2 Set -> Boolean
def Isintersect(H1,H2):
    if Isempty(H1) or Isempty(H2):
        return False
    else:
        if IsMember(FirstElmnt(H1),H2):
            return True
        else:
            return Isintersect(Tail(H1),H2)


# +=========================================================================+ #
#                        Realisasi Operator Terhadap Himpunan
# +=========================================================================+ #
# MakeIntersect1 : 2 Set -> set
def MakeIntersect1(H1,H2):
    if Isempty(H1) or Isempty(H2):
        return []
    else:
        if IsMember(FirstElmnt(H1),H2):
            return konso(FirstElmnt(H1),MakeIntersect1(Tail(H1),H2))
        else:
            return MakeIntersect1(Tail(H1),H2)


# MakeIntersect2 : 2 Set -> set

def MakeIntersect2(H1,H2):
    if Isempty(H1) or Isempty(H2):
        return []
    else:
        if IsMember(FirstElmnt(H2),H1):
            return konsi(MakeIntersect2(H1,Tail(H2)), FirstElmnt(H2))
        else:
            return MakeIntersect2(H1,Tail(H2))


#  MakeUnion1 : 2 Set -> set
def MakeUnion1(H1,H2):
    if Isempty(H1) and Isempty(H2):
        return []
    elif Isempty(H1) and not Isempty(H2):
        return H2
    elif not Isempty(H1) and Isempty(H2):
        return H1
    else:
        if IsMember(FirstElmnt(H1),H2):
            return MakeUnion1(Tail(H1),H2)
        else:
            return makeset(konso(FirstElmnt(H1),MakeUnion1(Tail(H1),H2)))

#  MakeUnion2 : 2 Set -> set
def MakeUnion2(H1,H2):
    if Isempty(H1) and Isempty(H2):
        return []
    elif Isempty(H1) and not Isempty(H2):
        return H2
    elif not Isempty(H1) and Isempty(H2):
        return H1
    else:
        if IsMember(FirstElmnt(H2),H1):
            return MakeUnion2(H1,Tail(H2))
        else:
            return makeset(konsi(MakeUnion2(H1,Tail(H2)), FirstElmnt(H2)))

#  NBUnion : 2 Set -> Integer
def NBUnion(H1,H2):
    if Isempty(H1) and Isempty(H2):
        return 0
    elif Isempty(H1) and not Isempty(H2):
        return NbElmnt(H2)
    elif not Isempty(H1) and Isempty(H2):
        return NbElmnt(H2)
    else:
        if IsMember(FirstElmnt(H1),H2):
            return NBUnion(Tail(H1),H2)
        else: return 1 + NBUnion(Tail(H1),H2)


#  NBIntersect : 2 Set -> Integer
def NBIntersect(H1,H2):
    if Isempty(H1) or Isempty(H2):
        return 0
    else:
        if IsMember(FirstElmnt(H1),H2):
            return 1 + NBIntersect(Tail(H1),H2)
        else:
            return NBIntersect(Tail(H1),H2)


# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #
print(rember(3,[1,2,3,4,3]))
print(rember2(3,[1,2,3,4,5,3]))         
print(MultiRember(3,[1,2,3,3,3,4,5]))
print ("makeset",makeset([1,1,2,2,3,2,1,3,4,4,5,1,1,1,1,1,1,1]))
print ("makeset2",makeset2([1,2,3,4,4,5,4,4,4,5,5,5,1,1,1,1,1,1,1]))
print(konsoset(1,[1,2,3,4]))   
print(IsSet2([1,2,3,4,4,4,4,5]))
print(IsSet([1,2,3]))
print("ISSubset:",IsSubset([1,2,3,4],[1,2,3,4,5]))
print("equal",IsEqualSet1([1,3,2],[3,1,4])) 
print("equal",IsEqualSet2([1,3,2],[3,1,4]))
print(Isintersect([1,2,3],[1,4,5]))        
print(MakeIntersect1([1,2,3],[1,4,5,3,2]))  
print(MakeIntersect2([1,2,3],[1,4,5,3,2]))      
print ("union",MakeUnion1([1,2,3,9,10,12],[1,2,3,4,5,6]))
print ("union",MakeUnion2([1,2,3,4,5,6,7,8,9],[1,2,3,4,11, 10]))   
print ("nbunion",NBUnion([1,2,3],[3,4,5,6,]))
print(NBIntersect([1,2,3],[1,4,5]))
