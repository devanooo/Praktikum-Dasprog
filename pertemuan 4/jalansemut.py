def jalanSemut(x,y,z):
    return ((min(x,y,z)**2 + (min(min(x,y,z)))**2))**0.5
            
print(jalanSemut(1,2,7))