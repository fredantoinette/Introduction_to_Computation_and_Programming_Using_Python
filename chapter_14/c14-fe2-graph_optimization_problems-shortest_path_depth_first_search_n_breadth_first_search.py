"""
Consider a diagraph with weighted edges. Is the first path found by BFS 
guaranteed to minimise the sum of the weights of the edges?
"""


class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self._name = name
    def get_name(self):
        return self._name
    def __str__(self):
        return self._name
    
class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self._src = src
        self._dest = dest
    def get_source(self):
        return self._src
    def get_destination(self):
        return self._dest
    def __str__(self):
        return self._src.get_name() + "->" + self._dest.get_name()
    
class Weighted_edge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        """Assumes src and dest are nodes, weight a number"""
        self._src = src
        self._dest = dest
        self._weight = weight
    def get_weight(self):
        return self._weight
    def __str__(self):
        return (f"{self._src.get_name()}->({self._weight})" +
                f"{self._dest.get_name()}")
    

class Digraph(object):
    # nodes is a list of the nodes in the graph
    # edges is a dict mapping each node to a list of its children
    def __init__(self):
        self._nodes = []
        self._edges = {}
    def add_node(self, node):
        if node in self._nodes:
            raise ValueError("Duplicate node")
        else:
            self._nodes.append(node)
            self._edges[node] = []
    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        w = edge.get_weight()
        if not (src in self._nodes and dest in self._nodes):
            raise ValueError("Node not in graph")
        self._edges[src].append((dest, w))
    def children_of(self, node):
        return self._edges[node]
    def has_node(self, node):
        return node in self._nodes
    def __str__(self):
        result = ""
        for src in self._nodes:
            for dest in self._edges[src]:
                result = (result + src.get_name() + "->"
                          + "(" + str(dest[1]) + ")"
                          + dest[0].get_name() + "\n")
        return result[:-1] # omit final newline
    
class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)
        
        
def print_path(path):
    """Assumes path is a list of nodes"""
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + "->"
    return result

def BFS(graph, start, end, to_print = False):
    """Assumes graph is a Digraph; start and end are nodes
    Returns a shortest weighted path from start to end in graph"""
    init_path = [start]
    path_queue = [init_path]
    weight_queue = [0]
    shortest_weighted_path = []
    shortest_weighted_weight= 0
    while len(path_queue) != 0:
        # Get and remove oldest element in path_queue and weight_queue
        tmp_path = path_queue.pop(0)
        tmp_weight = weight_queue.pop(0)
        if shortest_weighted_weight == 0 or shortest_weighted_weight > tmp_weight:
            if to_print:
                print("Current BFS path:", print_path(tmp_path) + ",", "weight =", tmp_weight)
            last_node = tmp_path[-1]
            if last_node == end:
                shortest_weighted_path, shortest_weighted_weight = tmp_path, tmp_weight
            for next_node, next_weight in graph.children_of(last_node):
                if next_node not in tmp_path:
                    new_path = tmp_path + [next_node]
                    new_weight = tmp_weight + next_weight
                    path_queue.append(new_path)
                    weight_queue.append(new_weight)
    return shortest_weighted_path, shortest_weighted_weight


def test_SWP():
    nodes = []
    for name in range(6): # create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Weighted_edge(nodes[0], nodes[1]))
    g.add_edge(Weighted_edge(nodes[1], nodes[2]))
    g.add_edge(Weighted_edge(nodes[2], nodes[3]))
    g.add_edge(Weighted_edge(nodes[2], nodes[4]))
    g.add_edge(Weighted_edge(nodes[3], nodes[4]))
    g.add_edge(Weighted_edge(nodes[3], nodes[5]))
    g.add_edge(Weighted_edge(nodes[0], nodes[2]))
    g.add_edge(Weighted_edge(nodes[1], nodes[0]))
    g.add_edge(Weighted_edge(nodes[3], nodes[1]))
    g.add_edge(Weighted_edge(nodes[4], nodes[0]))
    print("Directed graph:")
    print(g, "\n")
    swp = BFS(g, nodes[0], nodes[5], to_print = True)
    print("Shortest weighted path found by BFS:", print_path(swp[0]) + ",", "weight =", swp[1])
    
test_SWP()

print("\n-----\n")

def test_SWP_2():
    nodes = []
    for name in range(10): # create 10 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Weighted_edge(nodes[0], nodes[1]))
    g.add_edge(Weighted_edge(nodes[1], nodes[2]))
    g.add_edge(Weighted_edge(nodes[2], nodes[3]))
    g.add_edge(Weighted_edge(nodes[2], nodes[4]))
    g.add_edge(Weighted_edge(nodes[3], nodes[4]))
    g.add_edge(Weighted_edge(nodes[3], nodes[5]))
    g.add_edge(Weighted_edge(nodes[0], nodes[2]))
    g.add_edge(Weighted_edge(nodes[1], nodes[0]))
    g.add_edge(Weighted_edge(nodes[3], nodes[1]))
    g.add_edge(Weighted_edge(nodes[4], nodes[0]))
    g.add_edge(Weighted_edge(nodes[0], nodes[3], 3.0))
    g.add_edge(Weighted_edge(nodes[5], nodes[6], 5.0))
    g.add_edge(Weighted_edge(nodes[3], nodes[6], 7.5))
    g.add_edge(Weighted_edge(nodes[5], nodes[3]))
    print("Directed graph:")
    print(g, "\n")
    swp_2 = BFS(g, nodes[0], nodes[6], to_print = True)
    print("Shortest weighted path found by BFS:", print_path(swp_2[0]) + ",", "weight =", swp_2[1])
    
test_SWP_2()