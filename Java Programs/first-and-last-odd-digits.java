First and Last Odd Digits
Given N positive integers, the program must print the integers if the first and last digits are odd digits.
Boundary Condition(s):
1 <= N <= 9999
Input Format:
The first line contains N.
The second line contains N integers separated by space.
Output Format:
The first line contains the specified output
Example Input/Output 1:
Input:
4
21 33 12 15
Output:
33 15
Example Input/Output 2:
Input:
7
123 456 567 21 58 93 103
Output:
123 567 93 103
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String [] b = new String [n];
        for(int i=0;i<n;i++)
        {
            b[i] = sc.next();
        }
        for(int i=0;i<n;i++)
        {
            String temp = b[i];
            int k = temp.length();
            char c = temp.charAt(0);
            char d = temp.charAt(k-1);
            int f = Character.getNumericValue(c);
            int l = Character.getNumericValue(d);
            if(l%2 != 0 && f%2!=0)
            {
                System.out.print(temp + " ");
            }
            
            
        }
	}
}
