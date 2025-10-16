def is_safe(v, graph, path, pos):
    # Check if vertex is adjacent to the previous vertex
    if graph[path[pos - 1]][v] == 0:
        return False
    # Check if vertex already included
    if v in path:
        return False
    return True


def hamiltonian_cycle_util(graph, path, pos):
    N = len(graph)
    if pos == N:
        # Check if last vertex connects to first
        return graph[path[pos - 1]][path[0]] == 1

    for v in range(1, N):
        if is_safe(v, graph, path, pos):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1  # Backtrack

    return False


def hamiltonian_cycle(graph):
    N = len(graph)
    path = [-1] * N
    path[0] = 0

    if not hamiltonian_cycle_util(graph, path, 1):
        print("No Hamiltonian Cycle exists.")
    else:
        print("Hamiltonian Cycle exists:")
        print(" -> ".join(map(str, path + [path[0]])))


# ---- Main Program ----
if __name__ == "__main__":
    N = int(input("Enter number of vertices: "))
    graph = []
    print("Enter adjacency matrix row by row:")
    for i in range(N):
        row = list(map(int, input().split()))
        graph.append(row)

    hamiltonian_cycle(graph)

