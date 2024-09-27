class Node:    
    def __init__(self,data):
        self.data = data
        self.children = []


# ============== tree 1 =============
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

tree1 = root
# ============== tree 1 =============