# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex start to vertex end.

# Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.


# Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2


# Runtime: 1692 ms, faster than 81.71% of Python online submissions for Find if Path Exists in Graph.
def solve_leet_find_if_path_exists_in_graph( n, edges, start, end):
    return solve( n, edges, start, end)

def solve( n, edges, start, end):
    vertexs = get_vertexs(edges)
    return traverse_and_find(vertexs,vertexs[start],end,[start])

def traverse_and_find(vertexs,children,end,visited):
    if end in children:
        return True

    for child in children :
        if child not in visited:
            visited.append(child)
            if traverse_and_find(vertexs,vertexs[child],end,visited):
                return True
    return False

def get_vertexs(edges):
    vertexs = {}
    for edge in edges:
        if edge[0] not in vertexs:
            vertexs[edge[0]] = []
        if edge[1] not in vertexs:
            vertexs[edge[1]] = []
        vertexs[edge[0]].append(edge[1])
        vertexs[edge[1]].append(edge[0])
    return vertexs
