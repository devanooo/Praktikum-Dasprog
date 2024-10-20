# Program       : bilanganpenyebut.py
# Deskripsi     : Source Code Sequence Bilangan Penyebut
# NIM/Nama      : 24060124140149/Devano Trestanto
# Tanggal       : 27/09/2024


def denumeratorSeq(x):
    if (10**len(x)-1) % int(x) == 0:
        return f'Ada: {int((10**len(x)-1) / int(x))}'
    else:
        return 'Tidak ada'
    
print(eval(input()))