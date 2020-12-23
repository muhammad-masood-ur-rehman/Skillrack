Strict Professor - Class Cancellation
In a college ,  a professor is strict and mandates that at least M students out of the total N students must arrive on time to his class.Else he would cancel the class. The start time of the class is also passed as the input.The individual arrival time for N students is also passed as input in 24 hours format.
The program must print if the class was cancelled or not.
Example 1:
Input:
5 3
9:30
9:30 9:38 9:31 9:32 9:31
Output:
Yes
Explanation:
4 out of the students arrived late, which means only one arrived on time. As the professor has mandated 3 out of the 5 must arrive on time, the class was cancelled and hence Yes is printed as the output.
#include<stdio.h>
#include <stdlib.h>

int main()
{
 int max,n,count=0,h,m,min,hour;
 scanf("%d%d",&max,&n);
 scanf("%d:%d",&h,&m);
 while(scanf("%d:%d",&hour,&min)>0)
 {
 if(hour==h&&min<=m)
 count++;
 else if(hour<h)
 count++;
 }
 
 if(count>=n)
 printf("No");
 else
 printf("Yes");

}
