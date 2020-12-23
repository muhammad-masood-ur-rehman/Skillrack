Replace Max Digit - Two Integers
The program must accept two integers X and Y as the input. The program must replace all the occurrences of the maximum digit in X with the maximum digit in Y. Then the program must print the sum of X and Y as the output.
Boundary Condition(s):
10 <= X, Y <= 10^8
Input Format:
The first line contains X and Y separated by a space.
Output Format:
The first line contains an integer representing the sum of X and Y.
Example Input/Output 1:
Input:
1878 2020
Output:
3292
Explanation:
Here X = 1878 and Y = 2020.
After replacing all the occurrences of the maximum digit 8 in 1878 with the maximum digit 2 in 2020, the integer 1878 becomes 1272.
Here the sum of 1272 and 2020 is 3292.
Hence the output is 3292
Example Input/Output 2:
Input:
1111 144
Output:
4588
Example Input/Output 3:
Input:
189 1239
Output:
1428
Python:
a,b=input().split()
a=a.replace(max(a),max(b))
print(int(a)+int(b))
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
char ch1='0',ch='0',s[10],s1[10];
scanf("%s %s",s,s1);
for(int i=0;i<strlen(s1);i++)
{
    if(s1[i]>ch1)
    ch1=s1[i];
}
for(int i=0;i<strlen(s);i++)
{
    if(s[i]>ch)
    ch=s[i];
}
for(int i=0;i<strlen(s);i++)
{
    if(s[i]==ch)
    s[i]=ch1;
}
printf("%d",atoi(s)+atoi(s1));
}
C++:
#include <bits/stdc++.h>
 
using namespace std;

void find(char x[20], char y[20])
{
    int maxi1=0,maxi2=0;
    for(int i=0;i<strlen(y);i++)
    {
        if(maxi1<y[i]-'0')
            maxi1=y[i]-'0';
    }
    for(int i=0;i<strlen(x);i++)
    {
        if(maxi2<x[i]-'0')
            maxi2=x[i]-'0';
    }
    for(int i=0;i<strlen(x);i++)
    {
        if(x[i]-'0'==maxi2)
            x[i]=maxi1+'0';
    }
    cout<<atoi(x)+atoi(y);
}

int main(int argc, char** argv)
{
    char x[20],y[20];
    cin>>x>>y;
    find(x,y);
}
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Scanner q=new Scanner(System.in);
        int[] a=Integer.toString(q.nextInt()).chars().map(c->c-'0').toArray(),b=Integer.toString(q.nextInt()).chars().map(c->c-'0').toArray();
        int c=0,d=0,a1=0,b1=0;
        for(int i:a){
            c=Math.max(c,i);
        }
        for(int i:b){
            d=Math.max(d,i);
            b1=(b1*10)+i;
        }
        for(int i:a){
            if(i==c){
                i=d;
            }
            a1=(a1*10)+i;
        }
        System.out.print(a1+b1);
	}
}
