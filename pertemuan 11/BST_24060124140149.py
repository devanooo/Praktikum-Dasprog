# Nama File: BST_24060124140149.py
# Deskripsi : 
# Nama / NIM : Devano Trestanto / 24060124140149
# Tanggal: / /

from LISTTOTALBANGET import *

def MakePB(A , L , R):
    return [A,L,R]

def Akar(P):
    return P[0]

def Left(P):
    return P[1]

def Right(P):
    return P[2]


def PrintBinaryTreeHelp(T, indent):
    if T != []:
        print(indent + str(Akar(T)))
        PrintBinaryTreeHelp(Left(T), indent + "   ")
        PrintBinaryTreeHelp(Right(T), indent + "   ")
    else:
        print (indent + "[]")

def PrintBinaryTree(T):
    PrintBinaryTreeHelp(T,'')


def AddX(P, X):
    if Isempty(P):
        return MakePB(X, [],[])
    else:
        if X >= Akar(P):
            return MakePB(Akar(P),Left(P),AddX(Right(P),X))
        else:
            return MakePB(Akar(P), AddX(Left(P),X), Right(P))


def BSearchX(P,X):
    if Isempty(P):
        return False
    else:
        if Akar(P) == X:
            return True
        else: 
            if X < Akar(P):
                return BSearchX(Left(P),X)
            else:
                return BSearchX(Right(P),X)
            
    
def MakeBinSearchTree(L):
    if NbElmnt(L) == 0:
        return []
    else:
        return MakePB(L[NbElmnt(L)//2], MakeBinSearchTree(L[:NbElmnt(L)//2]),MakeBinSearchTree(L[(NbElmnt(L) // 2) + 1:]))

def ismaxmod4(L):
    if Isempty(L):
        return False
    elif Isempty(Right(L)):
        return Akar(L) % 4 == 0
    else:
        return ismaxmod4(Right(L))



pohonbiner = [6, [3, [2, [1, [], []], []], [5, [4, [], []], []]], [9, [8, [7, [], []], []], [20, [], []]]]

T = AddX(AddX(AddX(AddX(AddX([],50), 75), 200), 100), 120)

# PrintBinaryTree() 
print("NO5",ismaxmod4(pohonbiner))
print(MakeBinSearchTree([1,2,3,4,5,6]))

print(BSearchX(pohonbiner,2)) 
L = [1,2,3,4,5,6,7]
print(L[:3])
print(L[3:])

# print(MakeBinSearchTree)
