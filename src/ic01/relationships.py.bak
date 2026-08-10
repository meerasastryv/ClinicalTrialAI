from collections import defaultdict


def build_relationship_graph(requirements):
    graph = defaultdict(list)

    for req in requirements:
        for parent in req.links:
            graph[parent].append(req.id)

    return dict(graph)


def get_children(graph, req_id):
    return graph.get(req_id, [])


def print_graph(graph):
    for parent, children in graph.items():
        print(f"\n{parent}")
        for child in children:
            print(f"   └── {child}")
