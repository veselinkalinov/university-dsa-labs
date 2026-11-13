graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C"]}


def dfs(graph, start):
    visited = set()

    def visit(node):
        visited.add(node)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)


dfs(graph, "A")
