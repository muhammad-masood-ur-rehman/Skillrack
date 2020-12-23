Search Substring & Print Words
The program must accept a space-separated string S and N string values as the input. For each string X among the N string values, the program must print the words in S having the substring X at least once. If there is no such word in the string S, the program must print -1 as the output.
Boundary Condition(s):
1 <= Length of S <= 1000
1 <= N <= 50
1 <= Length of each string among the N string values <= 100
Input Format:
The first line contains S.
The second line contains N.
The next N lines, each contains a string value.
Output Format:
The first N lines, each contains a string or -1 as per the given conditions.
Example Input/Output 1:
Input:
learning makes a good man better and a bad man worse
4
k
ea
ma
a
Output:
makes
learning
makes man man
learning makes a man and a bad man
Explanation:
The 1st string is k, the word that contains the substring k in the string S is makes.
The 2nd string is ea, the word that contains the substring ea in the string S is learning.
The 3rd string is ma, the words that contain the substring ma in the string S are makes, man and man.
The 4th string is a, the words that contain the substring a in the string S are learning, makes, a, man, and, a, bad and man.
Example Input/Output 2:
Input:
programming is an explanatory activity
5
o
al
i
an
ing
Output:
programming explanatory
-1
programming is activity
an explanatory
programming
Example Input/Output 3:
Input:
enter green rocking cooking clean terminate backward eat
6
e
king
en
g
ter
ooo
Output:
enter green clean terminate eat
rocking cooking
enter green
green rocking cooking
enter terminate
-1
Python:
li=list(map(str,input().split()))
n=int(input())
li2=[input().strip() for ele in range(n)]
for ele in li2:
    c=0
    for foo in li:
        if ele in foo:
            print(foo,end=" ")
            c=1
    if(c==0):
		print(-1,end=" ")
    print()
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
char arr[100][1000];
int bar=0,num;
while(scanf("%arr",arr[bar])==1)
{
    if(isdigit(arr[bar][0]))
    {
        num=atoi(arr[bar]);
        break;
    }
	bar++;
}
char a[1000];
for(int ele=0;ele<num;ele++)
{
    scanf("%arr\n",a);
    int f=0;
    for(int foo=0;foo<bar;foo++)
    {
        char *p=strstr(arr[foo],a);
        if(p!=NULL)
        {
            f=1;
            printf("%arr ",arr[foo]);
        }
    }
    if(f==0)
    printf("-1\n");
    else
    printf("\n");
    
}
}
Java:
import java.util.*;
public class Hello 
{
    public static void main(String[] args) 
    {
		Scanner sc=new Scanner(System.in);
		String[] w=sc.nextLine().split(" ");
		int num=sc.nextInt(),ctr=0;
		for(int ele=1;ele<=num;ele++)
		{
		    String X=sc.next();
		    ctr=0;
		    for(int ctr=0;ctr<w.length;ctr++)
		    {
		        if(w[ctr].contains(X))
		        {
		            System.out.print(w[ctr]+" ");
		            ctr=1;
		        }
		    }
		    if(ctr==0)
		    System.out.println("-1");
		    else
		    System.out.println();
		}
	}
}
