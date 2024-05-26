# read words from files
# generate a graph for the files
import sys
from graph add Node, Graph


def read_words(file_name):

    words = []

    with open(file_name) as file:
        for line in file:
            for word in line.split():
                words.append(word)


    return words

def add_to_graph(graph, words):

    for word in words:
        graph.add_node(word)

    return graph

def generating_words(graph, word):
    

def main():
    
    file_path = sys.argv[1:]
    words = read_words(file_path)

    g = Graph()
    g = add_to_graph(g, words)




if __name__ ==" __main__":
    main()
