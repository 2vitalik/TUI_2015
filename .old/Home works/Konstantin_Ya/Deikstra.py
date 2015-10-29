__author__ = 'Kostik'
"""a = {
      0:[(1,10),(2,5)],
      1:[(0,10),(2,40),(3,50)],
      2:[(0,5),(1,40),(3,20),(4,25)],
      3:[(1,50),(2,20),(4,30)],
      4:[(2,25),(3,30)]
    }"""
a = dict()


with open('graph') as file:
    w1,w2 = [int(x) for x in file.readline().split()]
    n,m = [int(x) for x in file.readline().split()]
    for line in file:
        u, v, c = line.split()
        u = int(u)
        v = int(v)
        c = int(c)
        if u in a:
            a[u].append((v,c))
        else:
            a[u] = [(v,c)]

used=[False]*n
g=[1e9]*n
g[w1]=0
for l in range(n):
    index = -1
    curres = 1e9
    for j in range(n):
        if g[j] < curres:
            if used[j] == False:
                index = j
                curres = g[j]
    used[index] = True
    for (u,w) in a[index]:
        if g[u]>g[index]+w:
             g[u]=g[index]+w

print("Minimal distance from "+str(w1)+" to "+str(w2)+" is: "+str(g[w2]))





