Leap Year
A year Y will be passed as input.  The program must find if the given year is a leap year or not.  If it is a leap year, print yes else no.
Example 1:
Input:
2000
Output:
yes
Example 2:
Input:
1980
Output:
yes
Example 3:
Input:
400
Output:
yes
Example 4:
Input:
2019
Output:
no
Note: A year is a leap year if it is divisible by 4. If it is a century then it should be divisible by 400.The pseudocode is as given below:If year is divisible by 400 then is_leap_year else if year is divisible by 100 then not_leap_year else if year is divisible by 4 then is_leap_year else not_leap_year
import java.util.*;
public class Hello {
    public static void main(String[] args) {
           Scanner s=new Scanner(System.in);
            int n=s.nextInt();
            if((n%400==0)||(n%4==0)&&(n%100!=0))
            System.out.print("yes");
            else
            System.out.print("no");
            }
}
#include<stdio.h>
#include <stdlib.h>

int main()
{
int year;
scanf(“%d”,&year);
if((year%4==0&&year%100!=0)||(year%400==0))
printf(“yes”);
else
printf(“no”);

}
