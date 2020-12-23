Remaining Balloon Numbers
Remaining Balloon Numbers: There are N filled balloons each painted with a random number B(i) where i is from 1 to N and the balloons are tied up to a rope in a straight line. M kids who play football arrive and they decide to burst the balloons with the numbers divisible by their jersey numbers J(a) where a is from 1 to M. The program must print the numbers on the balloons remaining after all M kids burst the balloons in the order of their occurrence. If none of the balloons are remaining then the program must print -1.
Input Format:
The first line contains N and M separated by a space.
The second line contains N positive integers which denote the numbers on the balloons separated by a space.
The third line contains M positive integers which denote the numbers on the jerseys separated by a space.
Output Format:
The first line contains the numbers on the remaining balloons separated by a space (or -1 if no balloons remain)
Boundary Conditions:
1 <= N <= 9999
1 <= M <= 20
Example Input/Output 1:
Input:
11 3
38 40 11 46 44 48 35 14 39 44 23
2 3 11
Output:
35 23
Explanation:
The 1st kid bursts balloons with numbers which are divisible by 2. So the balloons remaining are 11 35 39 23
The 2nd kid bursts balloons with numbers which are divisible by 3. So the balloons remaining are 11 35 23.
The 3rd kid bursts balloons with numbers which are divisible by 11. So the balloons remaining are 35 23.
n,m=input().split()
l,=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=[]
for i in range(len(l1)):
    for j in range(len(l)):
        if l[j]%l1[i]==0:
            l2.append(l[j])
l3=[x for x in l if x not in l2]
if len(l3)>0:
    print(*l3)
else:
    print("-1")
#include<stdio.h>
#include <stdlib.h>
int main()
{
int n,m,i,j,k=0,f=0,x=0;
scanf("%d%d",&n,&m);
int a[n],b[m],c[9999];
for(i=0;i<n;i++)
    scanf("%d",&a[i]);
for(i=0;i<m;i++)
    scanf("%d",&b[i]);
for(i=0;i<m;i++)
{
    for(j=0;j<n;j++)
    {
        if(a[j]%b[i]==0)
            c[k++]=a[j];
    }
}
for(i=0;i<n;i++)
{
    for(j=0;j<k;j++)
    {
        if(a[i]==c[j])
        {
            x++;
            f=1;
            break;
        }
    }
    if(f==0)
        printf("%d ",a[i]);
    f=0;
}
if(x==n)
    printf("-1");

}
