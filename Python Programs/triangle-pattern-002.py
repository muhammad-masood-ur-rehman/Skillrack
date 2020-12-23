Triangle Pattern - 002
Given an odd integer N, print a triangle with * as mentioned in the below examples.
Input Format: The first line contains N.
Output Format: N/2 + 1 lines containing the triangle pattern as shown in the example input/output.
Boundary Conditions: 1 <= N <= 999
Example Input/Output 1:
Input:
5
Output:
!!*!!
!***!
*****

Example Input/Output 2:
Input:
9
Output:
!!!!*!!!!
!!!***!!!
!!*****!!
!*******!
*********
n=int(input())
for i in range(n//2+1):
    print('!'*((n//2)-i)+"*"*(2*i+1)+'!'*((n//2)-i))
#include<stdio.h>
int main(){
            int n,t,i,y;
            char *p="********************************************************************************";
            char *s="!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
            scanf("%d",&n);
            t=n/2;
            for(i=1;i<=n;i+=2)
            {
                        printf("%*.*s",t,t,s);     //same as printf("%*.*s%*.*s%*.*s\n",t,t,s,i,i,p,0,t,s);
                        printf("%*.*s",i,i,p);     //----^
                        printf("%*.*s\n",0,t,s); //----^
                        t--;
            }
            return 0;
}

