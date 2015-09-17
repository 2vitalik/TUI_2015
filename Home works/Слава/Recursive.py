__author__ = 'lavx64'
#Выводит ближайшее к 100 число в последовательности n = n + n*2
temp = 0
def GetOverThan100(int):
    global temp
    int += (int*2)
    if int>=100:
        if temp>int:
            print temp
        else:
            print int
    else:
        temp = int
        return GetOverThan100(int)


integer = raw_input("Enter n:\n")
integer = int(integer)
GetOverThan100(integer)