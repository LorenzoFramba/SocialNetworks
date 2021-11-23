#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
# @author:Clarky Clark Wang
# @license: Apache Licence 
# @file: LoadData.py 
# @time: 2021/11/09
# @contact: wangz@kth,se
# @software: PyCharm 
# Import Libs and Let's get started, shall we?
from DataGene import *
import networkx as nx
from colour import Color
from networkx.drawing.nx_pydot import graphviz_layout
SIZE = 20
user, task, full = User_Task(SIZE)
relation = User_Friend(SIZE, user)
# print(relation.head())


def relation_graph(relation):
    G = nx.Graph()
    user_list = list(relation.username)
    user_idx_list = list(relation.index)
    for i in range(len(user_list)):
        G.add_node(user_idx_list[i], name = user_idx_list[i])
    for i in range(len(user_list)):
        friend_list = relation.iloc[i]['friends']
        if len(friend_list) == 0:
            pass
        else:
            for j in friend_list:
                G.add_edge(i, j)
    return G

# print(full.head())
def user_chain_graph(user_idx, full, task):
    G = nx.DiGraph()
    acts, tasks = full.activity[user_idx], full.task[user_idx]
    G.add_node(user_idx, name = full.username[user_idx])
    for idx in range(len(acts)):
        G.add_node(task.activity[idx])
        G.add_edge(user_idx, task.activity[idx])
        for j in range(len(tasks[idx])):
            G.add_node(task.task[idx][j])
            G.add_edge(task.activity[idx], task.task[idx][j])
    return G

def norm(nums):
    output = []
    num_min, num_max = min(nums), max(nums)
    for i in nums:
        output.append((i - num_min) / (num_max - num_min))
    return output

def degree_user_map(G, full):
    labels = {}
    nodes = []
    for i in range(len(G.nodes()) - 1):
        labels[i] = f'index: {i}'
    degree_sequence = [d for n, d in G.degree()]
    node_size = norm(degree_sequence)
    for i in range(len(G.nodes())):
        nodes.append(node_size[i] * 200)
    groups = list(nx.get_node_attributes(G, 'name').values())
    acts = []
    for i in groups:
        act = full.task[i]
        counter = 0
        for j in act:
            counter += len(j)
        acts.append(counter)
    acts = norm(acts)
    temp = sorted(acts)
    dic_color = {}
    blue = Color("lightsalmon")
    colors = list(blue.range_to(Color("brown"), len(acts)))
    for i in range(len(temp)):
        dic_color[temp[i]] = colors[i]
    final = [str(colors[0])]
    for j in acts:
        col = str(dic_color[j])
        final.append(col)
    print(final)
    fig = plt.figure("Degree of a random graph", figsize=(8, 8))
    # Create a gridspec for adding subplots of different sizes
    axgrid = fig.add_gridspec(5, 4)
    ax0 = fig.add_subplot(axgrid[0:3, :])
    Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    pos = nx.spring_layout(Gcc, seed=10396953)
    nx.draw_networkx_nodes(Gcc, pos, ax=ax0, node_size=nodes, node_color=final)
    nx.draw_networkx_edges(Gcc, pos, ax=ax0, alpha=0.4)
    nx.draw_networkx_labels(Gcc, pos, ax=ax0, alpha=0.4, labels=labels)
    ax0.set_title("Connected components of G")
    ax0.set_axis_off()
    ax1 = fig.add_subplot(axgrid[3:, :2])
    ax1.plot(degree_sequence, "b-", marker="o")
    ax1.set_title("Degree Plot")
    ax1.set_ylabel("Degree")
    ax1.set_xlabel("User-Index")
    ax2 = fig.add_subplot(axgrid[3:, 2:])
    ax2.bar(*np.unique(degree_sequence, return_counts=True))
    ax2.set_title("Degree histogram")
    ax2.set_xlabel("Degree")
    ax2.set_ylabel("# of Nodes")

    fig.tight_layout()
    plt.show()







# def total_graph(full, task):

# print(task.head())
# print(user_chain_graph(1, full))

# G = user_chain_graph(1, full, task)
# G = relation_graph(relation)
# tree = nx.dfs_tree(G, source=1)
# pos = graphviz_layout(tree, prog="twopi")
# nx.draw(tree, pos, with_labels = True)
# plt.show()
### Changing the Size and Coloring for the Node stands for importance
### Adding Interests for the User in Single User Graph
###

G = relation_graph(relation)
# print(G.nodes(data=True))
# print(full.head(5))
degree_user_map(G, full)