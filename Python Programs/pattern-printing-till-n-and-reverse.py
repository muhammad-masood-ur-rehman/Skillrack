Pattern Printing - Till N & Reverse
Pattern Printing - Till N & Reverse: The program must accept an integer N and print 2N lines as shown in the Example Input/Output.
Input Format:
The first line contains N.
Output Format:
2N lines as shown in the Example Input/Output.
Boundary Conditions:
2 <=  N <= 100
Example Input/Output 1:
4
Output:
1
22
333
4444
4444
333
22
1
Example Input/Output 2:
7
Output:
1
22
333
4444
55555
666666
7777777
7777777
666666
55555
4444
333
22
1
n=int(input());p=[]
for i in range(1,n+1):
  l=[]
  for j in range(i):l.append(i)
  for i in l:print(i,end='')
  print();p.append(l)
for i in p[::-1]:
  for j in i:print(j,end='')
  print()
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n,a=1,i,j;
scanf("%d",&n);
for(i=0;i<n;i++)
{
    for(j=0;j<=i;j++)
        printf("%d",a);
    a++;
    printf("\n");
}
for(i=0;i<n;i++)
{
    a--;
    for(j=0;j<n-i;j++)
        printf("%d",a);
    printf("\n");
}

}
