from LISTTOTALBANGET import *


# # beratmangga
# def ganjil(x):
#     if Isempty(x):
#         return []
#     else:
#         if FirstElmnt(x) % 2 != 0:
#             return konso(FirstElmnt(x),ganjil(Tail(x)))
#         else:
#             return ganjil(Tail(x))
        
# def genap(x):
#     if Isempty(x):
#         return []
#     else:
#         if FirstElmnt(x) % 2 == 0:
#             return konso(FirstElmnt(x),genap(Tail(x)))
#         else:
#             return genap(Tail(x))

# def jumlahindongmas(x):
#     if Isempty(x):
#         return 0
#     else:
#         return FirstElmnt(x) + jumlahindongmas(Tail(x))
# # print(ganjil([1,2,3,4]))
# # print(genap([1,2,3,4]))


# def BeratMangga(mangga, agen):
#     if agen == 'A':
#         return jumlahindongmas(ganjil(mangga))
#     elif agen == 'B':
#         return jumlahindongmas(genap(mangga))
    

# print(BeratMangga([1,2,4,5,7],'A'))
# print(BeratMangga([1,2,4,5,7],'B'))


# ## Tebak Huruf

# def TebakHuruf(huruf,nama):
#     if Isempty(nama):
#         return "TIDAK"
#     else:
#         if huruf == FirstElmnt(nama):
#             return "YA"
#         else:
#             return TebakHuruf(huruf, Tail(nama))
        
# print(TebakHuruf('k',['s','e','n','k','u']))

# # barisansemut

# def jumlahelemen(x):
#     if Isempty(x):
#         return 0
#     else:
#         return 1 + jumlahelemen(Tail(x))
    
# print(jumlahelemen([1,2,3,4,5]))

# def BarisanSemut(x,y,n):
#     if n == 0:
#         return []
#     else:
#         if x % y == 0:
#             return BarisanSemut(x+1,y,n)
#         else:
#             return [x] + BarisanSemut(x+1,y,n-1)

# print("barisansemut",BarisanSemut(2,3,5))


# # # petualangan
# def Getlist(x):
#     return x[0]

# def tambah(x):
#     if Isempty(x):
#         return 0
#     else:
#         return FirstElmnt(x) + tambah(Tail(x))
# def kurang(x):
#     if Isempty(x):
#         return 0
#     else:
#         return FirstElmnt(x) - kurang(Tail(x))
# def kali(x):
#     if Isempty(x):
#         return 0
#     else:
#         return FirstElmnt(x) * kali(Tail(x))
# def bagi(x):
#     if Isempty(x):
#         return 0
#     else:
#         return FirstElmnt(x) / bagi(Tail(x))
        
# def petualangan(x):
#     if Isempty(x):
#         return []
#     else: 
#         if FirstElmnt(FirstElmnt(x)) == '+':
#             if IsAtom(x[1]) and IsAtom(x[2]):
#                 return x[1] + x[2]
#             elif not IsAtom(x[1]) and IsAtom(x[2]):
#                 return tambah(x[1]) + x[2]
#             elif IsAtom(x[1]) and not IsAtom(x[2]):
#                 return  x[1] + tambah(x[2])
#             else:
#                 return tambah(x[1]) + tambah(x[2])
#         elif FirstElmnt(FirstElmnt(x)) == '-':
#             if IsAtom(x[1]) and IsAtom(x[2]):
#                 return x[1] - x[2]
#             elif not IsAtom(x[1]) and IsAtom(x[2]):
#                 return kurang(x[1]) - x[2]
#             elif IsAtom(x[1]) and not IsAtom(x[2]):
#                 return  x[1] - kurang(x[2])
#             else:
#                 return kurang(x[1]) - kurang(x[2])

        
# print(petualangan(['+',[1,1,1],[1,2,3]]))


# def genap(L):
#     if Isempty(L):
#         return []
#     else:
#         if FirstElmnt(L) % 2 == 0:
#             return konso(FirstElmnt(L),genap(Tail(L)))
#         else:
#             return genap(Tail(L))
        
