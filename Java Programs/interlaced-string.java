Interlaced String
Given an input string , accept the input string S and print the string in the interlaced order as shown in the example Input/Output section.
Input Format:
The first line contains the value of String S (which may contain letters, white spaces, special characters, and numbers).
Output Format:
The string S has to be printed in the order of 1st character and (N-1) character, 2nd character and (N-2) character and so on
where N is the length of the string S.
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
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
	 Scanner sc = new Scanner( System.in);
	 String s = sc.nextLine();
	 int n = s.length();
	 int j = 0;
	 int k= n-1;
	 for(int i=0;i<n/2;i++)
	 {
	     System.out.print(s.charAt(j) + " ");
	     ++j;
	     System.out.print(s.charAt(k) + " ");
	     --k;
	 }
	 if(n%2!=0)
	 {
	     System.out.print(s.charAt(n/2));
	 }

	}
}
