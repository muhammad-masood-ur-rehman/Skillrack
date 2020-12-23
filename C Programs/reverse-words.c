Reverse words
Given a string S as the input Write a program to print the reverse order of the words in the string S.
Input Format:
The first line contains S.
Output Format:
The first line contains the words in the reverse order.
Boundary Conditions:
1 <= Length of S <= 100
Example Input/Output 1:
Input:
I Love India
Output:
India Love I
Example Input/Output 2:
Input:
Something must be printed!
Output:
printed! be must Something
import java.util.*;
public class Hello {
    public static void main(String[] args) {
                        Scanner s=new Scanner(System.in);
                        String str=s.nextLine();
                        String a[]=str.split(" ");
                        for(int i=a.length-1;i>=0;i--)
                        System.out.print(a[i]+" ");
            }
}
#include<stdio.h>
#include<string.h>
int main()
{
char s[100];
fgets(s,100,stdin);
char *tok;
char *b[100];
int i,j=0;
tok=strtok(s," ");
while(tok!=NULL)
{
    b[j++]=tok;
    tok=strtok(NULL," ");
}
for(i=j-1;i>=0;i--)
printf("%s ",b[i]);

}
v=[i for i in input().split()]
print(*v[::-1])

One liner:

print(' '.join(input().split()[::-1]))
