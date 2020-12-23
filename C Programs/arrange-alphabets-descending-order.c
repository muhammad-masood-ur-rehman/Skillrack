Arrange Alphabets - Descending Order
A string S (with only LOWER case alphabets and length from 3 to 100) will be passed  as input. The program should print the alphabets in the string in descending order.
Input Format:
The first line will contain S.
Output Format:
The first line will contain the alphabets present in S in descending order.
Example Input/Output 1:
Input:
cake
Output:
keca
Example Input/Output 2:
Input:
innovation
Output:
vtonia
import itertools
print(''.join(i for i,j in itertools.groupby(sorted(input(),reverse=True))))
n=input()
print(''.join(sorted(set(n)))[::-1])
import java.util.*;
public class Hello {

public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
String s=sc.next();
char[] c=s.toCharArray();
TreeSet<Character> h=new TreeSet<Character>();
Iterator it;
for(int i=0;i<c.length;i++)
h.add(c[i]);
it=h.descendingIterator();
while(it.hasNext())
{
    System.out.print(it.next());
}
    }
}
#include<stdio.h>
#include <stdlib.h>
#include<string.h>
int main()
{
char s[100],t,b[100];
scanf("%s",s);
int i,j,k=0,c=0;
for(i=0;i<strlen(s);i++)
{
    for(j=0;j<i;j++)
    {
        if(s[i]==s[j])
            c=1;
    }
    if(c==0)
        b[k++]=s[i];
    c=0;
}
for(i=0;i<strlen(b)-1;i++)
{
    for(j=i+1;j<strlen(b);j++)
    {
        if(b[i]>b[j])
        {
            t=b[i];
            b[i]=b[j];
            b[j]=t;
        }
    }
}
for(i=strlen(b)-1;i>=0;i--)
printf("%c",b[i]);

}
