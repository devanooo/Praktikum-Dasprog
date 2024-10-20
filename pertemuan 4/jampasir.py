def jam(j,m,s):
    if (j > 0 and j <= 24) and (m > 0 and m < 60) and (s > 0 and s < 60):
        return f"Jam: {j}, Menit: {m}, Detik:{s}"
    else:
        return("Waktu tidak valid")
    
print(jam(12,30,45))