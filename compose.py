# read words from files
# generate a graph for the files
import sys
import string
from graph import Node, Graph
import re

def find_https_url(line):
    pattern = r'https://[^\s]+'
    return bool(re.match(pattern, line))

def find_phone_number(line):
    pattern = r'\b\d{10\b}'
    return bool(re.match(pattern, line))

def filter_non_alphanumeric(word):
    pattern = r'[^a-zA-Z0-9]'
    return re.sub(pattern, '', word)



def read_words(file_name):

    words = []

    with open(file_name) as file:
        for line in file:
            if '<Media omitted>' in line:
                continue
            for word in line.split():
                if find_https_url(word) or find_phone_number(word):
                    continue
                word = filter_non_alphanumeric(word)
                word = word.lower()
                word = word.translate(str.maketrans('','',string.punctuation))
                words.append(word)


    return words

def add_to_graph( words):

    graph = Graph()

    previous_word = None

    for word in words:
        word_node = graph.get_node(word)

        if previous_word:
            previous_word.increment_edge(word_node)

        previous_word = word_node
    
    return graph

def generating_words(graph, word):

    string = ""
    if word not in graph.get_all_values():
        return "not in file"
    for i in range(150):
        node = graph.get_node(word)
        string = string +node.value + " "
        word = node.next_word().value
    print(string)
    return "done"
    

def compose(file_path):
    
    words = read_words(file_path)
    g = add_to_graph(words)
    g.generate_probability_maps()
    status_word = generating_words(g, words[0])

