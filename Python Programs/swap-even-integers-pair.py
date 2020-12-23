Swap Even Integers Pair
The program must accept N integers as the input. The program swap every two even integers among the N integers. Then the program must print the N modified integers as the output. If the number of even integers is odd, the last even integer will remain the same as it has no pair to swap.
Boundary Condition(s):
2 <= N <= 1000
1 <= Each integer value <= 10^5
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains the N modified integers separated by a space.
Example Input/Output 1:
Input:
7
22 43 56 51 68 50 28
Output:
56 43 22 51 50 68 28
Explanation:
There are two even integer pairs in the given integers.
The first even integer pair is 22 and 56. After swapping, the integers become 56 43 22 51 68 50 28.
The second even integer pair is 68 and 50. After swapping, the integers become 56 43 22 51 50 68 28.
Hence the output is 56 43 22 51 50 68 28
Example Input/Output 2:
Input:
6
2 8 3 12 98 56
Output:
8 2 3 98 12 56
Max Execution Time Limit: 500 millisecs
Python:
n=int(input())
l=list(map(int,input().split()))
c=0
ind=0
for i in range(n):
    if l[i]%2==0:
        c+=1
        if(c==2):
            l[ind],l[i]=l[i],l[ind]
            c=0
        ind=i 
for i in range(n):
    print(l[i],end=" ")
num=int(input())
li=[int(x) for x in input().split()]
b=list(filter(lambda x:(x%2==0),li))
length1=len(b);foo=0
if length1%2:
    length1-=1 
for ele in range(0,length1,2):
    b[ele],b[ele+1]=b[ele+1],b[ele]
for ele in li:
    if ele%2:
        print(ele,end=" ")
    else:
        print(b[foo],end=" ")
        foo+=1
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    scanf("%d",&num);
    int arra[num];  
    for(int ele=0;ele<num;ele++){
		scanf("%d",&arra[ele]);
    }
    int cnt=0;
    int foo;
    for(int ele=0;ele<num;ele++){
        if(arra[ele]%2==0){
            cnt++;
            if(cnt==2){
                int t=arra[foo];
                arra[foo]=arra[ele];
                arra[ele]=t;
                cnt=0;
            }
            foo=ele;
        }
    }
    for(int ele=0;ele<num;ele++){
		printf("%d ",arra[ele]);
	}
}
#include <stdio.h>

int main()
{
    int ele,k=0,temp,num;
	int arr1[1000],arr2[1000];
    scanf("%d",&num);
    for(ele=0;ele<num;ele++)
    {
        scanf("%d",&arr1[ele]);
        if(arr1[ele]%2==0)
        arr2[k++]=ele;
    }
    if(k%2!=0)
    k-=1;
    for(ele=0;ele<k-1;ele+=2)
    {
        temp=arr1[arr2[ele]];
        arr1[arr2[ele]]=arr1[arr2[ele+1]];
        arr1[arr2[ele+1]]=temp;
    }
    for(ele=0;ele<num;ele++){
		printf("%d ",arr1[ele]);
    }
}
C++:
#include <bits/stdc++.h>
#include<iostream>
#include<cstring>
using namespace std;

int main()
{
int num,ele,count=0,s1[1000],s2[1000];
cin>>num;
for(ele=0;ele<num;ele++){
    cin>>s1[ele];
    if(s1[ele]%2==0)
    s2[count++]=ele;
}
if(count%2!=0)
count-=1;
for(ele=0;ele<count-1;ele+=2){
    int temp=s1[s2[ele]];
    s1[s2[ele]]=s1[s2[ele+1]];
    s1[s2[ele+1]]=temp;
}
for(ele=0;ele<num;ele++){
    cout<<s1[ele]<<" ";
}
}
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
    Scanner sc=new Scanner(System.in);
    int N=sc.nextInt();
    int arr[]=new int[N];
    int start=-1;
    for(int i=0;i<N;i++)
    {
        arr[i]=sc.nextInt();
        if(arr[i]%2==0)
        {
            if(start==-1)
            {
            start=i;
            }
            else
            {
            int temp=arr[start];
            arr[start]=arr[i];
            arr[i]=temp;
            start=-1;
            }
        }
    }
    for(int i=0;i<N;i++)
    {
        System.out.print(arr[i]+" ");
    }
	}
}
