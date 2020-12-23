Date Overlap
The program must accept two date ranges as the input. The program must print YES if the date ranges are overlapping. Else the program must print NO as the output.
Input Format:
The first line contains the start date of the first date range.
The second line contains the end date of the first date range.
The third line contains the start date of the second date range.
The fourth line contains the end date of the second date range.
Output Format:
The first line contains either 'YES' or 'NO'.
Example Input/Output:
Input:
20160302
20160402
20160303
20160304
Output:
YES
Python:
x=int(input());f=0
y=int(input())
m=int(input())
n=int(input())
for x in range(x,y+1):
  if x>=m and x<=n:print('YES');f=1;break
if f==0:print('NO')
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int x,y,m,n;
    scanf("%d%d%d%d",&x,&y,&m,&n);
    
    for(x=x;x<=y;++x){
        if(x>=m && x<=n){
            printf("YES");
            return;
        }
    }
    printf("NO");

}
