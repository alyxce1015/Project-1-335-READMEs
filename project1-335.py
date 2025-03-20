# ALgorithm 1 Wildlife Monitoring system 
# Alyx Cui Edio & Alexie Gonzalez 


def isCycle(n, coord):
    # initialize set of our graph
    graph = {}
    
    # loop with 2 iterators in coord to check the pairs
    for x, y in coord:

        # check if pair is in graph set
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []

        # append these values to graph
        graph[x].append(y)
        graph[y].append(x)  # Since it's an undirected graph

    # initialize visited variable as set since we will have tuples being passed
    visited = set()

    # create DFS function to track paths
    def dfs(node, parent):
        # add start node to visited
        visited.add(node)

        # interate through the neighbors in graph from the current node
        for neighbor in graph[node]:
            if neighbor not in visited:  # If neighbor is unvisited, recurse to next
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:  # If neighbor is visited and not parent, cycle found
                return True
        
        return False # default return false

    # Iterate through all nodes in case of unvisited
    for node in graph:
        if node not in visited:
            if dfs(node, -1):  # Start DFS from an unvisited node
                print("Loop detected") # print if loop
                return # end

    print("No loop detected") # default print statement


# test cases
# cases must be of value that are tuples in form (n, [])
# n = number of nodes
# [] = coordinate pairs to traverse through
test1 = (7, [(0, 1), (1, 2), (2, 3), (3, 2), (5, 2), (4, 6)])
test2 = (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)])

# Call the function
isCycle(*test1)  # Expected Output: "Loop detected"
isCycle(*test2)  # Expected Output: "No loop detected"
