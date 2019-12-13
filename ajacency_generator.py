import numpy as np
import scipy.sparse as sps
import csv
import networkx as nx
# import matplotlib.pyplot as plt
from conts import file_path
import pylab as plt



def generate_adjmatrix(adjlist, nodes):
    matrix = []
    for node in nodes:
        weights = {endnode:int(weight)
                   for w in adjlist.get(node, {})
                   for endnode, weight in w.items()}
        matrix.append([weights.get(endnode, 0) for endnode in nodes])
    matrix = numpy.array(matrix)
    return matrix + matrix.transpose()



def generate_adjlist():

	all_user_list=[]

	with open(file_path,'r') as fx:
		rows=csv.reader(fx)
		for row in rows:
			if row[0]=='user_id':
				continue




def gen_graph():

	G=nx.Graph()
	# G = nx.DiGraph()
	all_data=[]
	all_user_list=[]
	label_dict={}
	with open(file_path,'r') as fx:
		rows=csv.reader(fx)
		for row in rows:
			if row[0]=='follower_id':
				continue

			all_data.append(row)
			label_dict[row[1]]=row[6]
			all_user_list.append(row[1])
			G.add_nodes_from([row[1]])
			if row[3]=='1' and row[5]=='1':
				# one_edge.append(row[0],row[1])
				one_edge_tup=(row[0],row[1])

				G.add_nodes_from([row[1],row[2]])
				G.add_edges_from([(row[1],row[2])],color='green')



			elif row[3]=='1' and row[5]=='0':
				# one_edge.append(row[0],row[1])
				one_edge_tup=(row[0],row[1])
				# G.add_edges_from([(row[1],row[2])], color='green')
				# all_edges_one_side.append(one_edge_tup)
				# G.add_nodes_from([row[1],row[2]])
				G.add_edges_from([(row[1],row[2])],color='brown')	


			elif row[3]=='1' and row[5]=='0':
				# one_edge.append(row[0],row[1])
				one_edge_tup=(row[0],row[1])
				# G.add_edges_from([(row[1],row[2])], color='green')
				# all_edges_one_side.append(one_edge_tup)
				# G.add_nodes_from([row[1],row[2]])
				G.add_edges_from([(row[1],row[2])],color='black')		
				# label_dict[row[1]]=row[6]
				# label_dict[row[2]]=row[6]
	nx.draw(G,labels=label_dict,with_labels=True,pos=nx.circular_layout(G))
	plt.savefig("test_circular2.png") # save as png
	# plt.show()
	print G.nodes()
	print G.edges()





if __name__=='__main__':
	gen_graph()
