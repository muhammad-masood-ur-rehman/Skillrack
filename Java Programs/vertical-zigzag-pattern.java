Vertical ZigZag Pattern
Fill in the missing lines of code to print the pattern as defined in the Example Input/Output section.
Input Format:
The first line contains N.
Output Format:
N lines contain the number pattern.
Boundary Conditions:
1 <= N <= 50
Example Input/Output 1:
Input:
5
Output:
1
2 9  
3 8 10
4 7 11 14
5 6 12 13 15
Example Input/Output 2:
Input:
4
Output:
1
2 7
3 6 8
4 5 9 10
Python:
n=int(input())
a=1;k=0;l=[];s=[];l1=[]
t=sum(range(1,n+1))
l=list(range(1,t+1))
for i in range(n):
    s=[]
    if (i%2==0):
        for j in range(n):
            if(i<=j):
                s.append(l[k])
                k+=1
            else:
                s.append(0)
        l1.append(s)
    else:
        for j in range(n-1,-1,-1):
            if(i<=j):
                s.append(l[k])
                k+=1
            else:
                s.append(0)
        l1.append(s[::-1])
for i in range(n):
    for j in range(n):
        if(j<=i):
            print(l1[j][i],end=' ')
    print()
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
                    
                    Scanner sc = new Scanner(System.in);
                    int n = sc.nextInt();
                    
                    int[][] matrix = new int[n][n];
                    int counter = 1;
                    int i=0,j=0;
                    for(i=0;i<n;i++)
                    {
                        if(j==n)
                        {
                           for(j=n-1;j>i-1;j--,counter++)
                           {
                               matrix[j][i]=counter;
                           }
                        }
                        else
                        {
                            for(j=i;j<n;j++,counter++)
                            {
                            matrix[j][i]=counter;
                            }
                        }
                    }
        
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(matrix[i][j]!=0)
                    System.out.print(matrix[i][j]+" ");
            }
            System.out.println();
        }
         
                }
}
