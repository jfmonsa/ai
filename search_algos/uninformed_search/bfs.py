# Implementation of BFS algo

# importing
from ..tree import Node

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

def dfs_preorder(root:Node, target:str):
    stack = [root]
    created_nodes = [root.data]
    expanded_nodes = []

    while stack:
        current = stack.pop()
        expanded_nodes.append(current.data)

        if current.data == target:
            return True

        stack.extend(current.children[::-1])

def main():
    
    #example 1:
    #
    #        H
    #    /    |    \
    #   A     B     C
    #  / \    |    /  \
    # D  E    F    G*  J
    #/ \    
    #K  L*

    #Note: start marked are goals
    

    # create the tree
    root = Node("H")
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")
    j = Node("J")
    k = Node("K")
    l = Node("L")

    # connect the nodes
    root.children = [a,b,c]
    a.children = [d,e]
    b.children = [f]
    c.children = [g,j]
    d.children = [k,l]

    # search
    created_nodes, expanded_nodes,  was_found = bfs(root, "G")
    print("Created nodes: ", created_nodes)
    print("Expanded nodes: ", expanded_nodes)
    print("Was found?: ", was_found)


if __name__ == "__main__":
    main()
