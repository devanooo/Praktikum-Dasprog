# Program       : lalulintaslangit.py
# Deskripsi     : Source Code Lalu Lintas Langit
# NIM/Nama      : 24060124140149/Devano Trestanto
# Tanggal       : 27/09/2024

def monitor_pesawat(x,y,z):
    if(y > 900 or y < 200):
        return "Kecepatan Berbahaya"
    elif(x > 12000):
        return "Terlalu Tinggi"
    elif(z < 20):
        return "Bahan Bakar Rendah"
    if(x < 5000 and (y >= 200 and y <= 900) and z > 50):
        return "Aman untuk Mendarat"
    else:
        return "Berjalan Normal"
print(eval(input()))