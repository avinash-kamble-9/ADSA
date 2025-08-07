import java.util.Scanner;

class Node {
    int data;
    Node left, right;

    public Node(int item) {
        data = item;
        left = right = null;
    }
}

class BSTt {
    Node root;

    BSTt() {
        root = null;
    }

    void insert(int key) {
        root = insertRec(root, key);
    }

    Node insertRec(Node root, int key) {
        if (root == null) {
            root = new Node(key);
            return root;
        }

        if (key < root.data)
            root.left = insertRec(root.left, key);
        else if (key > root.data)
            root.right = insertRec(root.right, key);

        return root;
    }

    void preorder() {
        preorderRec(root);
        System.out.println();
    }

    void preorderRec(Node root) {
        if (root != null) {
            System.out.print(root.data + " ");
            preorderRec(root.left);
            preorderRec(root.right);
        }
    }

    void inorder() {
        inorderRec(root);
        System.out.println();
    }

    void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.print(root.data + " ");
            inorderRec(root.right);
        }
    }

    void postorder() {
        postorderRec(root);
        System.out.println();
    }

    void postorderRec(Node root) {
        if (root != null) {
            postorderRec(root.left);
            postorderRec(root.right);
            System.out.print(root.data + " ");
        }
    }
}

public class BST {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BSTt tree = new BSTt();

        System.out.println("Enter number of nodes to insert:");
        int n = sc.nextInt();

        System.out.println("Enter " + n + " values to insert into the BST:");
        for (int i = 0; i < n; i++) {
            int val = sc.nextInt();
            tree.insert(val);
        }

        System.out.println("Preorder traversal:");
        tree.preorder();

        System.out.println("Inorder traversal:");
        tree.inorder();

        System.out.println("Postorder traversal:");
        tree.postorder();

        sc.close();
    }
}

