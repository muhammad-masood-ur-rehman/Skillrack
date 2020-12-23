Sum of ASCII Values
The program must accept a string S as the input. The program must print the sum of the ASCII values of all the characters in the string S.
Input : abcd
Output : 394
Explanation:
The ASCII value of a is 97.
The ASCII value of b is 98.
The ASCII value of c is 99.
The ASCII value of d is 100.
The sum of those ASCII values is 394.
Hence the output is 394
Here are the various methods and logic.
Java
//Java logic by @ Agent Thor
import java.io.*;
import java.util.*;
public class Main
{
	public static void main(String[] args) {
       Scanner S=new Scanner(System.in);
       String Str=S.nextLine();
       int i=0,sum=0,j;
      for(i=0;i<Str.length();i++)
       {
           j=Str.charAt(i);
           sum=sum+j;
           
       }
       System.out.print(sum);
	}
}
C
//C logic by @ Agent Marvel
int main()
{
char string[101];
scanf("%s",string);
int a=strlen(string);
int sum=0;
for(int i=o;i<a;i++)
{
sum=sum+(int)(string[i]));
}
printf("%d",sum);
}
//C logic by @ Agent Thor
#include<stdio.h>
#include <stdlib.h>
int main()
{
char s[1000];
int i,j,sum=0;
scanf("%s",s);
for(i=0;i<strlen(s);i++)
{
    j=s[i];
    sum=sum+j;
}
printf("%d",sum);
}
//C logic by @ Agent Nat
#include<stdio.h>
#include <stdlib.h>
int main()
{
int index,length,count=0;
char string[100];
scanf("%s",string);
length=strlen(string);
for(index=0;index<length;index++)
{
   count=count+string[index];
}
printf("%d",count);
}
Python
#Python logic by @ Agent Stark
num=input()
add=0
for i in num:
 	add+=ord(i)
print(add)
#Python logic by @ Agent Parker 
n=input() 
Sum=[] 
for i in n:
      Sum.append(ord(i))  
print(sum(Sum))
#Python logic by @ Agent Cherry
print(sum([ord(i) for i in input().strip()]))
C++
//C++ logic by @ Agent Wanda
#include<iostream>
using namespace std
int main()
{
char s[101];
std::cin>>s;
int i,l;
for(i=0;s[i]!='\0';i++)
{
int c=int(s[i]);
l+=c;
}
std::cout<<l;
}
