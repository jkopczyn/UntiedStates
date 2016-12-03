import sys
from collections import defaultdict

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        vertices = set()
        adjacencies = defaultdict(set)
        for line in lines:
            tokens = line.split()
            vertices |= set(tokens)
            vertex, neighbors = tokens[0], tokens[1:]
            adjacencies[vertex] |= set(neighbors)
            for neighbor in neighbors:
                adjacencies[neighbor] |= {vertex}
    return {
        "vertices": vertices,
        "adjacencies": adjacencies
    }

def try_possibilities(graph):
    ordered_vertices = sorted(list(graph["vertices"]))
    pass

flatten_once = lambda l: [item for sublist in l for item in sublist]

def recurse_possibilites(graph, capitals, ordered_choices):
    if not evaluate_partition(graph, capitals):
        return []
    return flatten_once([
            recurse_possibilities(
                graph,
                capitals.union(set([capital])),
                ordered_choices[idx+1:]
                )
            for capital, idx in enumerate(ordered_choices)
        ])

def evaluate_partition(graph, capital_set):
    pass

if __name__ == '__main__':
    input_file = sys.argv[1] if (len(sys.argv) > 1) else "state-connections.txt"
    graph = parse_file(input_file)
    print graph
