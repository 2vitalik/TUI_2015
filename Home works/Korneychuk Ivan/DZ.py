a = input('Enter any + number: ')
b = input('Enter any other + number: ')

if b>a:
    a,b = b,a

    while b!=0:
        a%=b
        a,b = b,a


