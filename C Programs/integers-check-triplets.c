Integers - Check Triplets
The program must accept N integers as the input. The program must print Yes if there is at least one triplet (a, b, c) in the given N integers where a2 + b2 = c2. Else the program must print No as the output.
Example Input/Output 1:
Input:
7
5 1 3 6 7 2 4
Output:
Yes
Explanation:
Here the triplet is (3, 4, 5) where 32 + 42 = 52 (9 + 16 = 25).
Hence the output is Yes
Example Input/Output 2:
Input:
8
93 20 76 42 100 12 99 79
Output:
No
Python:
from itertools import combinations
def perfect(i):
    if i[0]**2+i[1]**2==i[2]**2:
        return 1
    elif i[1]**2+i[2]**2==i[0]**2:
        return 1
    elif i[0]**2+i[2]**2==i[1]**2:
        return 1
    else:
        return 0
n=int(input())
l=list(map(int,input().split()))[:n];c=0
comb=combinations(l,3)
for i in list(comb):
    if perfect(i):
        c+=1
        break
if c!=0:print("Yes")
else:print("No")
a=int(input());l=list(map(int,input().split()))
def triplet(l):
    l=[i*i for i in l]
    l.sort()
    for i in range(len(l)-1):
        for j in range(1,len(l)):
            if l[i]+l[j] in l:return 'Yes'
    return 'No';
print(triplet(l))
from itertools import combinations
num=int(input())
b=sorted(map(int,input().split()));c=0 
for ele in list(combinations(b,3)):
    if (ele[0]**2)+(ele[1]**2)==(ele[2]**2):
        c=c+1 
if c>0:
    print("Yes")
else:
    print("No")
n=int(input());x=[];m=0
l=list(map(int,input().split()))
for i in range(n):x.append(l[i]*l[i]) 
for i in range(n-1):
    for j in range(i+1,n):
        if l[i]*l[i]+l[j]*l[j] in x:
           print("Yes");m=1;quit()
if m==0:print('No')
C:
#include<stdio.h>
#include <stdlib.h>
int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;++i)scanf("%d",&arr[i]); 
    for(int i=0;i<n-2;++i){
        for(int j=i+1;j<n-1;++j){
            for(int k=j+1;k<n;++k){
                int a=arr[i]*arr[i];
                int b=arr[j]*arr[j];
                int c=arr[k]*arr[k];             
                if((a+b) == c || (a+c) ==b || (b+c) ==a){
                    printf("Yes");
                    return;
                }
            }
        }
    }
    printf("No");
    return;
}
#include<stdio.h>
#include <stdlib.h>
int main()
{
    int size,arr[1001],flag=0;
    scanf("%d",&size);
    for(int ind1=0;ind1<size;ind1++){
        scanf("%d ",&arr[ind1]);
    }
    for(int ind1=0;ind1<size;ind1++){
        for(int ind2=ind1+1;ind2<size;ind2++){
            for(int ind3=ind2+1;ind3<size;ind3++){
                int p=(arr[ind1]*arr[ind1]);
                int q=(arr[ind2]*arr[ind2]);
                int r=(arr[ind3]*arr[ind3]);
                if(p+q==r || p+r==q || q+r==p)
                flag=1;
            }
        }
    }
    if(flag==1)
     printf("Yes");
    else
     printf("No");
}
#include<stdio.h>
#include <stdlib.h>
#define check(a,b,c) (a*a+b*b==c*c)?1:0
int main()
{
int num,i,j,k,t,input[101];
scanf("%d",&num);
for(i=0;i<num;i++)
scanf("%d",&input[i]);
for(i=0;i<num-1;i++)
for(j=i+1;j<num;j++)
if(input[i]>input[j])
{
    t=input[i];
    input[i]=input[j];
    input[j]=t;
}
for(i=0;i<num-2;i++)
for(j=i+1;j<num-1;j++)
for(k=j+1;k<num;k++)
{      
    if(check(input[i],input[j],input[k]))
    {
        printf("Yes");
        return 0;
    }
}
printf("No");
}
