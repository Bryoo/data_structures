class Node:
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

# traverse root, left subtree, then right subtree
    def pre_order(self):
        print(self.val, end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

# traverse left subtree, root, then right subtree
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.val, end=" ")
        if self.right:
            self.right.in_order()

# traverse left subtree, right subtree then root
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.val, end=" ")


root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
root.right.left = Node(6)
root.right.right = Node(7)

print("Preorder traversal:")
root.pre_order()
 
print("\nInorder traversal:")
root.in_order()

print("\nPostorder traversal:")
root.post_order()
