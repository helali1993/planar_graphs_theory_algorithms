from Graph import Graph
from Vertex import Vertex
from Edge import Edge


g = Graph()

u = Vertex(name=1)
v = Vertex(name=2)

# edge = Edge(u, v)

# g.add_edge_class(edge)


adj_dict = { '1' : {'2', '3'}, '2': set('1'), '3': set('1'), '4' : set('5'), '5': set('4')}

g.create_from_adjaceny_dict(adj_dict)



for vx in g.vertices:
    print(vx.get_name())


for ed in g.edges:
    print(ed.get_start().get_name(), ed.get_end().get_name())