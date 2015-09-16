a=int(input('Number 1'))
b=int(input('Number 2'))
def nod(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a%=b
        a,b=b,a
    return a
print(nod(a,b))