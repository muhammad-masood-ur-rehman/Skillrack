BST - Leaf Node Count
BST - Leaf Node Count: An array of N positive integers is passed as input. The program must form a binary search tree with these numbers. The first number (out of the N numbers passed as input) is the root node of the binary search tree. The program must print the count of leaf nodes present in the binary search tree.
Note: A node is a leaf node if it does not have a left or right child.
Input Format:
The first line contains N numbers, each separated by a space.
Output Format:
The first line contains the count of leaf nodes.
Boundary Conditions:
1 <= N <= 9999
Example Input/Output 1:
Input:
1 2 5 3 6 4
Output:
2
Explanation:
The leaf nodes are the nodes with the values 4 and 6.
Example Input/Output 2:
Input:
9 11 4 7 2 6 5
Output:
3
import java.util.*;
public class Hello {
    static int count=0;
    Scanner scan;
    class Node{
        Node left,right;
        int val;
        Node(int val){
            this.val=val;
            left=null;right=null;
        }
    }
    public Node insert(Node node,int val){
        if(node==null)return new Node(val);
        if(val< node.val)node.left=insert(node.left,val);
        else node.right=insert(node.right,val);
        return node;
    }
    public static int getCountOfLeaves(Node node){
        if(node==null)return 0;
        if(node.left==null && node.right ==null){
            return 1;
        }
        return getCountOfLeaves(node.left)+getCountOfLeaves(node.right);
    }
    public static void main(String[] args) {
        Node head=new Hello().fun(null);
        int var=getCountOfLeaves(head);
        System.out.print(var);
    }
    public Node fun(Node head)
    {
        scan=new Scanner(System.in);

        while(scan.hasNext()){
            head=insert(head,scan.nextInt());
        }
        return head;
    }
}
