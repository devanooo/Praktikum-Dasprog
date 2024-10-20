import tipebentukan

def kuadran(x,y):
    if tipebentukan.Absis(x) > 0 and tipebentukan.ordinat(x) > 0:
        return "Kuadran 1"
    elif tipebentukan.Absis(x) < 0 and tipebentukan.ordinat(x) > 0:
        return "Kuadran 2"
    elif tipebentukan.Absis(x) < 0 and tipebentukan.ordinat(x) < 0:
        return "Kuadran 3"
    elif tipebentukan.Absis(x) > 0 and tipebentukan.ordinat(x) > 0:
        return "Kuadran 4"