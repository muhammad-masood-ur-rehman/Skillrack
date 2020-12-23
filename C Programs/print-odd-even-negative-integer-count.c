Print Odd Even Negative Integer Count
Accept N integers and print the count of odd, even and negative integer count as the output.
Input Format:
The first line contains N.
The second line contains N integer values, separated by space.
Output Format:
The first line contains the count of odd, even and negative integer count separated by a space.
Boundary Conditions:
1 <= N <= 1000
Example Input/Output 1:
Input:
10
78 20 4 -12 96 93 15 60 -58 22
Output:
2 6 2
Example Input/Output 2:
Input:
20
-16 -32 87 79 -33 7 -8 87 63 25 84 39 -20 -12 84 98 8 28 22 74
Output:
7 7 6
n,neg,odd,eve,m=int(input()),0,0,0,[int(i) for i in input().split()]
for i in m:
    if i<0:
        neg+=1
    elif i%2==0 :
        eve+=1
    else:
        odd+=1
print("{0} {1} {2}".format(odd,eve,neg))  
#include<stdio.h>
int main()
{
int n,i,e=0,o=0,ne=0;
scanf("%d",&n);
int a[n];
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
if(a[i]<0) ne++;
else if(a[i]%2==0&&a[i]>=0) e++;
else o++;
}
    printf("%d %d %d",o,e,ne);

}
import java.util.*;
public class Hello {

    public static void main(String[] args) {
  Scanner sc=new Scanner(System.in);
  int n=sc.nextInt();
  int a,o=0,e=0,u=0;
  for(int i=1;i<=n;i++)
  {
   a=sc.nextInt();
   if(a<0)
   u++;
   else if(a&1==1)
   o++;
   else
   e++;
  }
     System.out.print(o+" "+e+" "+u+" ");
 }

}
