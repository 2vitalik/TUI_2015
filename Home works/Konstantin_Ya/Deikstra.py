__author__ = 'Kostik'
a = {
      1:{2:20,3:30},
      2:{1:20,3:7,4:5},
      3:{1:30,2:7,4:10},
      4:{2:5,3:10,5:93},
      5:{3:7,4:93}
    }
v=[1,2,3,4,5]
g=[None]*5
for l in range(0,5):
     for u,w in a[l].items:
         if g[l]is None or g[l]>g[l]+w:g[l]+=w
min = g[0]
for b in range(0,5,1):
    if g[b]< min:
        min = g[b]
print(min)



