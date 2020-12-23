String Characters Interlace
Given an input string S, accept the input string S and print the string in the interlaced order as shown in the example Input/Output section.
Input Format:
The first line contains the value of String S (may contain letters, white spaces, special characters, and numbers).
Output Format:
The string S has to be printed in the order of 1st character and (N-1) character, 2nd character and (N-2) character and so on where N is the length of the string S.
Boundary Conditions:
1 <= Length of S <= 100
Example Input/Output 1:
Input:
abc321
Output:
a 1 b 2 c 3
Example Input/Output 2:
Input:
pqrs-wxyz
Output:
p z q y r x s w -
import java.util.*;
public class Hello
 {
    public static void main(String[] args)
 {
    Scanner s=new Scanner(System.in);
String str=s.nextLine();
char ch[]=str.toCharArray();
int f=1,g=0,l=ch.length;
char c[]=new char[l];
for(int i=0;i<l;i++)
{
    if(i%2==0)
    {
    c[i]=ch[i-g];
    g++;
    }
    else
    {
    c[i]=ch[l-f];
    f++;
    }
}
for(int i=0;i<l;i++)
System.out.print(c[i]+" ");
    }
}
