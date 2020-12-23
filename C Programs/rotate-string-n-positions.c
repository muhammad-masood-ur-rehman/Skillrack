Rotate String - N Positions
A string S of length L is passed as the input. The program must rotate the string S by N position in forward direction and print the result as the output.
Input Format:
The first line will contain the value of S.
The second line will contain N.
Output Format:
The first line will contain the rotated string value.
Boundary Conditions:
The length L of the string S is from 3 to 100.
0 <= N <= L
Example Input/Output 1:
Input:
cricket
2
Output:
etcrick
Example Input/Output 2:
Input:
truth
5
Output:
truth
#include<stdio.h>
#include <stdlib.h>
int main()
{
char a[100];
int y,i,j=0;
scanf("%s %d",a,y);
for(i=strlen(a)-y;strlen(a)!=j;i++,j++,i%=strlen(a))
printf("%c",a[i]);
}
s,k=input(),int(input())
print(s[-k:]+s[:-k])
import java.util.*;
public class Hello {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        int n=sc.nextInt();
        int d=s.length()-n;
        int l=s.length();
        System.out.print(s.substring(d,l));
        System.out.print(s.substring(0,d));
    }

}