# print (genap([1,2,3,4,5]))


    # SearchXTree 1 ini mengeluarkan output X yang dicari sebagai Akar dan anak nya dari X sebagai output juga
def SearchXTree(X,T):
    if Isempty(T):
        return []  
    if akar(T) == X:
            return T 
    elif Isempty(anak(T)):
        return []
    else:
        if SearchXTree(X,FirstList(anak(T))):
            return SearchXTree(X,FirstList(anak(T)))
        else:
            return SearchXTree(X, MakePN(akar(T), TailList(anak(T))))


# def SearchXTree(x,T):
#     if Isempty(T):
#         return []
#     elif akar(T) == x:
#         return T
#     elif Isempty(anak(T)):
#         return []
#     else:
#         if SearchXTree(x,anak(T)):
#             return SearchXTree(x,)

        
#SearchXTree mengeluarkan output Boolean
#SearchXTree mengeluarkan output Boolean
def SearchXTree2(X,T):
    if Isempty(T):
        return False
    else:
        if akar(T) == X:
            return True
        elif Isempty(anak(T)):
            return False
        else:
            return SearchXTree2(X,FirstList(anak(T))) or SearchXTree2(X,MakePN(akar(T),TailList(anak(T))))


# tree = MakePN("Ridho", [MakePN("Silvani", []),])
# def ismaxmod4(L):
#     if Isempty(L):
#         return False
#     elif Isempty(Right(L)):
#         return Akar(L) % 4 == 0
#     else:
#         return ismaxmod4(rit(L))

def max2(a,b):
    if a>=b:
        return a
    else: return b

def maxs(L):
    if Isempty(L):
        return 0
    else:
        if IsAtom(FirstElmnt(L)):
            return max2(FirstElmnt(L), maxs(Tail(L)))
        else:
            return max2(maxs(FirstElmnt(L)),maxs(Tail(L)))

print(maxs([0,[6,5],[4,2,3],1]))


print(SearchXTree2('Eko',( MakePN("Ridho",
                                    [MakePN("Silvani",
                                            [MakePN("Nuha",[]), 
                                            MakePN("Syahrafi",[MakePN("Ega", [])]),
                                            MakePN("Noci",[])]), 
                                    MakePN("Rendi",[MakePN("Fikhrul",[])]), 
                                    MakePN("Ruth",[MakePN("Aji",[])]),
                                    MakePN("Eko",[MakePN("Raffi",[])])]))))


def max_list(L):
    if Isempty(L):
        return 0
    else:
        if FirstElmnt(L) >= max_list(Tail(L)):
            return FirstElmnt(L)
        else:
            return max_list(Tail(L))

print(max_list([19, 21, 25, 11,14, -13, 10, -19, 10]))

def min_list(L):
    if Isempty(L):
        return 0
    else:
        if FirstElmnt(L) <= min_list(Tail(L)):
            return FirstElmnt(L)
        else:
            return min_list(Tail(L))
def MakePB(A , L , R):
    return [A,L,R]

def MakeBinSearchTree(L):
    if NbElmnt(L) == 0:
        return []
    else:
        return MakePB(L[NbElmnt(L)//2], MakeBinSearchTree(L[:NbElmnt(L)//2]),MakeBinSearchTree(L[(NbElmnt(L) // 2) + 1:]))
print(min_list([19, 21, 25, 11,14, -13, 10, -19, 10]))

T = MakePB(50,
        MakePB(17,
                MakePB(12,
                        MakePB(9,[],[]),
                        MakePB(14,[],[])),
                MakePB(23,
                        MakePB(19,[],[]),
                        [])),
        MakePB(72,
                MakePB(54,[],
                        MakePB(67,[],[])),
                MakePB(76,[],[]))
    )

def total_elemen_daun(L):
    if Isempty(L):
        return 0
    elif IsOneElmnt(L):
        return 1
    else:
        return total_elemen_daun(Left(L)) + total_elemen_daun(Right(L))

def max_elmnt_daun(L):
    if Isempty(L):
        return 0
    if IsOneElmnt(L):
        return Akar(L)
    else:
        max2(max_elmnt_daun(Left(L)),max_elmnt_daun(Right(L)))


    





