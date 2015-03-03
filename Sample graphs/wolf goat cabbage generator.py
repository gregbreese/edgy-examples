# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 12:18:58 2015

@author: GBR
"""
import math
import networkx as nx
from networkx.readwrite import json_graph
from random import shuffle
import matplotlib.pyplot as plt
import json


# definitions
size_of_grid = 5  
file_name = 'grid_graph'

#create nodes
G = nx.Graph()
for i in xrange(size_of_grid):
    for j in xrange(size_of_grid):
        G.add_node((i,j), x=i, y=j, label=str(i)+','+str(j))

#create edges
for i in xrange(size_of_grid-1):
    for j in xrange(size_of_grid):
        G.add_edge((i,j),(i+1,j))
for i in xrange(size_of_grid):
    for j in xrange(size_of_grid-1):
        G.add_edge((i,j),(i,j+1))
edges = G.edges()
weights = range(len(edges))
shuffle(weights)
for i in xrange(len(edges)):
    G.edge[edges[i][0]][edges[i][1]]['weight'] = weights[i] + 1
    
# attributes for plot
x_pos =  nx.get_node_attributes(G,'x')
y_pos =  nx.get_node_attributes(G,'y')
pos = {}
for i in x_pos:
    pos[i] = (x_pos[i],y_pos[i])
edge_labels = nx.get_edge_attributes(G,'weight')

#plot graph
nx.draw(G, pos=pos, node_color='w', node_size=600, style='dotted')
nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_labels)
nx.draw_networkx_labels(G,pos=pos,labels=nx.get_node_attributes(G,'label'))

#export as json
data = json_graph.node_link_data(G)
s = json.dumps(data)
f = open(file_name + ".json",'w')
f.write(s)
f.close()
