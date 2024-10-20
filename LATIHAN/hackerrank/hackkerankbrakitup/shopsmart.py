# Program       : shopsmart.py
# Deskripsi     : Source Code Shop Smart
# NIM/Nama      : 24060124140149/Devano Trestanto
# Tanggal       : 27/09/2024




def hargaAkhir(harga,kategori,vip,lokasi,hari):
    if hari == "Jumat" or hari == "Sabtu":
        if kategori == "elektronik":
            if lokasi == "dalam negeri":
                if vip == True:
                    return int(((harga-(harga*0.3)) - ((harga-(harga*0.3))*0.05)) + (((harga-(harga*0.3)) - ((harga-(harga*0.3))*0.05))*0.1))
                # elektronik : vip diskon 30%, diskon jumat sabtu 5%, dalam negeri pajak 10%
                else: 
                    return int(((harga-(harga*0.1)) - ((harga-(harga*0.1))*0.05)) + (((harga-(harga*0.1)) - ((harga-(harga*0.1))*0.05))*0.1))
                # elektronik : non vip 10%, diskon jumat sabtu 5%,pajak luar negeri 20%
            else:
                if vip == True:
                    return int(((harga-(harga*0.3)) - ((harga-(harga*0.3))*0.05)) + (((harga-(harga*0.3)) - ((harga-(harga*0.3))*0.05))*0.2))
                # elektronik : vip diskon 30%, diskon jumat sabtu 5%, dalam negeri pajak 10%
                else: 
                    return int(((harga-(harga*0.1)) - ((harga-(harga*0.1))*0.05)) + (((harga-(harga*0.1)) - ((harga-(harga*0.1))*0.05))*0.2))
                # elektronik : non vip 10%, diskon jumat sabtu 5%,pajak luar negeri 20%

        elif kategori == "pakaian": 
            if lokasi == "dalam negeri":
                if vip == True:
                    return int(((harga-(harga*0.2)) - ((harga-(harga*0.2))*0.05)) + (((harga-(harga*0.2)) - ((harga-(harga*0.2))*0.05))*0.1))
                # pakaian : vip diskon 20%, diskon jumat sabtu 5%, dalam negeri pajak 10%
                else: 
                    return int(((harga-(harga*0.15)) - ((harga-(harga*0.15))*0.05)) + (((harga-(harga*0.15)) - ((harga-(harga*0.1))*0.05))*0.1))
                # pakaian : non vip 15%, diskon jumat sabtu 5%,pajak dalneg 10%
            else:
                if vip == True:
                    return int(((harga-(harga*0.2)) - ((harga-(harga*0.2))*0.05)) + (((harga-(harga*0.2)) - ((harga-(harga*0.2))*0.05))*0.2))
                # pakaian : vip diskon 20%, diskon jumat sabtu 5%, luar negeri pajak 20%
                else: 
                    return int(((harga-(harga*0.15)) - ((harga-(harga*0.15))*0.05)) + (((harga-(harga*0.15)) - ((harga-(harga*0.15))*0.05))*0.2))
                # pakaian : non vip 15%, diskon jumat sabtu 5%,pajak LN 20%

        elif kategori == "makanan":
            if lokasi == "dalam negeri":
                if vip == True:
                    return int(((harga-(harga*0.15)) - ((harga-(harga*0.15))*0.05)) + (((harga-(harga*0.15)) - ((harga-(harga*0.15))*0.05))*0.1))
                # makanan : VIP diskon 15%, diskon jumat sabtu 5%, dalam negeri pajak 10%
                else: 
                    return int(((harga-(harga*0.02)) - ((harga-(harga*0.02))*0.05)) + (((harga-(harga*0.02)) - ((harga-(harga*0.1))*0.05))*0.1))
                # makanan: non vip 2%, diskon jumat sabtu 5%,pajak dalneg 10%
            else:
                if vip == True:
                    return int(((harga-(harga*0.15)) - ((harga-(harga*0.15))*0.05)) + (((harga-(harga*0.15)) - ((harga-(harga*0.2))*0.05))*0.2))
                # makanan : VIP diskon 15%, diskon jumat sabtu 5%, luar negeri pajak 20%
                else: 
                    return int(((harga-(harga*0.02)) - ((harga-(harga*0.02))*0.05)) + (((harga-(harga*0.02)) - ((harga-(harga*0.15))*0.05))*0.2))
                # makanan: non vip 2%, diskon jumat sabtu 5%,pajak LN 20%

        else:
            if lokasi == "dalam negeri":
                return int(harga-(harga*0.05) + (harga-(harga*0.05)*0.1))
            else:
                return int(harga-(harga*0.05) + (harga-(harga*0.05)*0.2))

    elif hari == "Rabu" and kategori == "pakaian":
        if lokasi == "dalam negeri":
            if vip == True:
                return int(((harga - (harga * 0.2)) - ((harga - (harga * 0.2))*0.05)) + ((harga - (harga * 0.2)) - ((harga - (harga * 0.2))*0.05))*0.1)

            else:
                return int(((harga - (harga * 0.05)) - ((harga - (harga * 0.05))*0.05)) + ((harga - (harga * 0.05)) - ((harga - (harga * 0.05))*0.05))*0.1)
        else :
            if vip == True:
                return int((((harga - (harga * 0.2)) - ((harga - (harga * 0.2))*0.2))) + (((harga - (harga * 0.2)) - ((harga - (harga * 0.2))*0.2)))*0.2)

            else:
                return int((((harga - (harga * 0.05)) - ((harga - (harga * 0.05))*0.05))) + (((harga - (harga * 0.05)) - ((harga - (harga * 0.05))*0.05)))*0.2)

    elif hari == "Minggu":
        if kategori == "elektronik":
            if lokasi == "dalam negeri":
                if vip == True:
                    return int((((harga-(harga*0.3))) + ((harga-(harga*0.3)))*0.1) + (((harga-(harga*0.3))) + ((harga-(harga*0.3)))*0.1)*0.05 )
                else: 
                    return int((((harga-(harga*0.1))) + ((harga-(harga*0.1)))*0.1) + (((harga-(harga*0.1))) + ((harga-(harga*0.1)))*0.1)*0.05 )
            else:
                if vip == True:
                    return int((((harga-(harga*0.3))) + ((harga-(harga*0.3)))*0.2) + (((harga-(harga*0.3))) + ((harga-(harga*0.3)))*0.2)*0.05)
                else: 
                    return int((((harga-(harga*0.1))) + ((harga-(harga*0.1)))*0.2) + (((harga-(harga*0.1))) + ((harga-(harga*0.1)))*0.2)*0.05)

        elif kategori == "pakaian":
            if lokasi == "dalam negeri":
                if vip == True:
                    return int((((harga-(harga*0.2))) + ((harga-(harga*0.2)))*0.1) + (((harga-(harga*0.2))) + ((harga-(harga*0.2)))*0.1)*0.05 )
                else: 
                    return int((((harga-(harga*0.05))) + ((harga-(harga*0.05)))*0.1) + (((harga-(harga*0.05))) + ((harga-(harga*0.05)))*0.1)*0.05 )
            else:
                if vip == True:
                    return int((((harga-(harga*0.2))) + ((harga-(harga*0.2)))*0.2) + (((harga-(harga*0.2))) + ((harga-(harga*0.2)))*0.2)*0.05)
                else: 
                    return int((((harga-(harga*0.05))) + ((harga-(harga*0.05)))*0.2) + (((harga-(harga*0.05))) + ((harga-(harga*0.05)))*0.2)*0.05)
        elif kategori == "makanan":
            if lokasi == "dalam negeri":
                if vip == True:
                    return int((((harga-(harga*0.15))) + ((harga-(harga*0.15)))*0.1) + (((harga-(harga*0.15))) + ((harga-(harga*0.15)))*0.1)*0.05 )
                else: 
                    return int((((harga-(harga*0.02))) + ((harga-(harga*0.02)))*0.1) + (((harga-(harga*0.02))) + ((harga-(harga*0.02)))*0.1)*0.05 )
            else:
                if vip == True:
                    return int((((harga-(harga*0.15))) + ((harga-(harga*0.15)))*0.2) + (((harga-(harga*0.15))) + ((harga-(harga*0.2)))*0.2)*0.05)
                else: 
                    return int((((harga-(harga*0.02))) + ((harga-(harga*0.02)))*0.2) + (((harga-(harga*0.02))) + ((harga-(harga*0.02)))*0.2)*0.05)
        else:
            if lokasi == "dalam negeri":
                return int(harga + (harga*0.1)+ (harga + (harga*0.1))*0.05)
            else:
                return int(harga + (harga*0.2)+ (harga + (harga*0.2))*0.05)
    
    else:
        if kategori == "elektronik":
            if lokasi == "dalam negeri":
                if vip == True:
                    return int((harga - (harga*0.3)) + (harga - (harga*0.3))*0.1)
                else:
                    return int((harga - (harga*0.1)) + (harga - (harga*0.3))*0.1)
            else:
                if vip == True:
                    return int((harga - (harga*0.3)) + (harga - (harga*0.3))*0.2)
                else:
                    return int((harga - (harga*0.1)) + (harga - (harga*0.3))*0.2)
        if kategori == "pakaian":
            if lokasi == "dalam negeri":
                if vip == True:
                    return int(harga - (harga*0.2) + ((harga - (harga*0.2))*0.1))
                else :
                    return int(harga - (harga*0.05) + ((harga - (harga*0.05))*0.1))
            else:
                if vip == True:
                    return int(harga - (harga*0.2) + ((harga - (harga*0.2))*0.2))
                else :
                    return int(harga - (harga*0.05) + ((harga - (harga*0.05))*0.2))
        if kategori == "makanan":
            if lokasi == "dalam negeri":
                if vip == True:
                    return int(harga - (harga*0.15) + ((harga - (harga*0.15))*0.1))
                else :
                    return int(harga - (harga*0.02) + ((harga - (harga*0.02))*0.1))
            else:
                if vip == True:
                    return int(harga - (harga*0.15) + ((harga - (harga*0.15))*0.2))
                else :
                    return int(harga - (harga*0.02) + ((harga - (harga*0.02))*0.2))

    