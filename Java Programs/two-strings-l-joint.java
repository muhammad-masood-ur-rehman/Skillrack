Two Strings - L Joint
Given two strings S1 and S2, where the last letter of one of the strings is same as the first letter of the other string, print the output as given in the Example Input/Output section.
Input Format:
The first line contains S1.
The second line contains S2.
Output Format:
L lines containing the desired output where L is the length of the string whose last letter is same as the first letter of the other string.
Boundary Conditions:
2 <= Length of S1 and S2 <= 100
Example Input/Output 1:
Input:
elephant
tiger
Output:
e****
l****
e****
p****
h****
a****
n****
tiger
import java.util.*;
public class Hello {

    public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        int x = a.length();
        int y = b.length();
        if(a.charAt(x-1) == b.charAt(0))
        {
            for(int i=0;i<x-1;i++)
            {
                System.out.print(a.charAt(i));
                for(int j=0;j<y-1;j++)
                {
                    System.out.print("*");
                }
                System.out.println();
            }
            
            System.out.println(b);
        }
        else
        {
            for(int i=0;i<y-1;i++)
            {
                System.out.print(b.charAt(i));
                for(int j=0;j<x-1;j++)
                {
                    System.out.print("*");
                }
                System.out.println();
            }
            System.out.println(a);
        }
	}
}
