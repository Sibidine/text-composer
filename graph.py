import random

class Node:
    def __init__(self, value):
        
        self.value = value
        self.adjacent = {}
        self.neighbours = []
        self.neighbour_weights = []

    def add_edge(self, node, weight=0):
        
        self.adjacent[node] = weight

    def get_probability_map(self):
        for node, weight in self.adjacent.items():
            self.neighbours.append(node)
            self.neighbour_weights.append(weights)

    def next_word(self):
        
        'sum_values = 0
        for node in self.adjacent.keys():
            sum_values+= node.value

        divisions = {}
        for value in self.adjacent.keys():
            probability = value/sum_values
            
            if divisions:
                probability = probability + divisions[-1]
            
            divisions[value] = probability

        random_number = random.uniform(0,1)

        for key, value in division.items():

            if value > random_number:
                return key'
        
        return random.choices(self.neighbours,weights=self.neighbour_weights)[0]




    
def Graph:
    def __init__(self):
        
        self.nodes = {}

    def get_all_values(self):
        
        return set(self.nodes.keys())

    def add_node(self,value):
        
        self.nodes[value] = Node(value)

    def get_node(self, value)
        
        if(value not in self.nodes):
            self.add_node(value)

        return self.nodes[value]

    def get_next_word(self, current_node):

        return self.node[current_node.value].next_word()

    def generate_probability_maps(self):
        for node in self.nodes.values():
            node.get_probability_map()




