def IsKabisat(a):
    if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0):
        return 1
    else:
        return 0
    
def lusa(d,m,y):
    def dpm (B):
            if B == 1:
                return 1
            elif B == 2:
                return 32
            elif B == 3:
                return 60
            elif B == 4:
                return 91
            elif B == 5:
                return 121
            elif B == 6:
                return 152
            elif B == 7:
                return 182
            elif B == 8:
                return 213
            elif B == 9:
                return 244
            elif B == 10:
                return 274
            elif B == 11:
                return 305
            elif B == 12:
                return 335

    def Harike1900(d,m,y):
            if (m > 2):
                return dpm(m) + d - 1 + IsKabisat(y) + 2
            else:
                return dpm(m) + d - 1 + 2
    
    if Harike1900(d,m,y) % 7 == 0:
        return "Jum'at"
    elif Harike1900(d,m,y) % 7 == 1:
        return "Sabtu"
    elif Harike1900(d,m,y) % 7 == 2:
        return "Minggu"
    elif Harike1900(d,m,y) % 7 == 3:
        return "Senin"
    elif Harike1900(d,m,y) % 7 == 4:
        return "Selasa"
    elif Harike1900(d,m,y) % 7 == 5:
        return "Rabu"
    elif Harike1900(d,m,y) % 7 == 6:
        return "Kamis"

print(lusa(25,9,2000))