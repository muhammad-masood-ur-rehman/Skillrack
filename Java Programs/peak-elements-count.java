Peak Elements Count
Peak Elements Count: N integers are passed as input. The program must print the count of peak elements among the N integers. An element is a peak element if it is greater than it's neighbours (the elements to the left and right).
The elements present in the extreme left and right can never be peak elements.
Input Format:
The first line contains N.
The second line contains N integer values separated by a space.
Output Format:
The first line contains the count of peak elements.
Boundary Conditions:
2 <= N <= 1000
Example Input/Output 1:
Input:
5
1 2 3 1 3
Output:
1
Example Input/Output 2:
Input:
5
1 2 3 4 5
Output:
0
n,c=int(input()),0
v=[int(i) for i in input().split()]
for i in range(1,n-1):
    if v[i]>v[i-1] and v[i]>v[i+1]:
        c+=1;
print(c)        
import java.util.*;
public class Hello {

    public static void main(String[] args) {
        //Your Code Here
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int arr[]=new int[n];
for(int i=0;i<n;i++)
arr[i]=sc.nextInt();
int c=0;
for(int i=1;i<n-1;i++)
{
    if(arr[i]>arr[i-1] && arr[i]>arr[i+1])
    c++;
}
System.out.print(c);
    }
}
