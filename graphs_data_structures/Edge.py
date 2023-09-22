
import Vertex

class Edge(object):


    def __init__(self, start:Vertex, end:Vertex) -> None:
        
        self.start = start
        self.end = end

    def get_start(self) -> Vertex:
        return self.start

    def get_end(self) -> Vertex:
        return self.end 