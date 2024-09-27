# Implementation of BFS algo
from ..tree import tree1, Node

def bfs(root:Node, target:str):    
    queue = [root]
    # lists aren't needed actually only for visualization
    created_nodes = [root.data]
    expanded_nodes = []

    # while there are nodes in the queue
    while queue:
        current = queue.pop(0)

        # current node is not in expanded
        expanded_nodes.append(current.data)

        # current node is goal?
        if current.data == target:
            return created_nodes, expanded_nodes, True
        
        # append its children to created nodes
        created_nodes.extend([children.data for children in current.children])
        queue.extend(current.children)

    return created_nodes, expanded_nodes, False


if __name__ == "__main__":
    # search
    created_nodes, expanded_nodes,  was_found = bfs(tree1, "G")
    print("Created nodes: ", created_nodes)
    print("Expanded nodes: ", expanded_nodes)
    print("Was found?: ", was_found)
