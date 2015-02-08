# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 12:18:58 2015

@author: GBR
"""
import math
import networkx as nx
from networkx.readwrite import json_graph
from random import randint
import matplotlib.pyplot as plt
import json

G = nx.Graph()

# definitions
number_of_nodes = 10    
number_of_edges_per_node = 2
file_name = 'euclidean_graph'

for i in xrange(number_of_nodes):
    G.add_node(i, x=randint(0,2 * number_of_nodes), y=randint(0,2 * number_of_nodes), label=i)
    
for i in xrange(number_of_nodes):
    edge_lengths = [(math.sqrt( (G.node[i]['x'] - G.node[j]['x'])**2 + (G.node[i]['y'] - G.node[j]['y'])**2),j) for j in xrange(number_of_nodes)]
    edge_lengths.sort()
    for j in xrange(1,number_of_edges_per_node+1):
        G.add_edge(i,edge_lengths[j][1],weight=round(edge_lengths[j][0],1))

x_pos =  nx.get_node_attributes(G,'x')
y_pos =  nx.get_node_attributes(G,'y')
pos = {}
for i in xrange(number_of_nodes):
    pos[i] = (x_pos[i],y_pos[i])

edge_labels = nx.get_edge_attributes(G,'weight')
for key in edge_labels:
    edge_labels[key] = round(edge_labels[key],1)
nx.draw(G, pos=pos, node_color='w')
nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_labels)
nx.draw_networkx_labels(G,pos=pos,labels=nx.get_node_attributes(G,'label'))

#nx.write_dot(G, 'weighted_graph.dot')

data = json_graph.node_link_data(G)
s = json.dumps(data)
#f = open(file_name + ".json",'w')
#f.write(s)
#f.close()
