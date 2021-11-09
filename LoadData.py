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
SIZE = 10
user, task, full = User_Task(SIZE)
relation = User_Friend(SIZE, user)
# print(relation.head())


def relation_graph(relation):
    G = nx.Graph()
    user_list = list(relation['username'])
    user_idx_list = list(relation.index)
    for i in range(len(user_list)):
        G.add_node(user_idx_list[i], name = user_list[i])
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
    G = nx.Graph()
    acts, tasks = full.activity[user_idx], full.task[user_idx]
    G.add_node(user_idx, name = full.username[user_idx])
    for idx in range(len(acts)):
        G.add_node(task.activity[idx])
        G.add_edge(user_idx, task.activity[idx])
        for j in range(len(tasks[idx])):
            G.add_node(task.task[idx][j])
            G.add_edge(task.activity[idx], task.task[idx][j])
    return G
# print(task.head())
# print(user_chain_graph(1, full))

# G = user_chain_graph(1, full, task)
G = relation_graph(relation)
nx.draw_networkx(G)
plt.show()