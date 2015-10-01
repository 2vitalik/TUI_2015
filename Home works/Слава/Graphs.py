#!/usr/bin/env python

import networkx as nx
import matplotlib.pyplot as plot

G = nx.Graph()


G.add_edge(1, 2, weight=2)
G.add_edge(1, 6, weight=8)
G.add_edge(2, 6, weight=9)
G.add_edge(2, 3, weight=11)
G.add_edge(2, 7, weight=10)
G.add_edge(3, 7, weight=5)
G.add_edge(3, 4, weight=3)
G.add_edge(4, 7, weight=6)
G.add_edge(4, 5, weight=12)
G.add_edge(5, 7, weight=7)
G.add_edge(5, 6, weight=4)
G.add_edge(6, 7, weight=13)

plot.axis('off')
pos=nx.spring_layout(G)
nx.draw(G,pos)

edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G,pos,edge_labels)

print "Shortest path from 1 to 4: "
#print(nx.dijkstra_path(G, 1, 4))
Answ = nx.dijkstra_path(G, 1, 4)
for a in Answ:
    if a!=len(Answ):
        print a, "-->",
    else:
        print a
print "Length of this path: "
print(nx.dijkstra_path_length(G, 1, 4))
plot.show()

'''
e=[('a', 'b', 2),
   ('a','f', 8),
   ('b','f',9),
   ('b','c',11),
   ('b','g',10),
   ('c','g',5),
   ('c','d',3),
   ('d','g',6),
   ('d','e',12),
   ('e','g',7),
   ('e','f',4),
   ('f','g',13)]
G.add_weighted_edges_from(e)
print(nx.dijkstra_path(G, 'a', 'd'))
'''

'''N = {
    1: {2: 3, 3: 5, 6: 15},
    2: {4: 4},
    3: {4: 1},
    4: {5: 2, 6: 6},
    5: {6: 1},
    6: 0

}

ListOfAnswers = []
l = 1

while l != len(N):
    min = 1000
    for k in N[l]:
        if min > N[l][k]:
            min = k
    l = min
    ListOfAnswers.append(min)
print "End is: ", ListOfAnswers'''


