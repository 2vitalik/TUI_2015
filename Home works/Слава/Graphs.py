__author__ = 'lavx64'
N = {
    'a': {'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5},
    'b': {'c': 2, 'e': 4},
    'c': {'d': 3},
    'd': {'e': 4},
    'e': {'f': 5},
    'f': {'c': 2, 'g': 6, 'h': 7},
    'g': {'f': 5, 'h': 7},
    'h': {'f': 5}
}
#TODO
if 'b' in N['a']:
    print "Hello"
#smejnost'

print N['a']['b']
#ves

print len(N['a'])
#stepen'
