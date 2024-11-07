
class Graph:
    """
    Graph datastructure implemented adjacency list representation
        - Undirected graph
        - Non-weighted graph
    """
    def __init__(self):
        """Instantiate graph using dict ds"""
        self.graph = {}

    def add_vertex(self, vertex) -> bool:
        """Add new vertex to graph"""
        if vertex not in self.graph:
            self.graph[vertex] = []
            return True
        else:
            print('Vertex already exist in the graph')
            return True

    def add_edges(self, v1, v2) -> bool:
        """Add new edge from vertex v1 to vertex v2"""
        if v1 not in self.graph:
            print(v1, "not exist in graph")
            return False
        elif v2 not in self.graph:
            print(v2, "not in graph")
            return False
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
            return True

    def delete_vertex(self, vertex) -> bool:
        """Delete a vertex from graph"""
        if vertex not in self.graph:
            print('Vertex not found in the Graph')
            return False
        for ver in self.graph:
            if vertex in self.graph[ver]:
                self.graph[ver].remove(vertex)
            del self.graph[vertex]
            return True

    def delete_edge(self, v1, v2) -> bool:
        """Remove edge from v1 to v2 and v2 to v1"""
        # check weather v1 and v2 present in the graph or not
        if v1 not in self.graph:
            print(v1, "not in graph")
            return False
        elif v2 not in self.graph:
            print(v2, " not in graph")
            return False
        # Remove v1 from v2 list and v2 from v1 list
        self.graph[v1].remove(v2)
        self.graph[v2].remove(v1)
        return True

    def DFS(self) -> list:
        """Depth First search approach to traverse through the elements of graph"""
        result_arr = []  # you can use set instead of list for efficient lookup,
        # but I am using list for testing.

        def _DFS(node, visited):
            if node not in self.graph:
                print('Node is not found')
                return
            if node not in visited:
                visited.append(node)
                print(node, end=' ')

                for x in self.graph[node]:
                    _DFS(x, visited)
        _DFS(self, result_arr)
        return result_arr

    def BFS(self, node) -> list:
        """Breadth First search approach to traverse through the elements of graph"""
        visited = []
        queue = [node]
        while queue:
            val = queue.pop(0)
            print(val, end=" ")
            for x in self.graph[val]:
                if x not in visited:
                    queue.append(x)
                    visited.append(x)
        return visited;

    def __str__(self):
        return str(self.graph)



