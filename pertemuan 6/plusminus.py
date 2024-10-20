# def plus(x,y):
#     if y == 0:
#         return x
#     else:
#         return 1 + plus(x,y-1)
# def min(x,y):
#     if y == 0:
#         return x
#     else:
#         return min(x,y-1) - 1

# def kali(x,y):
#     if y == 1:
#         return x
#     else:
#         return kali(x,y-1) + x

# def pangkat(x,y):
#     if y == 1:
#         return x
#     else:
#         return pangkat(x,y-1) * x

# def bagi(x,y):
#     if x < y:
#         return 0
#     else:
#         return bagi(x-y,y) + 1
    
# print(kali(2,3))
# print(bagi(6,3))
# print(plus(1,2))
# print(plus(3,4))
# print(plus(6,7))


def Point(x,y) :
    return [x,y]

def absis (p) :
    return p[0]

def ordinat (p) :
    return p[1]

# def cekkuadran(P):
#     if absis(P) > 0 and ordinat(P) > 0:


print(absis(Point(1,2)))