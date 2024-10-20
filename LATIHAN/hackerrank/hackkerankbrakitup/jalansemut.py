# Program       : jalansemut.py
# Deskripsi     : Source Code Jalan Semut
# NIM/Nama      : 24060124140149/Devano Trestanto
# Tanggal       : 27/09/2024


def jalansemut(x,y,z):
    
    return round(min((((x+y)**2 + z**2)**0.5),(((x+z)**2 + y**2)**0.5),(((z+y)**2 + x**2)**0.5)),3)
    

print(jalansemut(3,4,5))