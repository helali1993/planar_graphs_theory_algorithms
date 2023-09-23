import copy
from Edge import Edge
from Vertex import Vertex



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

    def create_from_adjaceny_dict(self, adj_dict, duplicates = None) -> None:
        for key in adj_dict.keys():
            self.vertices.add(Vertex(key))
            for value in adj_dict[key]:
                self.vertices.add(Vertex(value))
                start_vx = Vertex(key) 
                end_vx = Vertex(value)
                if Edge(start_vx, end_vx) in self.edges:
                    pass
                else:
                    self.edges.append(Edge(start_vx, end_vx))

    def create_adjaceny_dict(self):
        pass

    def create_from_adjaceny_matrix(self, adj):
        pass

    def dfs(self):
        joker_vxs = copy.deepcopy(self.vertices)
        components = []

        for vx in self.vertices:
            if vx in joker_vxs:
                pass # dfs_helper()
    

    def dfs_helper(self, vx, joker_vxs):

        component = []


                
            

   
