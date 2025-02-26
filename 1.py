import pandas as pd
import numpy

class Graph:
	def __init__(self, number_nodes):
		self.number_nodes=number_nodes
		self.shortest_path = [float('inf')] * number_nodes
		#create adj matrix to store edges
		self.adj_matrix = [[0]*number_nodes for _ in range(number_nodes)]

	def add_edge(self, node1, node2, weight):
		#explicit type conversion to int for nodes and subtract1 since index starts at pos 0
		node1,node2 = int(node1), int(node2)
		self.adj_matrix[node1][node2] = float(weight)
		#directed graph
		self.adj_matrix[node2][node1] = float(weight)

	def dijkstra(self, start_node, end_node):
		visited_matrix = []
		unvisited_matrix = [i for i in range(self.number_nodes)]
		next_node = start_node
		self.shortest_path[start_node] = 0

		while(len(visited_matrix) < self.number_nodes):
			#find edges from next_Node
			for i in range(len(self.adj_matrix[next_node])):
				#if a path exists
				if self.adj_matrix[next_node][i] > 0:
					#updates shortest path if the new dist(travel to next node + distance to i) < shortest_path[i]
					if (self.adj_matrix[next_node][i] + self.shortest_path[next_node]) < self.shortest_path[i]:
						self.shortest_path[i] = self.adj_matrix[next_node][i] +self.shortest_path[next_node]
			#print(next_node)
			#print(self.shortest_path)
			visited_matrix.append(next_node)
			unvisited_matrix.remove(next_node)
			#find nextnode to take
			min_dist = float('inf')
			for node in unvisited_matrix:
				if self.shortest_path[node] < min_dist:
					min_dist = self.shortest_path[node]
					next_node = node
		print(self.shortest_path)


def main():
	df = pd.read_csv('input.txt', header=None)
	total_nodes = int(df.iloc[0].values[0])
	start_node = int(df.iloc[1].values[0])
	end_node = int(df.iloc[2].values[0])
	df = pd.read_csv('input.txt', skiprows=3, header=None,sep=r'\s+')
	#print(df)

	g = Graph(total_nodes) 
	for index,row in df.iterrows():
		#subtract 1 since matrx pos starts at 0, so 1st node = position 0
		g.add_edge(row[0]-1, row[1]-1, row[2])
	g.dijkstra(start_node-1, end_node-1)


if __name__ == "__main__":
    main()
