#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
# @author:Clarky Clark Wang
# @license: Apache Licence 
# @file: demo.py 
# @time: 2021/11/09
# @contact: wangz@kth,se
# @software: PyCharm 
# Import Libs and Let's get started, shall we?
import networkx as nx
import matplotlib.pyplot as plt
# define a graph, some nodes with a "Type" attribute, some without.
G = nx.Graph()
G.add_nodes_from([1,2,3], Type='MASTER')
G.add_nodes_from([4,5], Type='DOC')
G.add_nodes_from([6])


# extract nodes with specific setting of the attribute
master_nodes = [n for (n,ty) in \
    nx.get_node_attributes(G,'Type').items() if ty == 'MASTER']
doc_nodes = [n for (n,ty) in \
    nx.get_node_attributes(G,'Type').items() if ty == 'DOC']
# and find all the remaining nodes.
other_nodes = list(set(G.nodes()) - set(master_nodes) - set(doc_nodes))

# now draw them in subsets  using the `nodelist` arg
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, nodelist=master_nodes, \
    node_color='red', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=doc_nodes, \
    node_color='blue', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=other_nodes, \
    node_color='purple', node_shape='s')
plt.show()