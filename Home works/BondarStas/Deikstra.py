__author__ = 'Stas'
dict = {
    1:{2: 40,3: 34},
    2:{1: 40,3: 50,4: 68,5: 99},
    3:{1: 34,2: 50,5: 24},
    4:{2: 68,5: 34},
    5:{2: 99,4: 34}
};
result = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None
}
v = 1
for u,n in dict[v].items():
