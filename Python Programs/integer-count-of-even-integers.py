Integer - Count of Even Integers
The program must accept an integer N as the input. The program must print the number of even integers that can be formed from the digits of N without changing the order of their occurrences.
Note: There are no leading zeroes in the even integers.
Boundary Condition(s):
1 <= N <= 10^8
Input Format:
The first line contains N.
Output Format:
The first line contains the number of even integers that can be formed from the digits of N.
Example Input/Output 1:
Input:
5234
Output:
6
Explanation:
All possible even integers that can be formed from the digits of 5234 are given below.
52
5234
2
234
34
4
The number of possible even integers is 6. So 6 is printed as the output.
Example Input/Output 2:
Input:
20406
Output:
9
Explanation:
All possible even integers that can be formed from the digits of 20406 are given below.
2
20
204
2040
20406
4
40
406
6
The number of possible even integers is 9. So 9 is printed as the output.
Example Input/Output 3:
Input:
2424
Output:
10
Python:
strin=input().strip()
l=len(strin)-1
count=0
for ele in range(l,-1,-1):
    if (ord(strin[ele])-ord('0'))%2:
        continue
    for foo in range(ele,-1,-1):
        if strin[foo]!='0':
            count+=1
print(count)
strin=input().strip()
k=[]
for ele in range(len(strin)):
    if strin[ele]=='0':
	    continue
    for foo in range(ele,len(strin)):
        if int(strin[ele:foo+1])%2==0:
            k.append(0)
print(len(k))
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char strin[10];
    scanf("%strin",strin);
    int l=strlen(strin);
    
    int count=0;
    
    for(int ele=l-1;ele>=0;ele++){
        if((strin[ele]-'0')%2)continue;
        for(int foo=ele;foo>=0;foo--){
            if(strin[foo]!='0')count++;
        }
    }
    printf("%d",count);
}
#include <stdio.h>
#include <string.h>

int main()
{
    char strin[1001];
    scanf("%s",strin);
    int length=strlen(strin),count=0;
    for(int ele=0;ele<length-1;ele++){
        int temp=strin[ele]-'0';
        if(temp!=0){
            for(int foo=ele+1;foo<length;foo++){
                int index=strin[foo]-'0';
                if(index%2==0)
                count++;
            }
        }
        if(temp%2==0 && temp!=0)
        count++;
    }
    if(strin[length-1]%2==0 && strin[length-1]!='0'){
        count++;
    }
    printf("%temp",count);
}
Java:
import java.util.*;
public class Hello
{
public static void main(String[] args) {
   Scanner sc=new Scanner(System.in);
   String strin=sc.nextLine();
   char ch;
   int ele,temp,count=0;
   for(ele=strin.length()-1;ele>=0;ele--)
   {
       ch=strin.charAt(ele);
       if(ch%2==0)
       {
           temp=ele;
           while(temp>=0)
           {
               if(strin.charAt(temp)!='0')
               count++;
               temp--;
           }
       }
   }
System.out.println(count);
}
}
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String strin=sc.nextLine();
		int count=0,temp;
		for(int ele=0;ele<strin.length();ele++){
		    if(strin.charAt(ele)=='0') continue;
		    for(int foo=ele;foo<strin.length();foo++){
                String ch=strin.substring(ele,foo+1);
		        if(ch.length()>0){
		        temp=Integer.parseInt(ch);
		        if(temp%2==0) count++;} 
		    }
		}
		System.out.println(count);
	}
}
C++:
