C - Linked List - Append
In a linked list, append operation adds an element to the list at the end. Fill in the missing lines of code to implement the append function so that the program prints the sum of elements as mentioned below.
Boundary Condition(s):
1 <= N <= 10000
Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains N integers separated by a space.
Example Input/Output 1:
Input:
4
67 34 10 93
Output:
204
Example Input/Output 2:
Input:
7
23 11 56 93 72 93 78
Output:
426
#include<stdio.h>
struct Node
{
    int data;
    struct Node *next;
};

struct Node *head = NULL;
struct Node *tail = NULL;
void append(int val){
    struct Node* newNode=(struct Node*)malloc(sizeof(struct Node*));
    newNode->data=val;
    newNode->next=NULL;
    if(head==NULL){
        head=newNode;
        tail=newNode;
        return;
    }
    tail->next=newNode;
    tail=newNode;
    return;
}
int main()
{
    int N, value;
    scanf("%d", &N);
    while(N--)
    {
        scanf("%d", &value);
        append(value);
    }
    struct Node *ptr = head;
    int sum = 0;
    while(ptr != NULL)
    {
        sum += ptr->data;
        ptr = ptr->next;
    }
    printf("%d", sum);
}
