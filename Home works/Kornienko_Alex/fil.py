__author__ = 'Fun'
dic = {
    1:{
        2:20,
        3:30
    },
    2:{
       1:20,
       3:12,
       4:7
    },
    3:{
        1:30,
        2:12,
        4:3,
        5:5

    },
    4:{
        2:7,
        3:3,
        5:12
    },
    5:{
        4:12,
        3:5,
    }

}
lis = {
    1:0,
    2:None,
    3:None,
    4:None,
    5:None
}
for v in range(1,6):
    for u,w in dic.items():
        if lis[u] is None or lis[u]>lis[u]+w:
            lis[u]=lis[u]+w

print(lis)
