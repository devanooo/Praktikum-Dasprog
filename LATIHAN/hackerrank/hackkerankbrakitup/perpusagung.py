# Program       : perpusagung.py
# Deskripsi     : Source Code Perpustakaan Agung
# NIM/Nama      : 24060124140149/Devano Trestanto
# Tanggal       : 27/09/2024

def EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R):
    
    return round(partisi(X,Y,SS,SR,ratarata3hari(D),jangkauan(AS,AM,AIP),R),5)

def ratarata3hari(x):
    if x == "senin":
        return ((5000+6000+4000)/3)
    elif x == "selasa":
        return ((7000+5000+2000)/3)
    elif x == "rabu":
        return ((4500+3500+3000)/3)
    elif x == "kamis":
        return ((2900+2100+2000)/3)
    elif x == "jumat":
        return ((3000+3000+3000)/3)
    elif x == "sabtu":
        return ((2000+2500+2300)/3)
    elif x == "minggu":
        return ((1100+900+1000)/3)
    
def jangkauan(x,y,z):
    return (max(x,y,z) - min(x,y,z))


def partisi(X,Y,SS,SR,rata,jangkauan,persen):
    
    if X < SR and Y > SS:
        return ((((abs(X-SR) * jangkauan)/rata) * (persen/100)) + ((abs(SS-SR)*jangkauan)/rata) + (((abs(SS-Y) * jangkauan)/rata) * persen/100)) / 3
    
    elif X < SR and Y > SR:
        return((((abs(X-SR) * jangkauan)/rata) *(persen/100)) + ((abs(Y-SR)*jangkauan)/rata)) / 2
    elif Y > SS and X < SS:
        return(((abs(X-SS) * jangkauan)/rata) + (((abs(Y-SS)*jangkauan)/rata)*(persen/100))) / 2
    elif (X < SR) or ((X > SS) and (Y < SR)) or (Y > SS):
        return (((abs(Y-X) * jangkauan)/rata) * (persen/100))
    else:
        return (((abs(Y-X) * jangkauan)/rata))



print(eval(input()))