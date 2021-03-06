def Floyd(graph):
    length = len(graph)
    path = {}

    for i in range(length):
        path.setdefault(i, {})
        for j in range(length):
            if i == j:
                continue

            path[i].setdefault(j, [i,j])
            new_node = None

            for k in range(length):
                if k == j:
                    continue

                new_len = graph[i][k] + graph[k][j]
                if graph[i][j] > new_len:
                    graph[i][j] = new_len
                    new_node = k
            if new_node:
                path[i][j].insert(-1, new_node)

    return graph, path
