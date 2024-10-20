def konversi(suhu,kode):
    if kode == 1:
        return(suhu*(4/5)) #reamur
    elif kode == 2:
        return((suhu*9/5)+32)# fahrenheit
    elif kode == 3:
        return(suhu + 273) # kelvin
    
print(konversi(30,1))
print(konversi(30,2))
print(konversi(30,3))