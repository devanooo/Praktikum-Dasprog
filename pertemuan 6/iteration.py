def faciter(n, count,hasil):
    if n == count:
        return hasil * count
    else:
        return faciter(n, count + 1, hasil*count)
def fac2(n):
    return faciter(n,1,1)

print(fac2(3))
print(fac2(4))