#Dijkstra Algorithm following w3schools.com
#https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php

class Graph:
	def __init__(self,num_nodes):
		#create a matrix for the graph that holds all nodes and weights/travel time
		#set default val to 0
		self.adj_matrix= [[0]*num_nodes for _ in range(size)]
		self.num_nodes = num_nodes
		#creating a list to hold the names of the nodes
		self.nodes_list = [''] * num_nodes

	def add_edge(self, u, v, weight):
		# check to make sure node u and v are valid nodes in nodes list
		if 0 <= u < self.num_nodes and 0<= v < self.num_nodes
			self.adj_matrix[u][v] = weight
			self.adj_matrix[v][u] = weight #travel a-b should be same as b-a

	def add_node_data(self, node, data):
		if 0 <= node < self.num_nodes:
			self.nodes_list[node] = data

	def dijkstra(self, start_node):
		#finding the pos of the start node using the node name
		start_index = self.nodes_list.index(start_node)
		#set default values, traved to = false, fastest = inf, index at 0
		distances = [float('inf')] * self.num_nodes
		distances[start_index] = 0
		visited = [False] * self.num_nodes
		#create a list to keep track of the path
		predecessor = [None] * self.num_nodes

		#for each node
		for _ in range(self.num_nodes):
			min_dist = float('inf')
			u = None 
			#finding the next node to explore by using shortest path -min dist and not visited
			for i in range(self.num_nodes):
				if not visited[i] and distance[i] < min_dist:
					min_dist = distance[i]
					u = i
			#if no more nodes to explore break, otherwise updated visited list
			if u is None:
				break
			visited[u] = True

			for v in range(self.num_nodes):
				#checks to make sure path exists from u-v and not visited
				if self.adj_matrix[u][v] != 0 and not visited[v]:
					#checks new path weight using previous node weight + new path
					newpath = distance[u] + self.adj_matrix[u][v]
					if newpath < distance[v]:
						distance[v] = newpath
						predecessor[v] = u
		return distances, predecessor

		def get_path(self, predecessor, start_node, end_node):
			path=[]
			current = self.nodes_list.index(end_node)
			while current is not None:
				path.insert(0, self.nodes_list[current])
				current = predecessor[current]
				if current == self.nodes_list(start_node):
					path.insert(0, start_node)
					break
			return '->'.join(path)

