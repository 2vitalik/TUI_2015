__author__ = 'Kostik'
a=int(input("a:"))
b=int(input("b:"))

def nod(a,b):
    if a < b:
        a,b=b,a
    if b==0:
        return a
    else:
        return nod(b,a%b)
print(nod(a,b))