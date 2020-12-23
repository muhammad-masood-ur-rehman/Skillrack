Move M Words - End Reverse
The program must accept a string S which contains N words and move the first M words to the last in the reverse order.
Input format:
The first line contains S.
Boundary Conditions:
M <= N <= 50
10 <= Length of S <= 200
Example Input/Output 1:
Input:
one two three four five
3
Output:
four five three two one
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String a[] = s.split(" ");
        int n = sc.nextInt();
        for(int i = n;i<a.length;i++)
        {
            System.out.print(a[i] + " ");
        }
        for(int i=n-1;i>=0;i--)
        {
            System.out.print(a[i] + " ");
        }
	}
}
