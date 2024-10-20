def no6(a,b,c):
    
    if (-1*b + (b*b - 4*a*c)**0.5) / 2*a > (-1*b - (b*b - 4*a*c)**0.5) / 2*a:
        return ((-1*b + (b*b - 4*a*c)**0.5) / 2*a) /((-1*b - (b*b - 4*a*c)**0.5) / 2*a) 

    else:
        return ((-1*b - (b*b - 4*a*c)**0.5) / 2*a)/((-1*b + (b*b - 4*a*c)**0.5) / 2*a)

print(no6(1,4,5))
print(no6(1,-9,3))
print(no6(1,-5,6))