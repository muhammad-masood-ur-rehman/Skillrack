Reverse Number sign
An integer value N is passed as the input. The program must reverse the sign of N and print -N as the output.
Input Format:
The first line contains N.
Output Format:
The first line contains -N. Boundary Conditions: -999999 <= N <= 999999
Example Input/Output 1:
Input:
125
Output:
-125
Example Input/Output 2:
Input:
-346
Output:
346
Example Input/Output 3:
Input:
0
Output:
0
import java.util.*;
import java.lang.*;
public class Hello {
    public static void main(String[] args) {
    Scanner s=new Scanner(System.in);
    int n=s.nextInt();
    if(Math.abs(n)==n)
    System.out.print(-1*n);
    else
    System.out.println(Math.abs(n));
  }

}
