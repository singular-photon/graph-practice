import abc
import numpy as np

# adding below line just because i love python 2 more than python 3 . "heart has its reasons!"
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()}) 
#  solution is from this answer : https://stackoverflow.com/questions/35673474/using-abc-abcmeta-in-a-way-it-is-compatible-both-with-python-2-7-and-python-3-5


class Graph(ABC):


	def __init__(self,numVertices,directed=False):

		self.numVertices=numVertices
		self.directed=directed

	@abc.abstractmethod
	def add_edge(self,v1,v2,weight):
		pass
	
	@abc.abstractmethod
	def get_adjacent_vertices(self,v):
		pass

	@abc.abstractmethod
	def get_indegree(self,v):
		pass
	
	@abc.abstractmethod
	def get_edge_weight(self,v1,v2):
		pass

	@abc.abstractmethod
	def display(self):
		pass

#  inheriting above abstract class to implemant aur graph as adjacency matrix representation of graph


class AdjacencyMatrixGraph(Graph):

	def __init__(self,numVertices,directed=False):

		super(AdjacencyMatrixGraph,self).__init__(numVertices,directed)

		self.matrix=np.zeros((numVertices,numVertices))


	def add_edge(self,v1,v2,weight=1):

		if v1>=self.numVertices or v2>=self.numVertices or v1<0 or v2<0:
			raise ValueError("the vertices entered are not part of the graph as planned ,buzz off: you entered %d and %d , one of them of both caused this error."%(v1,v2))

		if weight<1:
			raise ValueError("here we are implementing undirected and unweighted graph pass weight as 1 only")


		self.matrix[v1][v2]=weight

		if self.directed==False:
			self.matrix[v1][v2]=weight


	def get_adjacent_vertices(self,v):

		if v<0 or v>self.numVertices:
			raise ValueError("cannot find vertices aroung this as %d does not exist in the graph"%v)

		adjacent_vertices=[]
		for i in range(self.numVertices):
			if self.matrix[v][i]>0:
				adjacent_vertices.append(i)

		
		return adjacent_vertices


	def get_indegree(self,v):

		if v<0 or v>self.numVertices:
			raise ValueError("cannot find vertices aroung this as %d does not exist in the graph"%v)

		indegree=0
		for i in range(self.numVertices):
			if self.matrix[i][v]>0:
				indegree+=1

		return indegree

	def get_edge_weight(self,v1,v2):
		return self.matrix[v1][v2]


	def display(self):

		for i in range(self.numVertices):
			for v in self.get_adjacent_vertices(i):
				print (i,"-->",v)

g = AdjacencyMatrixGraph(4)

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)


for i in range(4):
	print("Adjacnet to",i,g.get_adjacent_vertices(i))

for i in range(4):
	print("Indegree of",i,g.get_indegree(i))


g.display()








		






