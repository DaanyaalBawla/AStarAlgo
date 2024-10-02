def aStarAlgo(start, stop):
    open_set = set(start)
    closed_set = set()
    g = {}
    parents = {}

    g[start] = 0
    parents[start] = start

    while len(open_set) > 0:
        n = None

        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop or Graph[n] == None:
            pass
        else:
            for (m, weight) in neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('There is no path.')
            return None

        if n == stop:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start)

            path.reverse()

            print('Final solution: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('There is no path.')
    return None


def neighbors(v):
    if v in Graph:
        return Graph[v]
    else:
        return None


def heuristic(n):
    H_distance = {
        'A': 8,
        'B': 9,
        'C': 7,
        'D': 4,
        'E': 3,
        'F': 0,
        'G': 6,
        'H': 6,
        'S': 10,
    }
    return H_distance[n]


Graph = {
    'S':[('B',2),('A',3),('C',5)],
    'A': [('C', 3), ('G', 2)],
    'B': [('D', 6), ('A', 4)],
    'C': [('B', 4), ('H', 3)],
    'D': [('E', 2), ('F', 3)],
    'E': [('F', 5)],
    'F':None,
    'G': [('D', 4), ('E', 5)],
    'H': [('A', 4), ('D', 4)],

}
aStarAlgo('S', 'F')