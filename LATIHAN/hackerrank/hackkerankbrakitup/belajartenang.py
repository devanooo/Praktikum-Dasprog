# Program       : belajartenang.py
# Deskripsi     : Source Code Belajar Tenang
# NIM/Nama      : 24060124140149/Devano Trestanto
# Tanggal       : 27/09/2024

def BelajarTenang(dB,m):
    if 15 * 10 ** ((dB-40)/20) <= m:
        return f"{round((15*10**((dB-40)/20)),3)} meter"
    else:
        return "Isi bensin dulu, bang"
    
print(eval(input()))

print("test")