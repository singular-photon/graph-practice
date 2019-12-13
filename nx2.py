import networkx as nx
import csv
import matplotlib.pyplot as plt
import pygraphviz as pgv
from pygraphviz import *
import collections
import json
from networkx_viewer import Viewer
from io import BytesIO
import pylab as plt
from const import file_path
from networkx.drawing.nx_agraph import graphviz_layout


#Creating the NULL graph
G = nx.DiGraph()
# G=nx.Graph()
all_user_data=[]

with open(file_path,'r') as f:

	read = csv.reader(f)
	for row in read:
		# print row

		all_user_data.append([row[0],row[1],row[2],row[5]])

		# G.add_edge(row[2],row[1],color='red')


all_unique_users=[]
all_ref_unique=[]
for x in range(1,len(all_user_data)):
	that_user=all_user_data[x]

	if that_user[2]==None or that_user[2]=="" or len(that_user[2])<1:
		continue
	all_ref_unique.append(that_user[2])
	G.add_edge(that_user[2],that_user[1], weight=-1,color='green')



def hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, 
                  pos = None, parent = None):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node of current branch
       width: horizontal space allocated for this branch - avoids overlap with other branches
       vert_gap: gap between levels of hierarchy
       vert_loc: vertical location of root
       xcenter: horizontal location of root
       pos: a dict saying where all nodes go if they have been assigned
       parent: parent of this branch.'''
    if pos == None:
        pos = {root:(xcenter,vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    neighbors = list(G.neighbors(root)) 
    if parent != None:   #this should be removed for directed graphs.
        try:
        	neighbors.remove(parent)  #if directed, then parent not in neighbors.
    	except:
    		pass
    if len(neighbors)!=0:
        dx = width/len(neighbors) 
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = hierarchy_pos(G,neighbor, width = dx, vert_gap = vert_gap, 
                                vert_loc = vert_loc-vert_gap, xcenter=nextx, pos=pos, 
                                parent = root)
    return pos


pos = hierarchy_pos(G,'albert')    
nx.draw(G, pos=pos, with_labels=True)
plt.savefig('hierarchy.png')


# for node in source:
# 	for sink in sink_nodes:
# 		if node!=sink:
# 			for path in nx.all_simple_paths(G,source=node,target=sink):
# 				print path

# app = Viewer(G)
# app.mainloop()

# fig = plt.figure()
# plt.axis('off')
# nx.draw_networkx(G, node_size=5, node_color='c', font_size=0.1)
# network_graph = BytesIO()
# fig.savefig("abc", format='png',dpi=1000)

# plt.savefig("graph.png", dpi=1000)
# nx.draw(G, pos=graphviz_layout(G), node_size=1, cmap=plt.cm.Blues,
#         node_color=range(len(G)),
#         prog='dot')
# plt.show()
