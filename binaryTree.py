"""
One way to count the number of nodes in a complete binary tree in faster than O(n) 
time is to use the property that the number of nodes in a complete binary tree can 
be computed from the height of the tree.
If the height of the tree is h, then the number of nodes in the tree is at least 2^h - 1. 
This is because each level of the tree has at least twice as many nodes as the previous level, 
except for the first level which has one node. So the total number of nodes is at least the sum 
of the number of nodes at each level, which is 1 + 2 + 4 + ... + 2^(h-1) = 2^h - 1.


    1
   / \
  2   3
 / \ / \
4  5 6  7

"""
# Binary Tree

class Node:
    
    
    def __init__(self, data): # Constructor
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data): # Insert Node
        self.data = data
        if self.left is None:
            return Node(data)
        else:
            return self.left.insert(data)
        
    def printTree(self): # Inorder traversal
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
            
    def height(self): # Height of the tree
        if self.left is None and self.right is None:
            return 0
        else:
            return 1 + max(self.left.height(), self.right.height())
        
    def countNodes(self): # Count the number of nodes
        if self.left is None and self.right is None:
            return 1
        else:
            return 1 + self.left.countNodes() + self.right.countNodes()
        


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(root.height())
print(root.countNodes())
print(root.printTree())
print(root.left.printTree())
