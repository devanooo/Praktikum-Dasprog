def JenisSegitiga(a,b,c):
    if a > 0 and b > 0 and c > 0 and (a+b > c and a+c > b and c+b > a):
        if a == b == c:
            return("sama sisi")
        elif a == b or a == c or c == b:
            return("sama kaki")
        else : return("sembarang")
    else : return"tidak terbentuk"

print(JenisSegitiga(1,2,3))