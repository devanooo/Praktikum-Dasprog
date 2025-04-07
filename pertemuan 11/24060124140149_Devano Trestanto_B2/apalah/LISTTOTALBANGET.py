
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
        
def IsOneElmnt(L):
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

# ================================================================================================================================================================== #
# Nama File: LOL_24060124140149.py
# Deskripsi : List Of list 
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: 13/11/2024

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
    if IsOneElmnt(S):
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

# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

# print(KonsLo(1, [[1,2,3],[4,5,6]]))
# print(KonsLo([1,2,2], [[1,2,3],[4,5,6]]))

# print(KonsLi([[1,2,3],[4,5,6]],1))
# print(KonsLi([[1,2,3],[4,5,6]], [1,2,2]))

# print(FirstList([[1,2,3],[4,5,6]]))
# print(FirstList([]))
# print(LastList([]))
# print(LastList([[1,2,3],[4,5,6]]))
# print(TailList([[1,2,3],[4,5,6],1,2,[]]))
# print(HeadList([[1,2,3],[4,5,6],1,2,[]]))

# print(Isempty([]))
# print(Isempty([1]))
# print(IsAtom([1]))
# print(IsAtom(1))

# print("MaxsUm",MaxSumElmt([1,3,[1],2,[12,300],4,[12],313,6]))
# print("MaxsUm",MaxSumElmt([1,3,[1],2,[12,300],4,[12],3,6]))
# print("MaxNbekemnohnlist",MaxNBElmtList([1,3,[1],2,[12],4,[12],5,6]))
# print("SumLOL",SumLoL([1,3,[1],2,[12],4,5,6]))
# print("NBelementlist",NBElmtList([1,3,[1],2,[12],4,5,6]))
# print("NBelementatom",NBElmtAtom([1,3,[1],2,[12],4,5,6]))
# print("max",Max([1,3,[1],2,[12]]))
# print("ismembers",IsmemberS([3],[1,2,3,[3]]))
# # print("rember",rember([3],[1,3,[1],2,[3]]))

# +=========================================================================+ #
#                                Aplikasi
# +=========================================================================+ #

# print("Hasil Konso:", konso(1,[2,3,4,5]))
# print("Hasil Konsoi:", konsi([1,2,3,4],5))

# print("\nHasil IsEmpty :", Isempty([]))
# print("Hasil IsEmpty :", Isempty([1,2,3,4,5]))
# print("Hasil IsOneElement :", IsOneElmnt([]))
# print("Hasil IsOneElement :", IsOneElmnt([1]))
# print("Hasil IsOneElement :", IsOneElmnt([1,2,3,4,5]))

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

