Next Number Palindrome
Given a number N, the program must print the next palindromic number P. 
Boundary Conditions:9 < N < 100000 

Input Format:First line will contain the number N 
Output Format: First line will contain the next palindromic number P. 
Sample Input/Output: 
Example 1:
 Input: 909 
Output:919
 
Example 2:
 Input: 2131 
Output: 2222
import java.util.*;
import java.lang.*;
class Palindrome
{
 public static void main (String[] args) 
 {
 Scanner s=new Scanner(System.in);
 int n=s.nextInt();
 n++; 
 for(;;n++){
     if(String.valueOf(n).equals(new StringBuilder(String.valueOf(n)).reverse().toString()))
     {
     System.out.print(n);
     break;
 }
 }
 }
}
