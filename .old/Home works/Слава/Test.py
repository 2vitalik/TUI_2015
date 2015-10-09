__author__ = 'lavx64'

def SredneeArifm():
    list_1 = []
    list_1 = raw_input("Enter list\n").split(' ')
    i = 0
    while i<len(list_1):
        list_1[i]=int(list_1[i])
        i+=1
    max = 0
    for i in list_1:
        max+=i
    print ("Srednee arifm. :", max/len(list_1))