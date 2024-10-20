def no6(a,b,c):
    
    if (-1*b + (b*b - 4*a*c)**0.5) / 2*a > (-1*b - (b*b - 4*a*c)**0.5) / 2*a:
        return ((-1*b + (b*b - 4*a*c)**0.5) / 2*a) /((-1*b - (b*b - 4*a*c)**0.5) / 2*a) 

    else:
        return ((-1*b - (b*b - 4*a*c)**0.5) / 2*a)/((-1*b + (b*b - 4*a*c)**0.5) / 2*a) 
    


# def no5(a,b,c):

#     if a == b and a == c and b == c:
#         return("sama sisi")
#     elif (a == b or a == c or b == c):
#         return("sama kaki")
#     elif (a != b and a != c and b != c):
#         return("sembarang")

# print("Sama sisi : ", no5(1,1,1))
# print("Sama kaki : ", no5(1,2,1))
# print("Sembarang : ", no5(1,2,4))

print(no6(1,5,6))