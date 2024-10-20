def max(x,y):
    return (x+y + abs(x-y)) /2
def min(x,y):
    return (x+y - abs(x-y)) / 2

def MO(a,b,c,d):
    max_total = max(max(a,b),max(c,d))
    min_total = min(min(a,b),min(c,d))
    return((a+b+c+d) - max_total - min_total) / 2

print (MO(3,5,4,2))

