
import Vertex

class Edge(object):


    def __init__(self, start:Vertex = None, end:Vertex = None) -> None:
        
        self.start = start
        self.end = end

    def __eq__(self, __value: object) -> bool:
        if type(__value) != type(Edge()):
            return False
        return ((self.start == __value.start and self.end == __value.end)
                or (self.start == __value.end and self.end == __value.start))
    

    def get_start(self) -> Vertex:
        return self.start

    def get_end(self) -> Vertex:
        return self.end 