def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def faktorial(n):
    if n != 0:
        return n * faktorial(n - 1)
    else:
        return 1

print(fac(3))
print(faktorial(3))