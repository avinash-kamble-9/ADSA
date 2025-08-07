import java.util.*;

class Node {
    int data;
    Node left, right;

    Node(int data) {
        this.data = data;
        left = right = null;
    }
}

public class BinaryTreeTraversal {
    Node root;

    BinaryTreeTraversal() {
        root = null;
    }

    // Inorder traversal: Left -> Root -> Right
    void inorder(Node node) {
        if (node == null) return;

        inorder(node.left);
        System.out.print(node.data + " ");
        inorder(node.right);
    }

    // Preorder traversal: Root -> Left -> Right
    void preorder(Node node) {
        if (node == null) return;

        System.out.print(node.data + " ");
        preorder(node.left);
        preorder(node.right);
    }

    // Postorder traversal: Left -> Right -> Root
    void postorder(Node node) {
        if (node == null) return;

        postorder(node.left);
        postorder(node.right);
        System.out.print(node.data + " ");
    }

    // Build tree from user input (level order), -1 means no child
    void buildTreeFromInput() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter root node value:");
        int rootVal = sc.nextInt();
        if (rootVal == -1) {
            root = null;
            return;
        }

        root = new Node(rootVal);
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            System.out.println("Enter left child of " + current.data + " (-1 for no child):");
            int leftVal = sc.nextInt();
            if (leftVal != -1) {
                current.left = new Node(leftVal);
                queue.add(current.left);
            }

            System.out.println("Enter right child of " + current.data + " (-1 for no child):");
            int rightVal = sc.nextInt();
            if (rightVal != -1) {
                current.right = new Node(rightVal);
                queue.add(current.right);
            }
        }
    }

    public static void main(String[] args) {
        BinaryTreeTraversal tree = new BinaryTreeTraversal();

        tree.buildTreeFromInput();

        System.out.print("Inorder traversal: ");
        tree.inorder(tree.root);
        System.out.println();

        System.out.print("Preorder traversal: ");
        tree.preorder(tree.root);
        System.out.println();

        System.out.print("Postorder traversal: ");
        tree.postorder(tree.root);
        System.out.println();
    }
}


