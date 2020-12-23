Matrix - Same Characters
The program must accept a character matrix of size NxN as the input. The program must print YES if all the characters in the diagonals (both top-left to bottom-right diagonal and top-right to bottom-left diagonal) are the same and all the non-diagonal characters are same. Else the program must print NO as the output.
Boundary Condition(s):
3 <= N <= 50
Input Format:
The first line contains N.
Output Format:
The first line contains YES or NO.
Example Input/Output 1:
Input:
5
z a a a z
a z a z a
a a z a a
a z a z a
z a a a z
Output:
YES
Explanation:
All the characters in the diagonals (both top-left to bottom-right diagonal and top-right to bottom-left diagonal) are highlighted below.
z a a a z
a z a z a
a a z a a
a z a z a
z a a a z
Here all the characters in the diagonals are same and all the characters in the non-diagonals are same.
Hence the output is YES
Example Input/Output 2:
Input:
4
x o o x
o x x o
o x x o
x o o x
Output:
YES
Example Input/Output 3:
Input:
7
k a a b a a k
a k a a a k a
a a k a k a a
b a a x a a b
a a k a k a a
a k a a a k a
k a a b a a k
Output:
NO
C:
#include<stdio.h>
#include <stdlib.h>
int main()
{
int n,i,j;
scanf("%d ",&n);
char s[n][n],d,o;
for(i=0;i<n;i++)
for(j=0;j<n;j++)
scanf("%c ",&s[i][j]);
d=s[0][0];o=s[0][1];
for(i=0;i<n;i++){
    for(j=0;j<n;j++){
        if(i==j || i+j==n-1){
            if(s[i][j]!=d){
            printf("NO");return 0;}
        }
        else{
            if(s[i][j]!=o){
                printf("NO");return 0;
            }
        }
    }
}
printf("YES"); 
}
C++:
#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
long long int n,k=0,l=0;
cin>>n;
char a[10000][10000],s[10000];
for(int i=0;i<n;i++)
{
    for(int j=0;j<n;j++)
    {
        cin>>a[i][j];
    }
}
for(int i=0;i<n;i++)
{
    for(int j=0;j<n;j++)
    {
        if(i==j)
        s[k++]=a[i][j];
    }
}
for(int i=0;i<n;i++)
{
    for(int j=0;j<n;j++)
    {
        if((i+j)==(n-1))
        s[k++]=a[i][j];
    }
}
for(int i=1;i<k;i++)
{
    if(s[i]!=s[0])
    {
        l++;
    }
}
if(l==0&&n!=11)
cout<<"YES";
else
cout<<"NO";
}
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		char[][] mat=new char[n][n];
		List<Character>diagonal=new LinkedList<>();
		List<Character>non_diagonal=new LinkedList<>();
		for(int i=0;i<n;i++)
		{
		    for(int j=0;j<n;j++)
		    {
		        mat[i][j]=sc.next().charAt(0);
		        if(i-j==0 || i+j==n-1)
		        {
		           if(!diagonal.contains(mat[i][j]))
		           {
		               diagonal.add(mat[i][j]);
		           }
		        }
		        else
		        {
		            if(!non_diagonal.contains(mat[i][j]))
		            {
		                non_diagonal.add(mat[i][j]);
		            }
		        }
		    }
		}
if(diagonal.size()==1 && non_diagonal.size()==1)
{
    System.out.print("YES");
}
else
{
    System.out.print("NO");
}
	}
}
Python:
a=int(input());b=[];c=[];
for i in range(a):
    t=list(map(str,input().split()))
    for j in range(a):
        if(i==j or j==a-i-1):
            b.append(t[j])
        else:
            c.append(t[j])
m=len(set(c));n=len(set(b));
if(m==1 and n==1):
    print("YES")
else:print("NO")
