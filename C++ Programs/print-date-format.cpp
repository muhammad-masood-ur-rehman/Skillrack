Print Date Format
The program must accept a valid date D in any format as the input. The day DD, the month MM or MMM and the year YYYY in the date D can be in any order. The program must print the format of the given date D as the output. If more than one formats are applicable for the given date D, the program must print -1 as the output.
Note: MMM will be like Jan, Feb, Mar,.... till Dec.
Boundary Condition(s):
1 <= DD <= 31
1 <= MM <= 12
1000 <= YYYY <= 2020
Input Format:
The first line contains D.
Output Format:
The first line contains the date format of D.
Example Input/Output 1:
Input:
02-Nov-2012
Output:
DD-MMM-YYYY
Explanation:
Here the given date is 02-Nov-2012, which is in the format DD-MMM-YYYY.
Hence the output is DD-MMM-YYYY
Example Input/Output 2:
Input:
1997-27-02
Output:
YYYY-DD-MM
Example Input/Output 3:
Input:
04-06-2017
Output:
-1
Explanation:
Here two formats are applicable, they are DD-MM-YYYY and MM-DD-YYYY.
Hence the output is -1
Python:
li=list(input().split("-")) 
fi=list(filter(lambda x:len(x)==2,li)) 
c=1
ma=0
k=0
res=[]
if(len(fi)==2 and int(fi[1])<13 and int(fi[0])<13):
    print(-1)
    k=1
else:
    if(len(fi)==2):
        ma=max(fi)
    

    for i in li: 
        if(len(i)==4):
            res.append("YYYY")
        elif(len(i)==3):
            res.append("MMM")
            
        elif(len(i)==2 and int(i)<=int(ma) and int(i)<13):
            res.append("MM")
        else:
            res.append("DD") 
            c=0
if(k==0):  
    print("-".join(res))
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
		Scanner sc= new Scanner(System.in);
		String s[]=sc.next().split("-");
		List<String> str=new ArrayList<>();
		int f=0;
		for(int i=0;i<s.length;i++)
		{
		    if(s[i].length()==4)
		    str.add("YYYY");
		    else if(s[i].length()==3)
		    {
		        if(str.contains("MM"))
		        Collections.replaceAll(str,"MM","DD");
		        str.add("MMM");
		    }
		    else
		    {
		        if(Integer.parseInt(s[i])>12)
		        str.add("DD");
		        else
		        {
		            if(str.contains("MM"))
		            {
		                f=1;
		                break;
		            }
		            else if(!str.contains("MMM"))
		            str.add("MM");
		            else
		            str.add("DD");
		        }
		    }
		}
		if(f==1)
		System.out.print("-1");
		else
		{
		    for(int i=0;i<str.size();i++)
		    {
		        System.out.print(str.get(i));
		        if(i!=(str.size()-1))
		        System.out.print("-");
		    }
		    
		}
	}
}
C++:
#include <bits/stdc++.h>
#include<cstdlib>
#include<cstdio>
using namespace std;

int f=0;

string check(char a[10])
{
    if(isalpha(a[0]))
    {
        f=1;
        return "MMM";
    }
    else if(atoi(a)>12 && atoi(a)<=31 || (f==1 && atoi(a)<=12))
        return "DD";
    else if(atoi(a)>=1000)
        return "YYYY";
    else if(atoi(a)<=12)
        return "MM";
}

void find(char a[10], char b[10], char c[10])
{
    if(check(a)==check(b) || check(b)==check(c) || check(a)==check(c))
        cout<<"-1";
    else
        cout<<check(a)<<"-"<<check(b)<<"-"<<check(c);
}

int main(int argc, char** argv)
{
    char a[10],b[10],c[10];
    scanf("%[^-]-%[^-]-%s",a,b,c);
    find(a,b,c);
}
C:
#include<stdio.h>
#include <stdlib.h>
int q=0,c=0;
void date(char g[],int l)
{
    if(l==4)
    printf("YYYY");
    if(l==3)
    {
        printf("MMM");
    }
    if(l==2)
    {
        if(q==1)
        printf("DD");
        else
        {
            if(atoi(g)>=12)
            printf("DD");
            else
            printf("MM");
        }
    }
}

int main()
{
    char d[3][5];
    scanf("%[^-]-%[^-]-%s",&d[0],&d[1],&d[2]);
    int l[3];
    l[0]=strlen(d[0]);
    l[1]=strlen(d[1]);
    l[2]=strlen(d[2]);
    for(int i=0;i<3;i++)
    {
        if(l[i]==3)
        q=1;
        if(l[i]==2)
        {
            if(atoi(d[i])<=12)
            c++;
        }
    }
    if(c==2)
    {
        printf("-1");
        return 1;
    }
    else
    {
        date(d[0],l[0]);
        printf("-");
        date(d[1],l[1]);
        printf("-");
        date(d[2],l[2]);
    }
}
