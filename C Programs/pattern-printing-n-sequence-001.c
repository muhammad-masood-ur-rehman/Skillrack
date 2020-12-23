Pattern Printing N - Sequence 001
The program must accept an integer N and print the pattern as shown in the Example Input/Output. 
Input Format: The first line contains N.
 Output Format: N lines containing the pattern as shown in the Example Input/Output. 
Boundary Conditions: 2 <= N <= 100 
Example Input/Output 1:
 Input:
4 
Output:
1 2 3 4 
9 10 11 12 
13 14 15 16 
5 6 7 8 
Example Input/Output 2: 
Input: 
7 
Output: 
1 2 3 4 5 6 7 
15 16 17 18 19 20 
21 29 30 31 32 33 34 35 
43 44 45 46 47 48 49 
36 37 38 39 40 41 42 
22 23 24 25 26 27 28 
8 9 10 11 12 13 14
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n,c=1,i,j,k=0,m=0;
scanf("%d",&n);
int a[n][n];
for(i=0;i<n;i++)
{
    if(i%2==0)
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",c);
            c++;
        }
        printf("\n");
    }
    else
    {
        for(j=0;j<n;j++)
        {
            if(m==n)
            m=0;
            a[k][m]=c;
            c++;
            m++;
        }
        k++;
    }
}
for(i=k-1;i>=0;i--)
{
    for(j=0;j<m;j++)
        printf("%d ",a[i][j]);
    printf("\n");
}

}
import java.util.*;
public class Hello {

    public static void main(String[] args) {
  Scanner sc=new Scanner(System.in);
  int n=sc.nextInt();
  int m=1,i,j,o;
  o=n%2==0?n:n+1;
  for(i=0;i<n;i++)
  {
      for(j=m;j<m+n;j++)
          System.out.print(j+" ");
      System.out.println();
      if(i==(o/2)-1)
        m+=(n%2==0)?n:(-1*n);
      else if(i<(o/2)-1)
        m+=2*n;
      else
        m-=2*n;
  }
 }

}
