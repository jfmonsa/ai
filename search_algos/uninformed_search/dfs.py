# DFS implementation for uninformed search
from ..tree import Node, tree1


def dfs_preorder(root:Node, target:str):
    stack = [root]
    created_nodes = [root.data]
    expanded_nodes = []

    while stack:
        current = stack.pop()
        expanded_nodes.append(current.data)

        if current.data == target:
            return created_nodes, expanded_nodes, True

        stack.extend(current.children[::-1])
        created_nodes.extend([children.data for children in current.children])

    return created_nodes, expanded_nodes, False


if __name__ == "__main__":
    # search
    created_nodes, expanded_nodes,  was_found = dfs_preorder(tree1, "G")
    print("Created nodes: ", created_nodes)
    print("Expanded nodes: ", expanded_nodes)
    print("Was found?: ", was_found)
