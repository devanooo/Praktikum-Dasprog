def rekursi_tanpa_basis(n):
    return rekursi_tanpa_basis(n-1)

def faktorial(n):
    if n != 0:
        return n * faktorial(n - 1)
    else:
        return 1

    


print (faktorial(3))
