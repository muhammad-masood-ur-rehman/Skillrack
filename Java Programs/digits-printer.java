Digits Printer
Given a number N. print all the digits of the number N in descending order.
Boundary Condition:
0 <= N <= 99999999999999
Input Format:
The first line contains the value of N.
Output Format:
The first line contains all the digits of the number N printed in descending order.
Example Input/ Output 1:
Input:
12447511
Output:
75442111
Example Input/ Output 2:
Input:
019454401
Output:
95444110
import java.util.*;
public class Hello {

    public static void main(String[] args) {
  Scanner sc=new Scanner(System.in);
  String s=sc.next();
  char ch[]=s.toCharArray();
  int i,j,k,l=s.length();
  Arrays.sort(ch);
  for(i=l-1;i>0;i--)
      System.out.print(ch[i]);
  if(ch[0]!='0'&&ch[1]!='0')
      System.out.print(ch[0]);
  else if(ch[0]=='0'&&ch[1]!='0')
  System.out.print(ch[0]);
 }
}
