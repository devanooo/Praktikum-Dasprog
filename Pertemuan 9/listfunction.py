
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
# ElmtkeN: integer >= 0, List -> elemen
def ElemntkeN(n,L):
    return L[n-1]
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

# IsMember: elemen, List -> boolean
def IsMember(n,L):
    if n == FirstElmnt(L):
        return True
    elif Isempty(L):
        return False
    else:
        return IsMember(n,Tail(L))
    
# print (IsMember(0,[1,2,3,4]))

# +=========================================================================+ #
#                           REALISASI OPERATOR
# +=========================================================================+ #
# NbElmnt: List -> Integer
def NbElmnt(L):
    if Isempty(L):
        return 0
    else : 
        return 1 + NbElmnt(Tail(L))

# Copy: List -> List
def copy(L):
    if Isempty(L):
        return []
    else:
        return konso(FirstElmnt(L),copy(Tail(L)))
# print(copy([1,2,3,4,5]))

# Inverse: List -> List
def inverse(L):
    if Isempty(L):
        return []
    else:
        return konso(LastElmnt(L),inverse(Head(L)))
    
# print("Hasil Inverse: ", inverse([1,2,3,4]))

# Konkat: 2 List -> List
def konkat(L1,L2):
    if Isempty(L2):
        return L1
    else:
        return konsi(konkat(L1,Head(L2)),LastElmnt(L2))
# print("konkta",konkat([1,2,3,4],[7,8,9]))

# sumElmt: List of integer -> integer
def SumElmnt(L):
    if Isempty(L):
        return 0
    else: 
        return FirstElmnt(L) + SumElmnt(Tail(L))
# print(SumElmnt([1,2,3,4,6]))

# AvgElmt: List of integer -> integer
def AvgElmnt(L):
    if Isempty(L):
        return 0
    else:
        return SumElmnt(L) / NbElmnt(L)
# print (AvgElmnt([1,1,1,1]))

# MaxElmt: List of integer -> integer
def MaxElmnt(L):
    if Isempty(L):
        return None
    elif NbElmnt(L) == 1:
        return FirstElmnt(L)
    else:
        if FirstElmnt(L) > MaxElmnt(Tail(L)):
            return FirstElmnt(L)
        else:
            return MaxElmnt(Tail(L))
def JumlahMax(M, L):
    if Isempty(L):
        return 0
    else:
        if M == FirstElmnt(L):
            return 1 + JumlahMax(M,Tail(L))
        else:
            return JumlahMax(M,Tail(L))
        

# MaxNB: List of integer -> <integer, integer>
def MaxNB(L):
    if Isempty(L):
        return []
    else:
        return [JumlahMax(MaxElmnt(L),L),MaxElmnt(L)]
# print (MaxNB([1,2,2,2,2]))

# AddList: 2 List of integer -> List of integer
def Addlist(L1,L2):
    if Isempty(L1) and Isempty(L2):
        return []
    elif NbElmnt(L1) != NbElmnt(L2):
        return False
    else:
        return konso(FirstElmnt(L1)+FirstElmnt(L2), Addlist(Tail(L1),Tail(L2)))

# print(Addlist([1,2,3],[1,2,3]))

# IsPalindrom: List of character -> boolean
def IsPalindrome(L):
    if Isempty(L):
        return True
    else:
        return FirstElmnt(L) == LastElmnt(L) and IsPalindrome(Head(Tail(L)))
# print(IsPalindrome(['A','b','A','C']))


# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

# print("Hasil Konso:", konso(1,[2,3,4,5]))
# print("Hasil Konsoi:", konsi([1,2,3,4],5))

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

