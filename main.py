from Graph import Graph
from Vertex import Vertex
from Edge import Edge


g = Graph()

u = Vertex(name=1)
v = Vertex(name=2)

edge = Edge(u, v)

g.add_edge_class(edge)
