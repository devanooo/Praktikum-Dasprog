# Program       : jampasirajaib.py
# Deskripsi     : Source Code Jam Pasir Ajaib
# NIM/Nama      : 24060124140149/Devano Trestanto
# Tanggal       : 27/09/2024

def jam(j,m,s):
    if (j >= 0 and j <= 24) and (m >= 0 and m < 60) and (s >= 0 and s < 60):
        return f"Jam: {j}, Menit: {m}, Detik: {s}"
    else:
        return("Waktu tidak valid")
    
print(eval(input()))