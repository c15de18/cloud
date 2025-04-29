from collections import deque

def add_edge(graph,u,v):
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph,vertex,visited):
    visited.add(vertex)
    print(vertex,end = ' ')

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)

def bfs(graph,start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end = ' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    graph = {0: [], 1:[], 2 : [], 3:[], 4 : []}

    add_edge(graph,0,1)
    add_edge(graph,0,2)
    add_edge(graph,1,3)
    add_edge(graph,1,4)
    add_edge(graph,2,4)

    print("Graph structure : ",graph)

    print("\nDFS Traversal starting from vertex 0: ")
    dfs(graph,0,set())

    print("\n\nBFS Traversal starting from vertex 0: ")
    bfs(graph,0)

if __name__ == "__main__":
    main()