# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 20:24:49 2015

@author: GBR
"""
import sys
import math
import networkx as nx
from networkx.readwrite import json_graph
from random import randint
import matplotlib.pyplot as plt
import json

def plot_graph(data):
    #load the graph
    G = json_graph.node_link_graph(json.loads(data))
    
    #attributes for plot
    x_pos =  nx.get_node_attributes(G,'x')
    y_pos =  nx.get_node_attributes(G,'y')
    pos = {}
    for i in xrange(G.number_of_nodes()):
        pos[i] = (x_pos[i],y_pos[i])

    node_labels = nx.get_node_attributes(G,'label')
    if len(node_labels) == 0:
        for i in xrange(G.number_of_nodes()):
            node_labels[i] = i
    edge_labels = nx.get_edge_attributes(G,'weight')
    for key in edge_labels:
        edge_labels[key] = round(edge_labels[key],1)
    #plot
    nx.draw(G, pos=pos, node_color='w')
    nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_labels)
    nx.draw_networkx_labels(G,pos=pos,labels=node_labels)
    plt.show()

if __name__ == "__main__":    
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = input_data_file.read()
        input_data_file.close()

        plot_graph(input_data)
    else:
        print 'File name argument required.'

