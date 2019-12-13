import networkx as nx
import csv
import matplotlib.pyplot as plt
import pygraphviz as pgv
from pygraphviz import *
import collections
import json
from const import file_path
from networkx_viewer import Viewer
from io import BytesIO
import pylab as plt
from networkx.drawing.nx_agraph import graphviz_layout
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models.graphs import from_networkx

#Creating the NULL graph
G = nx.DiGraph()
# G=nx.Graph()
all_user_data=[]


def get_name(number):

	all_data=[]

	with open(file_path,'r') as f:

		read = csv.reader(f)
		for row in read:
			# print row

			all_data.append([row[0],row[1],row[2],row[5]])	

	for x in all_data:
		if x[1]==number:
			return x[3]


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
	G.add_edge(that_user[2],that_user[1],color='green')





# fh=open("test.csv",'wb')
# nx.write_edgelist(G, fh)

sink_nodes = [node for node,outdegree in G.out_degree(G.nodes()) if outdegree==0]
source = [node for node,outdegree in G.in_degree(G.nodes()) if outdegree>=1]


# 9930712524
all_rep_nodes=[]
for node in source:
	print "\n\n\n"
	print node
	outde=G.out_degree(node)
	# if outde<=2:
	# 	continue
	if node in all_rep_nodes:
		continue


	for sink in sink_nodes:
		if node!=sink:
			for path in nx.all_simple_paths(G,source=node,target=sink):
				print path

				if len(path)>2:
					one_path=[]
					for z in path:
						outd=G.out_degree(z)
						if outd<=2:
							all_rep_nodes.append(z)
						tup1=(z,outd)
						one_path.append(tup1)
					with open('connections.csv','a') as newFile:
						newfile=csv.writer(newFile)
						name=get_name(path[0])
						newfile.writerow([name,path[0],len(path),one_path,path[len(path)-1]])
				# if len(path)>6:
				# 	print path,"    ",len(path)
				# 	break
		# print "-------------------------"



# plot = figure(title="Networkx Integration Demonstration", x_range=(-1000.1,1000.1), y_range=(-1000.1,1000.1),
#               tools="", toolbar_location=None)

# graph = from_networkx(G, nx.spring_layout, scale=100, center=(0,0))
# # graph = from_networkx(G, nx.spectral_layout, scale=1000)
# # spectral_layout
# plot.renderers.append(graph)

# output_file("networkx_graph.html")
# show(plot)

app = Viewer(G)
app.mainloop()

fig = plt.figure()
plt.axis('off')
nx.draw_networkx(G, node_size=5, node_color='c', font_size=0.1)
network_graph = BytesIO()
fig.savefig("abc", format='png',dpi=1000)

plt.savefig("graph.png", dpi=1000)
nx.draw(G, pos=graphviz_layout(G), node_size=1, cmap=plt.cm.Blues,
node_color=range(len(G)),prog='dot')
plt.show()

