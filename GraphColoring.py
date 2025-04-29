
def is_safe(graph,color,c,node):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True

def graph_coloring(graph,m,color,node):
    if node == len(graph):
        return True

    for c in range(1,m+1):
        if is_safe(graph,color,c,node):
            color[node] = c
            if graph_coloring(graph,m,color,node+1):
                return True
            color[node] = 0
    
    return False

def main():
    graph = [
        [0,1,1,1],
        [1,0,1,0],
        [1,1,0,1],
        [1,0,1,0]
    ]

    m = 3

    color = [0] * len(graph)

    if graph_coloring(graph,m,color,0):
        print("Solution exists!Coloring is : ")
        print(color)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()

