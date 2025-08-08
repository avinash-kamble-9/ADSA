# Node class for BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert function
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Inorder Traversal (Left → Root → Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Preorder Traversal (Root → Left → Right)
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder Traversal (Left → Right → Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

# --- Main Program ---
if __name__ == "__main__":
    n = int(input("Enter number of nodes: "))
    root = None

    print("Enter the node values:")
    for _ in range(n):
        value = int(input())
        root = insert(root, value)

    print("\nInorder Traversal: ")
    inorder(root)

    print("\nPreorder Traversal: ")
    preorder(root)

    print("\nPostorder Traversal: ")
    postorder(root)


# Enter number of nodes: 7
# Enter the node values:
# 50
# 30
# 20
# 40
# 70
# 60
# 80

# Inorder Traversal: 
# 20 30 40 50 60 70 80
# Preorder Traversal: 
# 50 30 20 40 70 60 80
# Postorder Traversal: 
# 20 40 30 60 80 70 50

