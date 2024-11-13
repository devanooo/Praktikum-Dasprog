import listfunction as lst
import math

# print(lst.isoneelemet([1]))
# print(lst.FirstElmnt([1,2,3,4,5]))

# print(lst.Tail([1,2,3,4]))

def logaritma(n):
    if n == 1:
        return [2]
    else:
        return lst.konso(2**n, logaritma(n-1))

def pangkat(x,n):
    if n == 0:
        return 1
    else:
        return x*pangkat(x,n-1)

print(pangkat(2,3))
print("Log",logaritma(3))