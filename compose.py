# read words from files
# generate a graph for the files
import sys
from graph import Node, Graph


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

    if word not in graph.get_all_nodes():
        return "not in file"
    for i in range(150):
        node = graph.get_node(word)
        print(node.value + " ")
        word = node.next_word.value
    return "done"
    

def main():
    
    print("c")
    file_path = "test.txt"
    words = read_words(file_path)
    print("a")
    g = Graph()
    g = add_to_graph(g, words)
    g.generate_probability_maps()
    print("b")
    print_word = genarating_words(g, words[-1])
    print(print_word)



if __name__ == " __main__":
    main()
