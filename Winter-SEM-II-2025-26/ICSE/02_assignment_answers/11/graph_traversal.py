from typing import List

from graph import DiGraph, Vertex


def depth_first_search(g: DiGraph, node: Vertex) -> List[Vertex]:
    g.reset()
    visited_nodes: List[Vertex] = []
    dfs(g, node, visited_nodes)
    return visited_nodes


def dfs(g: DiGraph, vertex: Vertex, visited_nodes: List[Vertex]) -> Vertex:
    vertex.visited = True
    visited_nodes.append(vertex)
    for v in g.get_neighbors(vertex):
        if v.visited is False:
            dfs(g, v, visited_nodes)
    return vertex


def breath_first_search(g: DiGraph, node: Vertex) -> List[Vertex]:
    g.reset()
    visited_nodes: List[Vertex] = []
    node.visited = True
    neighbour_queue = g.get_neighbors(node)
    visited_nodes.append(node)
    while len(neighbour_queue) > 0:
        current = neighbour_queue.pop(0)
        if current.visited is False:
            current.visited = True
            visited_nodes.append(current)
            for neighbour in g.get_neighbors(current):
                if neighbour.visited is False:
                    neighbour_queue.append(neighbour)
    return visited_nodes


if __name__ == "__main__":
    v_1 = Vertex(1)
    v_2 = Vertex(2)
    v_3 = Vertex(3)
    v_4 = Vertex(4)
    v_5 = Vertex(5)
    v_6 = Vertex(6)
    v_7 = Vertex(7)
    v_8 = Vertex(8)

    nodes = [v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8]
    edges = [
        (v_1, v_3), (v_1, v_6), (v_1, v_8),
        (v_2, v_8),
        (v_3, v_1), (v_3, v_7),
        (v_4, v_5), (v_4, v_5),
        (v_5, v_4), (v_5, v_6), (v_5, v_7), (v_5, v_8),
        (v_6, v_1), (v_6, v_4), (v_6, v_5),
        (v_7, v_3), (v_7, v_5),
        (v_8, v_1), (v_8, v_2), (v_8, v_5)
    ]

    g = DiGraph(nodes=nodes, edges=edges)

    print(depth_first_search(g, v_1))
    assert depth_first_search(g, v_1) == [v_1, v_3, v_7, v_5, v_4, v_6, v_8, v_2]

    print(breath_first_search(g, v_1))
    assert breath_first_search(g, v_1) == [v_1, v_3, v_6, v_8, v_7, v_4, v_5, v_2]
