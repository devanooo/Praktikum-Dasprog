def MakePoint(x,y):
    return [x,y]
def Absis(P):
    return P[0]
def ordinat(P):
    return P[1]

def IsOrigin(P):
    if (Absis(P) == 0 and ordinat(P) == 0):
        return True
    else:
        return False


def kuadran(x):
    if Absis(x) > 0 and ordinat(x) > 0:
        return "Kuadran 1"
    elif Absis(x) < 0 and ordinat(x) > 0:
        return "Kuadran 2"
    elif Absis(x) < 0 and ordinat(x) < 0:
        return "Kuadran 3"
    elif Absis(x) > 0 and ordinat(x) < 0:
        return "Kuadran 4"

P = MakePoint(2,3)

print (kuadran(MakePoint(2,-3)))
print(P)
print(Absis(P),ordinat(P))
print(Absis(P))
print(ordinat(P))