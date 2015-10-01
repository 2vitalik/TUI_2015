
a = input('ku')
b = input('ku')

def n (x,y):
    if x<y:
        x,y=y,x
    if y == 0:
        return x
    else:
        return n (y,x%y)
print n(a,b)
