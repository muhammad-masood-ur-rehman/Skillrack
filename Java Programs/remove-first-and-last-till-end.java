Remove First And Last Till End
Given a string S, print the string S removing first and last character till no characters are left.
Boundary Condition :
1 <= Length of string S <= 1000
Input Format:
The first line contains S
Example Input/Output 1:
Input:
water
Output :
water
ate
t
Example Input/Output 2:
Input:
keyboard
Output :
keyboard
eyboar
yboa
bo
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
		Scanner sc = new Scanner(System.in);
		String a = sc.next();
        int n = a.length();
        int x = 0;
        int j = 0,k=n-1;
        if(n%2 == 0)
        {
             x = n/2;
        }
        else
        {
             x = n/2;
             x++;
        }
    //    System.out.println(x);
        for(int i=0;i<x;i++)
        {
            for(int r = j;r<=k;r++)
            {
                System.out.print(a.charAt(r));
            }
            j++;
            k--;
            System.out.println();
        }
	}
}
