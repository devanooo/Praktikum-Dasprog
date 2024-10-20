"""def max(x,y):
    return (x+y + abs(x-y)) /2
def min(x,y):
    return (x+y - abs(x-y)) / 2

def max4bil(a,b,c,d):
    max1 = max(a,b)
    max2 = max(c,d)
    
    maxtotal = (max1+max2 + abs(max1-max2)) /2
    return maxtotal

def min4bil(a,b,c,d):
    min1 = min(a,b)
    min2 = min(c,d)

    mintotal = min1+min2 - abs(min(a,b)-min(c,d)) /2
    return mintotal

def MO(a,b,c,d):
    max = max4bil(a,b,c,d)
    min = min4bil(a,b,c,d)
    total = a+b+c+d

    hasilMO = total - max - min
    return hasilMO"""

def max(x,y):
    return (x+y + abs(x-y)) /2
def min(x,y):
    return (x+y - abs(x-y)) / 2

def MO(a,b,c,d):
    max_total = max(max(a,b),max(c,d))
    min_total = min(min(a,b),min(c,d))
    return((a+b+c+d) - max_total - min_total) / 2

print (MO(3,5,4,2)) # 3.5


