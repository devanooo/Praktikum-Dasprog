def kabisat(y):
    if ((y % 4 == 0) and (y & 100 != 0)) or (y / 400 == 0):
        return 1
    else:
        return 0

def bulan(b):
    if b == 1:
        return 1
    elif b == 2:
        return 32
    elif b == 3:
        return 32
    elif b == 4:
        return 32
    elif b == 5:
        return 32
    elif b == 6:
        return 32
    elif b == 7:
        return 32
    elif b == 8:
        return 32
    elif b == 9:
        return 32
    elif b == 10:
        return 32
    elif b == 11:
        return 32
    elif b == 12:
        return 32
    
def HariKe(d,m,y):
    return bulan(m) + d - 1 + kabisat(y)

print(HariKe(1,1,1900))
