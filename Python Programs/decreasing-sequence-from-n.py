Decreasing Sequence from N
Decreasing Sequence from N: Two integers N and D are passed as input. The program must print the decreasing sequence from N to 1 with common difference D.
Boundary Condition(s):
2 <= N <= 9999999
1 <= D <= 9999999
Input Format:
The first line contains N and D separated by space(s).
Output Format:
The first line contains integers separated by a space.
Example Input/Output 1:
Input:
20 3
Output:
17 14 11 8 5 2
Example Input/Output 2:
Input:
26 5
Output:
21 16 11 6 1
Python:
n,d=map(int,input().split())
lim=d
while(n-d>0):
    n=n-d
    print(n,end=" ")
Java:
import java.util.*;
public class Main
{
public static void main(String[] args)  
{
    Scanner sc = new Scanner( System.in);
	int n = sc.nextInt();
	int d = sc.nextInt();
	int lim=d;
	while(n-d>0){
	    n=n-d;
	    System.out.print(n+" ");
	}
} 
} 
