#Dijkstra Algorithm following w3schools.com
#https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php

class Graph:
	def __init__(self,num_nodes):
		#create a matrix for the graph that holds all nodes and weights/travel time
		#set default val to 0
		self.adj_matrix= [[0]*num_nodes for _ in range(num_nodes)]
		self.num_nodes = num_nodes
		#creating a list to hold the names of the nodes
		self.nodes_list = [''] * num_nodes

	def add_edge(self, u, v, weight, approx_dist):
		# check to make sure node u and v are valid nodes in nodes list
		if 0 <= u < self.num_nodes and 0<= v < self.num_nodes:
			self.adj_matrix[u][v] = weight
			self.adj_matrix[v][u] = weight #travel a-b should be same as b-a

	def add_node_data(self, node, data):
		if 0 <= node < self.num_nodes:
			self.nodes_list[node] = data

	def dijkstra(self, start_node):
		#finding the pos of the start node using the node name
		start_index = self.nodes_list.index(start_node)
		#set default values, traved to = false, fastest = inf, index at 0
		distance = [float('inf')] * self.num_nodes
		distance[start_index] = 0
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
		return distance, predecessor

	def get_path(self, predecessor, start_node, end_node):
		path=[]
		current = self.nodes_list.index(end_node)
		while current is not None:
			path.insert(0, self.nodes_list[current])
			current = predecessor[current]
			if current == self.nodes_list.index(start_node):
				path.insert(0, start_node)
				break
		return '->'.join(path)

class aGraph:
	def __init__(self,num_nodes):
		#create a matrix for the graph that holds all nodes and weights/travel time
		#set default val to 0
		self.adj_matrix= [[0]*num_nodes for _ in range(num_nodes)]
		self.approx_matrix = [[0] *num_nodes for _ in range(num_nodes)]
		self.num_nodes = num_nodes
		#creating a list to hold the names of the nodes
		self.nodes_list = [''] * num_nodes

	def add_edge(self, u, v, weight, approx_dist):
		# check to make sure node u and v are valid nodes in nodes list
		if 0 <= u < self.num_nodes and 0<= v < self.num_nodes:
			self.adj_matrix[u][v] = weight
			self.adj_matrix[v][u] = weight #travel a-b should be same as b-a
			self.approx_matrix[u][v] = weight + approx_dist
			self.approx_matrix[v][u] = weight + approx_dist

	def add_node_data(self, node, data):
		if 0 <= node < self.num_nodes:
			self.nodes_list[node] = data

	def astar(self, start_node, end_node):
		#finding the pos of the start node using the node name
		start_index = self.nodes_list.index(start_node)
		end_index = self.nodes_list.index(end_node)
		#set default values, traved to = false, fastest = inf, index at 0
		distance = [float('inf')] * self.num_nodes
		distance[start_index] = 0
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
			#if u is None:
			#	break
			visited[u] = True

			for v in range(self.num_nodes):
				#checks to make sure path exists from u-v and not visited
				if self.approx_matrix[u][v] != 0 and not visited[v]:
					#checks new path weight using previous node weight + new path
					newpath = distance[u] + self.approx_matrix[u][v]
					if newpath < distance[v]:
						distance[v] = distance[u] + self.adj_matrix[u][v]
						predecessor[v] = u
			if u is end_index:
				break
		return distance, predecessor

	def get_path(self, predecessor, start_node, end_node):
		path=[]
		current = self.nodes_list.index(end_node)
		while current is not None:
			path.insert(0, self.nodes_list[current])
			current = predecessor[current]
			if current == self.nodes_list.index(start_node):
				path.insert(0, start_node)
				break
		return '->'.join(path)

def run_dijkstra():
	g = Graph(7)

	g.add_node_data(0, 'A')
	g.add_node_data(1, 'B')
	g.add_node_data(2, 'C')
	g.add_node_data(3, 'D')
	g.add_node_data(4, 'E')
	g.add_node_data(5, 'F')
	g.add_node_data(6, 'G')

	g.add_edge(3, 0, 4)  # D -> A, weight 4
	g.add_edge(3, 4, 2)  # D -> E, weight 2
	g.add_edge(0, 2, 3)  # A -> C, weight 3
	g.add_edge(0, 4, 4)  # A -> E, weight 4
	g.add_edge(4, 2, 4)  # E -> C, weight 4
	g.add_edge(4, 6, 5)  # E -> G, weight 5
	g.add_edge(2, 5, 5)  # C -> F, weight 5
	g.add_edge(1, 2, 2)  # B -> C, weight 2
	g.add_edge(1, 5, 2)  # B -> F, weight 2
	g.add_edge(6, 5, 5)  # G -> F, weight 5

	# Dijkstra's algorithm from D to all vertices
	print("Dijkstra's Algorithm starting from vertex D:\n")
	distance, predecessor = g.dijkstra('D')
	for i, d in enumerate(distance):
		path= g.get_path(predecessor, 'D', g.nodes_list[i])
		print(f"{path}, Distance: {d}")

def run_astar():
	g = aGraph(7)

	g.add_node_data(0, 'A')
	g.add_node_data(1, 'B')
	g.add_node_data(2, 'C')
	g.add_node_data(3, 'D')
	g.add_node_data(4, 'E')
	g.add_node_data(5, 'F')
	g.add_node_data(6, 'G')

	g.add_edge(3, 0, 4, 5)  # D -> A, weight 4
	g.add_edge(3, 4, 2, 1)  # D -> E, weight 2
	g.add_edge(0, 2, 3, 1)  # A -> C, weight 3
	g.add_edge(0, 4, 4, 1)  # A -> E, weight 4
	g.add_edge(4, 2, 4, 1)  # E -> C, weight 4
	g.add_edge(4, 6, 5, 1)  # E -> G, weight 5
	g.add_edge(2, 5, 5, 1)  # C -> F, weight 5
	g.add_edge(1, 2, 2, 1)  # B -> C, weight 2
	g.add_edge(1, 5, 2, 1)  # B -> F, weight 2
	g.add_edge(6, 5, 5, 1)  # G -> F, weight 5
	g.add_edge(3, 1, 4, 10)

	# Dijkstra's algorithm from D to all vertices
	print("Dijkstra's Algorithm starting from vertex D:\n")
	distance, predecessor = g.astar('D', 'A')
	for i, d in enumerate(distance):
		path= g.get_path(predecessor, 'D', g.nodes_list[i])
		print(f"{path}, Distance: {d}")

def main():
	#run_dijkstra()
	run_astar()


if __name__ == "__main__":
    main()

