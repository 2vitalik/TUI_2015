a = input('Enter number 1')
b = input('Enter number 2')
def nod (a, b):
    if a < b:
        a,b=b,a
    while b!=0:
        a=a%b
        a,b=b,a
    return a
print nod (12,18)