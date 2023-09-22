


class Vertex(object):

    def __init__(self, name = None) -> None:
        self.name = name
        self.neighbours = []


    def __eq__(self, value) -> bool:
        return self.get_name() == value.get_name()
    
    #Dangerous not sure of behaviour later
    def __hash__(self) -> int:
        return hash(self.get_name())
    
    def get_name(self):
        return self.name
    