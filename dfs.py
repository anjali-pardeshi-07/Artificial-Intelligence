visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


user_size = int(input("How many nodes: "))
graph = {}

for i in range(user_size):
    get_node = input("Enter node name: ")
    get_neighs = input("Enter connected nodes as space separated: ")
    
    if len(get_neighs)!=0:
        temp_neighs = get_neighs.split(" ")
        graph[get_node] = temp_neighs
        
    else:
        graph[get_node] = []

print("The graph is: {}".format(graph))
starting_ = input("Enter starting node: ")

print("Following is the Depth-First Search")

dfs(visited, graph, starting_)