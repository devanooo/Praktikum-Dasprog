# Nama File: pert1.py
# Pembuat : Devano Trestanto
# Tanggal: 27 Agustus 2024

# Deskripsi : Menentukan bilangan genap

# Definisi dan Spesifikasi
# genap: Integer --> boolean
#   genap(angka) untuk menentukan apakah suatu bilangan "angka" genap atau tidak
# tentukan : boolean --> string
#   tentukan(tf) untuk memberikan output kepada user

# Realisai
def genap(angka):
    return angka%2 == 0

def tentukan(genap):
    if genap == True:
        print("Angka Genap!")

    else:
        print("Angka Ganjil!")

# Aplikasi
angka = int(input("Masukkan Angka : "))

tf = genap(angka)

tentukan(tf)



