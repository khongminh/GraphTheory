def adjacencyMatrix(nodes, edges):
    A = [[0]*nodes for _ in range(nodes)]

    for i in range(edges):
        print("Enter edge {0}: ".format(i+1))
        x,y = map(int, input().split())
        A[x-1][y-1] = 1
    return A


def adjacencyList(nodes, edges, isDirect = False):
    A = {};
    for node in nodes:
        A[node] = []
    for i in range(edges):
        print("Enter edge {0}: ".format(i+1))
        x,y = input().split()
        A[x].append(y)
        if not isDirect:
            A[y].append(x)
    return A


