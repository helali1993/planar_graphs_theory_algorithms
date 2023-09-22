import Edge
import Vertex



class Graph(object):
    
    def __init__(self) -> None:
        
        self.vertices = set()
        self.edges = []

    # creating graph if a list of edges of the class
    # type Edges.
    def add_edge_class(self, edge):

        self.vertices.add(edge.get_start())
        self.vertices.add(edge.get_end())
        self.edges.append(edge)

   
