visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0) 
        print (m, end = " ") 

    for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)


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

print("Following is the Breadth-First Search")

bfs(visited, graph, starting_)